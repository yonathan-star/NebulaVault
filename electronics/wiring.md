# Harness and power plan

Source of truth: `netlist.csv`. Pico numbers are **physical header pins**, not GP numbers. U2 is DIP14, notch upward, counted counterclockwise. Solder this harness onto the Perma-Proto; this project has no custom PCB, and no Gerbers are claimed.

| Function | Pico GP | Physical pin | Destination |
|---|---:|---:|---|
| SDA | 4 | 6 | OLED SDA |
| SCL | 5 | 7 | OLED SCL |
| Encoder A | 10 | 14 | Encoder A; internal 3.3V pull-up |
| Encoder B | 11 | 15 | Encoder B; internal 3.3V pull-up |
| Encoder press | 12 | 16 | Switch contact; other contact to ground |
| Servo PWM | 15 | 20 | AHCT input pin5 -> output6 -> servo signal |
| Pixel data | 16 | 21 | AHCT input2 -> output3 -> 470 ohm -> ring DIN |
| 3.3V | — | 36 | OLED VIN only |
| USB 5V | — | 40 | Star connection: servo red, ring5V, U2 pin14 |
| Ground | — | 38 | Common star ground |

U2: pins1 and4 to GND enable the two used channels. Tie unused input9 and12 to GND; disable unused outputs8 and11 by tying enables10 and13 to **5V**. Outputs8 and11 remain unconnected. C2=100nF directly between U2 pins14/7. C1=4700uF positive to5V, striped negative toGND near the servo/ring feed. Keep the 470-ohm resistor near ring DIN. Never connect 5V to a Pico GPIO. The OLED is powered from3.3V, including its I2C pull-ups.

Power is external supply -> Pico micro-USB -> VBUS pin40 -> separate short power branches. Never feed motor current through a GPIO or the Pico3V3 regulator. Use parallel conductors on 5V and GND if using the thin jumper set, and keep them short. No external battery, charger, exposed mains, or simultaneous separate power injection is used. Disconnect servo and ring power while programming from a computer USB port; reconnect the external adapter for operation. Supply rating is2.5A; a 1A servo transient plus a full-white ring at60mA/pixel and120mA logic/display gives a **planning allowance** of1.84A, not a measured load. The actual firmware caps channels at32/255, reducing the planned ring contribution to about90mA. Servo current, USB contact drop, capacitor inrush and brownout behavior still need bench testing. Capacitor buffering does not make an undersized supply adequate.

Validate motor lead colors from the supplier: brown/black ground, red positive, orange/yellow signal. Verify encoder pins with a meter before soldering; manufacturer views may be from the shaft side. Swap A/B or invert decoding if the ring moves in the opposite direction. Test the OLED address with `i2c.scan()`; expected0x3C.
