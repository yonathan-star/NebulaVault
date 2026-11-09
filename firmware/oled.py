"""Minimal SSD1306 128x32 I2C driver using MicroPython framebuf.
Original implementation for Yonathan’s original project. Commands follow SSD1306 datasheet.
"""
import framebuf

class OLED:
    def __init__(self, i2c, address=0x3c):
        self.i2c = i2c
        self.address = address
        self.buffer = bytearray(512)
        self.fb = framebuf.FrameBuffer(self.buffer, 128, 32, framebuf.MONO_VLSB)
        for cmd in (0xae, 0xd5, 0x80, 0xa8, 31, 0xd3, 0, 0x40,
                    0x8d, 0x14, 0x20, 0, 0xa1, 0xc8, 0xda, 0x02,
                    0x81, 0x7f, 0xd9, 0xf1, 0xdb, 0x40, 0xa4, 0xa6, 0xaf):
            self.command(cmd)

    def command(self, cmd):
        self.i2c.writeto(self.address, bytes((0, cmd)))

    def draw(self, phase, message):
        self.fb.fill(0)
        self.fb.text('NEBULA VAULT', 0, 0, 1)
        self.fb.text(phase[:16], 0, 12, 1)
        self.fb.text(message[:16], 0, 24, 1)
        for cmd in (0x21, 0, 127, 0x22, 0, 3):
            self.command(cmd)
        self.i2c.writeto(self.address, b'\x40' + self.buffer)
