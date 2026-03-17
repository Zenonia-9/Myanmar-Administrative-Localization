# Myanmar Administrative Localization Addons

Complete suite of Odoo 19 modules for Myanmar administrative address hierarchy integration using the official **MIMU P-code system**.

---

## Modules

### 1. l10n_mm_address (Base Module)

Core module providing the complete Myanmar administrative address hierarchy for Odoo contacts.

**Features:**
* 18 States/Regions — Myanmar administrative divisions
* 86 Districts — Including Self-Administered Zones (SAZ) and Divisions (SAD)
* 358 Townships — With 5-digit postal codes, latitude, and longitude coordinates
* 800+ Towns — Linked to Townships
* 16,000+ Wards and Village Tracts — With full MIMU P-code support
* 900+ Postal Codes — 5-digit format linked to Townships
* Cascading dropdowns — State → District → Township → Town → Ward
* Auto-fill from P-Code or Ward selection
* Myanmar language names (`name_mm` fields)
* Map view using township-level coordinates (only on Enterprise)
* Computed full address field on `res.partner`

---

### 2. l10n_mm_address_crm

Extends CRM leads and opportunities with Myanmar address fields.

**Depends on:** `crm`, `l10n_mm_address`

**Features:**
* Myanmar address fields in the Extra Information tab of leads and opportunities
* Cascading dropdowns — State → District → Township → Town → Ward
* Auto-fill from P-Code or Ward selection
* Dynamic field visibility (Myanmar country only)

---

### 3. l10n_mm_address_hr

Extends employee records with Myanmar address fields for private addresses.

**Depends on:** `hr`, `l10n_mm_address`

**Features:**
* Myanmar address fields in the Private Information tab of employee records
* Cascading dropdowns — State → District → Township → Town → Ward
* Auto-fill from P-Code or Ward selection
* Dynamic field visibility (Myanmar country only)
* Fields restricted to `hr.group_hr_user`

---

## Address Hierarchy

```
State/Region (res.country.state)
  └── District (res.district)
      └── Township (res.township)
          ├── Town (res.town)
          │   └── Ward / Village Tract (res.ward)
          └── Ward / Village Tract (res.ward)
```

---

## Installation

1. Copy all modules to your Odoo addons directory
2. Update apps list: **Apps → Update Apps List**
3. Install modules in order:
   - `l10n_mm_address` — required base, install first
   - `l10n_mm_address_crm` — optional, requires `crm`
   - `l10n_mm_address_hr` — optional, requires `hr`

---

## Data Sources

* **Myanmar Information Management Unit (MIMU)** — Administrative hierarchy and P-code data
  [https://themimu.info/mm/place-codes](https://themimu.info/mm/place-codes)

* **Myanmar Post** — Official postal code data
  [https://myanmarpost.com.mm/postcode](https://myanmarpost.com.mm/postcode)

* **Dr. Nyein Chan's P-Code Database** — Extended P-code reference
  [https://pcode.drnyeinchan.com/](https://pcode.drnyeinchan.com/)

---

## Requirements

* Odoo 19.0 Community or Enterprise
* Python 3.10+

---

## Developer

**Author:**
Thein Htoo Aung

**Company:**
Automated Resources Integrator Co., Ltd

Repository: [https://github.com/Zenonia-9/Myanmar-Administrative-Localization](https://github.com/Zenonia-9/Myanmar-Administrative-Localization)

---

## License

LGPL-3
