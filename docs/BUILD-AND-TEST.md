# Assembly, operation and troubleshooting

This is a design-stage build guide. Every fabrication or bench step below is a future action, not a record of work completed.

## Tools and preparation

Obtain printer access, a soldering iron, multimeter, hand tools, an M3 tap, and a data-capable Micro-USB cable. Confirm the actual parts against the BOM. The board and motor reference shapes are simplified envelopes, not certified manufacturer models. Check the servo shaft offset, horn dimensions, encoder shaft and OLED board before printing the full enclosure.

## Print and fit

1. Print `fit_coupon.stl` first. It provides holes around a nominal 6 mm shaft with radial clearances from 0.2 to 0.6 mm. Choose the fit using a measured shaft or pin. The shell's skirt clearance starts at 0.4 mm per side.
2. Print the body upright. Rotate the lid so its broad outer face is on the bed if that gives a cleaner result; review the engraved lettering and support contact. Exported STLs sit on Z=0 but still require slicer orientation and support choices.
3. Starting settings: 0.2 mm layers, four perimeters, about 20% infill. Use six perimeters or solid fill for the small latch. Print the diffuser in natural or translucent PLA. These are untested starting settings, not a validated print profile.
4. The shelf, rear retaining features and keeper may require localized supports. Remove them without rounding off the mating faces. Deburr, test empty, and change the source if the parts bind. Do not force the lid into place.

## Mount the parts

The encoder mounts through its 7.4 mm center hole with the supplied hardware. Fit the ring under the twelve light ports. Its PCB sits below the lid; the translucent printed ring sits above the ports. Use the modeled post/tab locations and insulating mounting tape as needed. The driver board has no exact mounting-hole model; check it against the purchased part.

Use the printed strap and suitable insulating shims to retain the OLED beneath its window. Tap the 2.6 mm pilot holes M3 before fitting the nylon screws. The strap-to-board stack must be shimmed after measuring the actual board. Do not tighten a strap directly against fragile display glass.

Seat the Perma-Proto on the rear ledges and retain it with insulated mounting tape. Keep solder joints clear of hardware. Secure the servo to its shelf with two small cable ties through the 3 mm slots. Fasten the printed extension to the supplied horn with two more miniature ties through its slots. Retain the horn with its supplied center screw only after calibration.

Leave a service loop in the lid wiring so the lid can be tilted and lifted without pulling connectors. Label plugs before closing the box.

## Wire and program

Follow `electronics/netlist.csv` and `electronics/wiring.md`. Pico numbers in the netlist are physical header pins; GP numbers in the firmware are logical GPIO identifiers. Confirm encoder pins with a multimeter, since shaft-side and solder-side drawings can be reversed.

Inspect for shorts without power. Verify the electrolytic capacitor's polarity, AHCT pin numbering, the two enabled channels, disabled unused channels, and the shared ground. No 5 V node may touch a Pico GPIO. The OLED is powered at 3.3 V so its I2C pull-ups stay compatible.

Disconnect motor and ring power while programming from computer USB. Hold BOOTSEL while connecting a data cable, install official stable MicroPython for Raspberry Pi Pico RP2040 from https://micropython.org/download/RPI_PICO/, then copy `main.py`, `core.py` and `oled.py` to the board using Thonny or mpremote. The needed `machine`, `neopixel` and `framebuf` modules are included in MicroPython.

Disconnect the computer, reconnect the external adapter, and check the display and ring before connecting the motor. Do not inject a separate power source into VBUS while USB power is connected. A missing OLED prints an error and lets the game run; after fixing I2C, reset to re-enable display writes.

## Calibrate the latch

Remove the horn and keep the lid off. The starting values are 1000 µs for open and 1500 µs for locked, at 50 Hz. Fit the horn so the locked extension points toward the keeper. Open should rotate it sideways clear of the keeper. Adjust `OPEN_US` and `LOCK_US` to the real assembly.

If the servo buzzes or presses against a stop, disconnect power and correct the angle or geometry. Do not blindly increase the pulse extremes. The firmware removes pulses after 650 ms, so verify that the latch stays in the intended position without active holding torque.

With the empty lid installed, prove the manual release works while power is off. The rear slot gives tool access to the horn; it is intentionally not a security feature.

## Operation

Close the lid, press to arm, then turn clockwise to 03 and press. Turn counterclockwise to 08 and press. Turn clockwise to 01 and press. The final turn into each alignment must match the direction, and the first stage requires actual movement.

Watch four flashes. After playback finishes, tap once to start, then reproduce 450, 900 and 450 ms intervals with three further presses. The game accepts ±180 ms per gap. Correct timing releases the latch. Failure returns to stage one after 1.5 seconds. A 2.5-second hold requests reset and release. Boot requests open; loss of power cannot move the servo.

## Physical acceptance checklist

| Check | Proposed acceptance | Actual result |
|---|---|---|
| Lid fit | No forced flex; rear tongues and keeper engage and release | Not run |
| Manual recovery | Open without power or damage | Not run |
| Motor endpoints | No stall, buzzing or forced stop | Not run |
| Supply behavior | Meets component rails during movement; no reset | Not run |
| Inputs | 100 slow detents each direction and 20 presses recognized | Not run |
| Puzzle | Ten successes and ten intentional failures behave correctly | Not run |
| Endurance | 50 empty-box cycles without sticking or loosening | Not run |
| Visibility | All ports visible, OLED legible, acceptable glare | Not run |

## Troubleshooting

| Symptom | Checks and correction |
|---|---|
| OLED blank | Scan I2C for 0x3C; verify power, ground, SDA/SCL, SSD1306 and 128×32 configuration. Reset after fixing wiring. |
| Pixels flicker | Check common ground, 5 V feed, AHCT pins, resistor and DIN direction. Shorten the data wire. |
| Reset on motor movement | Inspect supply drop, cable resistance, capacitor inrush, ground path and mechanical stall. Remove horn and test separately. A bigger capacitor alone does not fix an undersized supply. |
| Dial backwards | Swap A/B or invert the decoder direction after confirming pinout. |
| Dial skips | Check bounce, detents per quadrature cycle and wiring. Fast rotation during NeoPixel writes still needs a bench test. |
| Correct number rejected | Final direction must be clockwise/counterclockwise/clockwise; actual movement is required. |
| Rhythm rejected | Wait for playback to finish. Make a starting tap followed by three timed gaps. Press edges, not releases, determine timing. |
| Lid stuck | Unplug power, use the rear slot, inspect keeper alignment, and recalibrate with the lid off. Do not force the motor. |
