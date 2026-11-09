# Final bill of materials

Prices and availability were verified in the actual carts on November 8, 2026, New York time. Every priced line below matches a vendor cart quantity. The two custom-print batches and workshop consumables are separately disclosed as unquoted, rather than assigned invented prices. There are 15 priced line items across two vendors.

| Ref | Exact part / purchase package | Buy qty | Unit USD | Extended USD | Vendor |
|---|---|---:|---:|---:|---|
| U1 | Pico RP2040 with loose headers — 4883 | 1 | $5.00 | $5.00 | [Adafruit](https://www.adafruit.com/product/4883) |
| ENC1 | 24-pulse encoder with push switch and knob — 377 | 1 | $4.50 | $4.50 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/377/7902287) |
| LED1 | NeoPixel 12 RGB ring — 1643 | 1 | $8.95 | $8.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1643/5154677) |
| DISP1 | 128x32 SSD1306 I2C OLED — 4440 | 1 | $12.50 | $12.50 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4440/10824271) |
| M1 | TowerPro SG92R micro servo with horns and screws — 169 | 1 | $5.95 | $5.95 | [Adafruit](https://www.adafruit.com/product/169) |
| U2 | 5V TTL-input quad buffer, DIP14 — SN74AHCT125N | 1 | $0.95 | $0.95 | [DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/SN74AHCT125N/375798) |
| C1 | 4700uF >=10V radial electrolytic — 1589 | 1 | $1.95 | $1.95 | [Adafruit](https://www.adafruit.com/product/1589) |
| C2 | 100nF 50V X7R radial decoupling capacitor — K104K15X7RF5TL2 | 1 | $0.29 | $0.29 | [DigiKey](https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/K104K15X7RF5TL2/286538) |
| R1 | 470-ohm 1/4W 5% axial resistor — CF14JT470R | 1 | $0.10 | $0.10 | [DigiKey](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/CF14JT470R/1830342) |
| PROTO1 | Half-size Perma-Proto solder board — 1609 | 1 | $4.50 | $4.50 | [Adafruit](https://www.adafruit.com/product/1609) |
| WIRE1 | Female-female 150mm jumper wires, pack of 20 — 1950 | 2 | $1.95 | $3.90 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1950/6827084) |
| PWR1 | 5.25V 2.5A supply with Micro-USB cable, US plug — 1995 | 1 | $8.25 | $8.25 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1995/7902284) |
| HW1 | M3 nylon screws/nuts/standoffs 420-piece assortment — 4685 | 1 | $16.95 | $16.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4685/13180686) |
| PRINT1 | Custom PLA body, lid, horn extension, OLED strap, dial cap and fit coupon — NebulaVault R1: six named STL files | 1 | Unknown | Unknown | [Local FDM printing — quote required](../cad/model.py) |
| PRINT2 | Custom natural/translucent PLA diffuser — NebulaVault R1 diffuser.stl | 1 | Unknown | Unknown | [Local FDM printing — quote required](../cad/diffuser.stl) |
| TIES1 | 2.5mm wide, 99mm long nylon locking cable tie — PLT1M-C | 4 | $0.25 | $1.00 | [DigiKey](https://www.digikey.com/en/products/detail/panduit-corp/PLT1M-C/280033) |
| USB1 | USB-A to Micro-B data cable, 3 foot — 592 | 1 | $2.95 | $2.95 | [Adafruit](https://www.adafruit.com/product/592) |
| CONSUMABLES | Workshop allocation: solder, insulation/heat-shrink, insulating mounting tape/shims — See build guide for required use; existing stock unverified | 1 | Unknown | Unknown | Workshop stock or local supply — not priced |


## Recorded totals

| Cost | USD | Status |
|---|---:|---|
| Adafruit merchandise, 5 line items | $20.35 | Live cart verified |
| DigiKey merchandise, 10 line items | $57.39 | Live cart verified |
| All priced merchandise | **$77.74** | Sum reconciled to BOM |
| DigiKey USPS Ground Advantage | $4.99 | Vendor estimate selected |
| DigiKey tariff | $0.15 | Vendor estimate |
| Known combined amount | **$82.88** | Excludes all unknowns below |
| Adafruit shipping | Unknown | Calculated in checkout; not treated as free |
| Sales tax, both vendors | Unknown | Destination-dependent; not treated as zero |
| Custom printing/material/service | Unknown | No quote or printer-stock claim |
| Workshop consumable allocation | Unknown | Existing stock and cost unverified |

There is **$17.12** between the known $82.88 and the $100 funding ceiling. Every remaining charge must fit inside that amount for a fully funded build. Therefore budget compliance is **not established**. Tools and printer access are not included or assumed verified. Vendor estimates can change at checkout; no checkout or order was completed.

Supply changes: the backordered DigiKey Perma-Proto was removed and the same part was added at Adafruit. The unavailable Adafruit resistor pack was replaced by a single electrically matching Stackpole CF14JT470R at DigiKey. The programming cable and four exact 2.5 mm cable ties are now priced and in their carts.

M3 hardware use: four M3 screws secure the diffuser and OLED strap; the purchased assortment provides length choices for the measured stack and spares. The servo includes its own horn/center screw. Four PLT1M-C ties secure the servo and horn extension. Two jumper-wire packs supply 40 conductors; cut selected leads for solder tails and retain parallel conductors on power feeds as described in the wiring guide.
