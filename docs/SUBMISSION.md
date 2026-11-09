# Nebula Vault — submission fields

**Yonathan’s design project, prepared for submission; acceptance unverified.** These are finished answers for the fields identified in the public instructions, not a claim that the locked final form was accessed.

**Project name:** Nebula Vault

**Week/category:** Week 5 — Freestyle / Design Your Own

**Requested tier:** Tier 3, requested, subject to reviewer approval. The owner confirmed 20 personal design hours; actual session dates and allocations were not supplied.

**Description:** Nebula Vault is a small escape-room artifact disguised as a damaged spacecraft's core container. A glowing orbital dial, a narrow status screen and a hidden servo latch turn the lid into the final step of a two-stage puzzle. First, align three numbered signals using alternating turns. Then watch the light ring and repeat its short–long–short pulse timing. Recover the sequence and the latch releases the compartment. The enclosure, lid catches, light diffuser and latch extension are custom parametric parts. A manual release slot keeps the contents accessible if the motor or power fails.

**Why this project?** A combination lock asks for a number; this prop asks the player to operate something that feels like a machine. The dial provides the spatial puzzle, the ring supplies the timing clue, and the physical latch makes success tangible.

**What is original?** The enclosure layout, the two-stage interaction, alternating-direction rules, custom printed latch/keeper geometry and associated firmware were created for this project. Off-the-shelf electronics supply power, sensing, light and movement. This is not a kit assembly or a reskin of one of the reviewed community projects.

**How does it work?** A Pico reads the encoder with quadrature interrupts and a debounced push switch. Three correct directional alignments lead to a four-flash playback. The player makes a starting tap and reproduces the three intervals, 450/900/450 ms, within ±180 ms. Success commands the servo open; failure restarts the puzzle after 1.5 seconds. A 2.5-second hold resets and requests release. Servo pulses stop after 650 ms to avoid continuous stall. A 5 V AHCT buffer shifts data and motor-control logic; OLED pull-ups remain at 3.3 V.

**Design files:** cad/model.py; assembly and individual STEP models; seven print-ready STL files; electronics/netlist.csv; electronics/schematic.svg; full MicroPython sources.

**Verification:** Executed desktop tests exercise success, wrong direction, wrong position, missing movement, timing limits, timeouts, resets and pixel limits. CAD geometry reports test solid validity and digital interference. See evidence/test-results.txt and cad/geometry-report.json for actual results. No physical device, torque measurement, solder test, optical test or completed print is claimed.

**BOM:** bom.csv and procurement/BOM.md; known merchandise subtotal is computed there. All unknown fabrication, shipping and tax costs are labeled. Vendor cart evidence has its own status report.

**Repository URL:** Publication not yet verified; no repository URL is invented.

**Cover:** previews/assembled.png — a render of the actual CAD geometry, not a physical photograph. Deterministic render of the supplied CAD; no physical photograph is claimed. Program acceptance of this cover remains unverified.

**Journal/hours:** Owner-confirmed total: 20 actual design hours. Existing preparation notes are retained; no session dates, individual hour allocations, Lapse recordings or physical results are invented.

**Idea / 5-hour / 15-hour / final reels:** Four distinct 30–60 second videos are included in media/. They use actual project-file visuals, labeled CAD renders and a labeled recorded software simulation, with narration.

**Current result:** A reviewable digital prototype with testable logic and mechanical source. Original project authorship is Yonathan’s. Reviewer eligibility decisions remain pending. Publication and live acceptance remain unverified. The priced vendor carts are complete; printing, workshop costs and physical verification remain pending.
