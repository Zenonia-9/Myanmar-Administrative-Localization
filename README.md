# Myanmar Administrative Localization (l10n_mm_pcode)

Odoo module that adds Myanmar administrative hierarchy fields based on the  
official **MIMU P-code system** (Place Codes).

This module provides structured State/Region → District (including Self-Administered Zones) → Township → Ward/Village Tract data for accurate geographic referencing.

---

## Features

- **States / Regions** — pre-loaded administrative divisions
- **District-Level Units** — includes:
  - Districts  
  - Self-Administered Zones (SAZ)  
  - Self-Administered Divisions (SAD)
- **Townships**
- **Wards / Village Tracts**
- **Official MIMU P-codes** — unique geographic identifiers for each unit
- **Hierarchical Cascade Logic**
  - Ward selection auto-fills township, district, state
  - Township filters wards
  - District filters townships
- **Myanmar-Only Visibility** — fields appear when country is set to Myanmar

---

## Administrative Structure

State / Region  
→ District / SAZ / SAD  
→ Township  
→ Town
→ Ward / Village Tract  

Town level (where applicable) is supported optionally.

---

## P-code Structure

| Level | Example | Description |
|-------|----------|------------|
| Country | MMR | Myanmar ISO-3 |
| District | MMR017D006 | District-level administrative code |
| Ward / VT | MMR017024040 | Unique place code |

P-codes are geographic identifiers used for mapping, census, and data management —  
they are **not postal delivery codes**.

---

## Installation

1. Place `l10n_mm_pcode` in your Odoo addons path
2. Update apps list: **Apps → Update Apps List**
3. Search for **"Myanmar Administrative Localization"** and install

No additional configuration required.

---

## Menu Access

Contacts → Configuration → Myanmar Administrative Units

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Depends on:
  - `base`
  - `contacts`

---

## Data Source

Myanmar Information Management Unit (MIMU)  
Official Myanmar Place Codes (P-codes)

https://themimu.info/mm/place-codes

---

## Purpose

This module is intended for:

- Structured administrative referencing
- Reporting by geographic hierarchy
- GIS integration
- Data standardization across Myanmar locations

It does not replace Myanmar Post 7-digit postal code modules.

---

## License

LGPL-3