"""MicroPython RP2040 entry point. See electronics/netlist.csv before wiring.
Firmware for Yonathan’s original project; bench verification and servo calibration remain required.
"""
import time
import machine
from machine import Pin, PWM, I2C
import neopixel
from core import Vault
from oled import OLED

LOCK_US = 1500
OPEN_US = 1000
SERVO_SETTLE_MS = 650
BUTTON_DEBOUNCE_MS = 35

servo = PWM(Pin(15), freq=50)
pixels = neopixel.NeoPixel(Pin(16), 12)
encoder_a = Pin(10, Pin.IN, Pin.PULL_UP)
encoder_b = Pin(11, Pin.IN, Pin.PULL_UP)
button = Pin(12, Pin.IN, Pin.PULL_UP)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
display = None
try:
    display = OLED(i2c, address=0x3c)
except OSError as err:
    print('OLED unavailable; puzzle still runs:', err)

# Full quadrature cycle; illegal 2-bit jumps contribute no travel.
TRANSITIONS = (0, -1, 1, 0, 1, 0, 0, -1, -1, 0, 0, 1, 0, 1, -1, 0)
old_ab = (encoder_a.value() << 1) | encoder_b.value()
quarter_steps = 0
pending = 0

def encoder_irq(_pin):
    global old_ab, quarter_steps, pending
    ab = (encoder_a.value() << 1) | encoder_b.value()
    if (old_ab ^ ab) == 3:
        quarter_steps = 0
    else:
        quarter_steps += TRANSITIONS[(old_ab << 2) | ab]
        if quarter_steps >= 4:
            pending += 1
            quarter_steps = 0
        elif quarter_steps <= -4:
            pending -= 1
            quarter_steps = 0
    old_ab = ab

encoder_a.irq(encoder_irq, Pin.IRQ_RISING | Pin.IRQ_FALLING)
encoder_b.irq(encoder_irq, Pin.IRQ_RISING | Pin.IRQ_FALLING)
vault = Vault()
last_lock = None
servo_until = 0
last_display = -100
raw_button = button.value()
stable_button = raw_button
changed_at = 0
pressed_at = None
long_handled = False
previous_tick = time.ticks_ms()
now = 0

def move_latch(locked, current):
    global servo_until
    us = LOCK_US if locked else OPEN_US
    servo.duty_u16(int(us * 65535 / 20000))
    servo_until = current + SERVO_SETTLE_MS

try:
    while True:
        tick = time.ticks_ms()
        now += time.ticks_diff(tick, previous_tick)
        previous_tick = tick
        irq_state = machine.disable_irq()
        delta = pending
        pending = 0
        machine.enable_irq(irq_state)
        # Apply each detent separately so travel/direction stay faithful.
        for _ in range(abs(delta)):
            vault.rotate(1 if delta > 0 else -1, now)
        raw = button.value()
        if raw != raw_button:
            raw_button = raw
            changed_at = now
        if now - changed_at >= BUTTON_DEBOUNCE_MS and stable_button != raw:
            stable_button = raw
            if not raw:
                pressed_at = now
                long_handled = False
                # Tap on press, not release: hold duration must not alter rhythm.
                vault.press(now)
            else:
                pressed_at = None
        if pressed_at is not None and now - pressed_at >= 2500 and not long_handled:
            vault.reset(now)
            long_handled = True
        vault.tick(now)
        if vault.locked != last_lock:
            move_latch(vault.locked, now)
            last_lock = vault.locked
        if servo_until and now >= servo_until:
            servo.duty_u16(0)  # no continuous holding torque or prolonged stall
            servo_until = 0
        colors = vault.lights(now)
        for i, rgb in enumerate(colors):
            pixels[i] = rgb
        pixels.write()
        if now - last_display >= 100:
            if display:
                try:
                    display.draw(vault.phase, vault.message)
                except OSError as err:
                    print('OLED I2C error:', err)
                    display = None
            last_display = now
        time.sleep_ms(5)
finally:
    # Request open on controlled script exit; power loss cannot move a servo.
    servo.duty_u16(int(OPEN_US * 65535 / 20000))
    time.sleep_ms(SERVO_SETTLE_MS)
    servo.deinit()
    pixels.fill((0, 0, 0))
    pixels.write()
