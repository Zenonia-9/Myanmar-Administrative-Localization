# Myanmar CRM Address Localization (l10n_mm_address_crm)

## Overview

**Myanmar CRM Address Localization** is an Odoo 18 module developed by **Zenonia** that extends CRM leads and opportunities with the complete Myanmar administrative address hierarchy, powered by **MIMU P-code** data from `l10n_mm_address`.

Myanmar address fields are added to the **Extra Information** tab of lead and opportunity forms with cascading dropdowns, auto-fill from P-Code, and dynamic visibility based on country selection.

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

## Features

* **Myanmar address fields** — Full hierarchy in the Extra Information tab of leads and opportunities
* **Cascading dropdowns** — State → District → Township → Town → Ward
* **Auto-fill from P-Code** — Enter a MIMU P-code to populate the full address
* **Auto-fill from Ward** — Selecting a Ward fills Township, District, State, and Country
* **Dynamic visibility** — Myanmar address fields appear only when Country is set to Myanmar
* **Myanmar language names** — Inherits `name_mm` display from `l10n_mm_address`

---

## Technical Details

### Address Fields on `crm.lead`

| Field | Description |
| --- | --- |
| `l10n_mm_district_id` | District, filtered by State |
| `l10n_mm_township_id` | Township, filtered by District |
| `l10n_mm_town_id` | Town, filtered by Township |
| `l10n_mm_ward_id` | Ward, filtered by Town or Township |
| `l10n_mm_pcode` | MIMU P-Code for auto-fill |
| `l10n_mm_zip_id` | Postal code, filtered by Township |

### Security

| Group | Permissions |
| --- | --- |
| `base.group_user` | Read |
| `base.group_partner_manager` | Read, Write, Create, Delete |

---

## Installation

### 1. Copy Module

```bash
cp -r l10n_mm_address_crm /path/to/odoo/addons/
```

### 2. Update Apps List

In Odoo, go to **Apps → Update Apps List**.

### 3. Install

Search for `Myanmar CRM Address Localization` and click **Install**.

> **Note:** `l10n_mm_address` must be installed first as it is a required dependency.

---

## Usage

After installation:

* Navigate to **CRM → Leads** or **CRM → Pipeline** and open any lead or opportunity
* Go to the **Extra Information** tab
* Set **Country** to `Myanmar` to reveal the Myanmar address fields
* Use the **P-Code** field to auto-fill the entire address hierarchy, or select fields manually starting from Ward

---

# Requirements

* Odoo 18
* Python 3.10+
* Docker (optional)
* PostgreSQL

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
