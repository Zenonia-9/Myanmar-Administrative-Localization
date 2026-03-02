# Myanmar Administrative Localization (l10n_mm_pcode)

Odoo module that adds Myanmar administrative hierarchy fields to contacts based on the official **MIMU P-code system** (Place Codes).

Provides structured State/Region → District → Township → Town → Ward/Village Tract data for accurate geographic referencing.

---

## Features

- **Complete Administrative Hierarchy**
  - States / Regions (18 divisions)
  - Districts (88 units including SAZ/SAD)
  - Townships (358 townships)
  - Towns (536 urban centers)
  - Wards / Village Tracts (65,000+ units)

- **Partner Integration**
  - Myanmar address fields in contact forms
  - Cascading selection (ward → township → district → state)
  - P-code auto-fill functionality
  - Kanban view with Myanmar address display
  - Child contact address support

- **Smart Field Behavior**
  - Auto-fill upper levels from lower selections
  - Dynamic domain filtering
  - Myanmar-only visibility
  - Integrated address formatting

- **Official MIMU P-codes**
  - Unique geographic identifiers
  - Hierarchical structure
  - Search by name or P-code

---

## Administrative Structure

```
State / Region  
└── District / SAZ / SAD  
    └── Township  
        └── Town (optional)
            └── Ward / Village Tract
```

---

## P-code Structure

| Level | Example | Description |
|-------|----------|-------------|
| Country | MMR | Myanmar ISO-3 |
| State | MMR017 | Ayeyarwady Region |
| District | MMR017D006 | Pyapon District |
| Township | MMR017024 | Bogale Township |
| Ward | MMR017024040 | Specific ward/village tract |

P-codes are geographic identifiers for mapping, census, and data management — not postal codes.

---

## Usage

### Contact Form
1. Set country to Myanmar
2. Myanmar address fields appear automatically
3. Select ward/township or enter P-code
4. Upper levels auto-fill

### P-code Entry
- Enter P-code in contact form
- All address fields populate automatically
- Validates against official MIMU database

### Search
- Search wards by name, P-code, township, or district
- Hierarchical display in dropdowns

---

## Installation

1. Place `l10n_mm_pcode` in your Odoo addons path
2. Update apps list: **Apps → Update Apps List**
3. Search for **"Myanmar Administrative Localization"** and install

No additional configuration required.

---

## Menu Access

**Contacts → Configuration → Myanmar Localization**
- Districts
- Townships
- Towns
- Wards

---

## Technical Details

### Models
- `res.district` - District/SAZ/SAD management
- `res.township` - Township records
- `res.town` - Town/urban center records
- `res.ward` - Ward/village tract records
- `res.partner` - Extended with Myanmar fields

### Key Features
- SQL constraints for unique codes
- Computed fields with cascade logic
- Custom name search implementation
- Integrated address formatting

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Dependencies: `base`, `contacts`

---

## Data Source

Myanmar Information Management Unit (MIMU)  
Official Myanmar Place Codes (P-codes)

https://themimu.info/mm/place-codes

---

## License

LGPL-3