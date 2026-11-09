# Nebula Vault — updated BOM and cost notes

**Estimated total: $137.13 — $37.13 over the $100 allowance.**

Basis: supplied November 8, 2026 checkout reconciliation for ZIP 33026. This update carries those estimates forward; no fresh checkout verification was performed. No order or payment was placed. The existing project package has not been changed.

## Purchase BOM

The linked CSV includes exact part identifiers, purchase quantities and vendor URLs. Quantities below are purchase quantities; wire quantities are packs.

| Item / part | Qty | Unit USD | Extended USD | Vendor |
|---|---:|---:|---:|---|
| Pico RP2040 with loose headers — 4883 | 1 | $5.00 | $5.00 | [Adafruit](https://www.adafruit.com/product/4883) |
| 24-pulse encoder with push switch and knob — 377 | 1 | $4.50 | $4.50 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/377/7902287) |
| NeoPixel 12 RGB ring — 1643 | 1 | $8.95 | $8.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1643/5154677) |
| 128x32 SSD1306 I2C OLED — 4440 | 1 | $12.50 | $12.50 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4440/10824271) |
| TowerPro SG92R micro servo with horns and screws — 169 | 1 | $5.95 | $5.95 | [Adafruit](https://www.adafruit.com/product/169) |
| 5V TTL-input quad buffer, DIP14 — SN74AHCT125N | 1 | $0.95 | $0.95 | [DigiKey](https://www.digikey.com/en/products/detail/texas-instruments/SN74AHCT125N/375798) |
| 4700uF >=10V radial electrolytic — 1589 | 1 | $1.95 | $1.95 | [Adafruit](https://www.adafruit.com/product/1589) |
| 100nF 50V X7R radial decoupling capacitor — K104K15X7RF5TL2 | 1 | $0.29 | $0.29 | [DigiKey](https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/K104K15X7RF5TL2/286538) |
| 470-ohm 1/4W 5% axial resistor — CF14JT470R | 1 | $0.10 | $0.10 | [DigiKey](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/CF14JT470R/1830342) |
| Half-size Perma-Proto solder board — 1609 | 1 | $4.50 | $4.50 | [Adafruit](https://www.adafruit.com/product/1609) |
| Female-female 150mm jumper wires, pack of 20 — 1950 | 2 | $1.95 | $3.90 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1950/6827084) |
| 5.25V 2.5A supply with Micro-USB cable, US plug — 1995 | 1 | $8.25 | $8.25 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1995/7902284) |
| M3 nylon screws/nuts/standoffs 420-piece assortment — 4685 | 1 | $16.95 | $16.95 | [DigiKey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4685/13180686) |
| 2.5mm wide, 99mm long nylon locking cable tie — PLT1M-C | 4 | $0.25 | $1.00 | [DigiKey](https://www.digikey.com/en/products/detail/panduit-corp/PLT1M-C/280033) |
| USB-A to Micro-B data cable, 3 foot — 592 | 1 | $2.95 | $2.95 | [Adafruit](https://www.adafruit.com/product/592) |
| Panchroma Translucent PLA; Translucent Natural / Semi-Transparent; 1.75 mm; 1 kg — CA02037 | 1 | $19.99 | $19.99 | [Polymaker](https://shop.polymaker.com/products/translucent-pla?variant=46478202765369) |
| Solder, insulation/heat-shrink, insulating mounting tape/shims — No itemized SKU breakdown supplied | 1 | $19.95 | $19.95 | Prior consumables estimate |

**Purchased goods and carried consumables: $117.68.** Shipping, tariff and taxes add $19.45.

## Checkout totals

| Vendor / allocation | Goods | Shipping | Tariff | Tax | Total |
|---|---:|---:|---:|---:|---:|
| Adafruit | $20.35 | $7.46 | — | $1.42 | **$29.23** |
| DigiKey | $57.39 | $4.99 | $0.15 | $4.03 | **$66.56** |
| Polymaker | $19.99 | FREE | — | $1.40 estimated | **$21.39** |
| Carried consumables | $19.95 | Unknown / not separately itemized | — | Unknown / not separately itemized | **$19.95 carried estimate** |
| **Project estimate** | | | | | **$137.13** |

The $19.95 consumables amount is an aggregate carried from prior pricing. Its individual packages, vendor links, availability and treatment of shipping/tax are unverified. No additional unknown consumables charges have been invented or added to the estimate.

## Changes to apply elsewhere

- Replace the previous provisional $102.83 total with **$137.13**. DigiKey shipping $4.99 and tariff $0.15 were already included in that baseline; do not add them a second time.
- Exclude every outsourced printing-service charge. Home printing uses the user-reported Bambu Lab P1S or A1 mini.
- Purchase **one 1 kg spool of Polymaker Panchroma Translucent Natural / Semi-Transparent PLA, 1.75 mm, SKU CA02037**. The same material covers all seven parts: body, lid, horn extension, OLED strap, dial cap, fit coupon and diffuser. There is no separately purchased opaque enclosure spool.
- Consequently, the planned enclosure is natural/translucent. Any navy/turquoise CAD preview should be described as illustrative part colors, not the purchased material finish.
- No separate per-part printing charge is added: material is budgeted through the whole spool. Actual consumption, fit, supports, calibration waste and reprint allowance still require slicing and physical verification. No print weight or time is established.
- Suggested starting settings carried from the build guide: 0.2 mm layers, four perimeters, approximately 20% infill; latch six perimeters or solid. These are proposed settings, not tested results.
- The current estimate exceeds the $100 allowance by **$37.13**. It does not demonstrate compliance with the Tier 3 budget. Other eligibility and video limitations remain outside this BOM-only update.

## Estimate limits and availability

Electronics quantities match the previously checked carts: Adafruit five lines (one each); DigiKey ten lines (encoder, buffer, capacitor, ring, OLED, supply, hardware kit and resistor one each; wires two packs; ties four). Previously recorded availability was in stock on November 8; availability was not refreshed here.

Adafruit shipping is USPS Ground Advantage (5–8 business days). DigiKey's selected $4.99 Ground Advantage rate applies under its 15 oz limit; the vendor may change service and charges if overweight. Polymaker Economy delivery is 3–7 business days and was explicitly free in the supplied ZIP-based checkout estimate via PM_BFCM2026_USCA_FREESHIPPING. The filament checkout lacked full street/contact information, so its $1.40 tax and $21.39 total may change.

All amounts are checkout estimates, not paid invoices or binding quotes. The attached Adafruit tax screenshot supports merchandise $20.35 and tax $1.42; the other figures are carried from the supplied reconciliation text.

## Files

- [Updated purchase BOM](NebulaVault-updated-BOM.csv)
- [Cost summary](NebulaVault-updated-cost-summary.csv)
