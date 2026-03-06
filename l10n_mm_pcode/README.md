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

## Use Cases

- **Contact Management**: Accurate customer/supplier addresses
- **Sales & Distribution**: Territory-based customer segmentation
- **Logistics**: Delivery route planning and optimization
- **Reporting**: Geographic analysis and regional statistics
- **Compliance**: Standardized address data for government reporting

---

## Usage

### Contact Form

1. Navigate to **Contacts → Contacts**
2. Open or create a contact
3. Set **Country** to "Myanmar"
4. Myanmar address fields appear automatically

### P-code Entry Method

1. Enter P-code in the P-Code field (e.g., `MMR017024040`)
2. All address fields populate automatically:
   - Ward
   - Town (if applicable)
   - Township
   - District
   - State/Region
   - Country

### Manual Selection Method

1. Select **Ward** from dropdown
2. Upper levels auto-fill (Township, District, State)
3. Or select **Township** first, then choose Ward
4. P-code updates automatically

### Field Behavior

- **Country Change**: Clears all Myanmar fields if not Myanmar
- **State Change**: Clears lower levels if state changes
- **District Change**: Clears township, town, ward
- **Township Change**: Clears town and ward
- **Ward Change**: Updates all upper levels and P-code

### Search Functionality

- Search wards by name, P-code, township, or district
- Hierarchical display in dropdowns
- Fast lookup with indexed P-codes

---

## Installation

### Prerequisites

- Odoo 18.0 Community or Enterprise
- `base` and `contacts` modules (Odoo standard)

### Install Steps

1. Place `l10n_mm_pcode` in your Odoo addons path
2. Restart Odoo server (if needed)
3. Update apps list: **Apps → Update Apps List**
4. Search for **"Myanmar Administrative Localization"**
5. Click **Install**

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

#### res.district
- District/SAZ/SAD management
- Fields: `name`, `code`, `state_id`, `district_type`
- SQL constraint: Unique district code

#### res.township
- Township records
- Fields: `name`, `code`, `district_id`
- SQL constraint: Unique township code

#### res.town
- Town/urban center records
- Fields: `name`, `code`, `township_id`
- SQL constraint: Unique town code

#### res.ward
- Ward/village tract records
- Fields: `name`, `p_code`, `township_id`, `town_id`, `ward_type`
- SQL constraint: Unique P-code
- Custom display name with hierarchy
- Advanced name search (name, P-code, township, district)

#### res.partner (Extended)
- Myanmar address fields
- Fields: `l10n_mm_district_id`, `l10n_mm_township_id`, `l10n_mm_town_id`, `l10n_mm_ward_id`, `l10n_mm_pcode`, `l10n_mm_is_myanmar`
- Related fields for address formatting

### New Fields

| Field | Type | Description |
|-------|------|-------------|
| `l10n_mm_district_id` | Many2one | District reference (computed) |
| `l10n_mm_township_id` | Many2one | Township reference (computed) |
| `l10n_mm_town_id` | Many2one | Town reference (optional) |
| `l10n_mm_ward_id` | Many2one | Ward reference |
| `l10n_mm_pcode` | Char | MIMU P-code |
| `l10n_mm_is_myanmar` | Boolean | Myanmar country check (computed) |

### Key Methods

- `_compute_l10n_mm_is_myanmar()` - Country detection
- `_compute_l10n_mm_district_id()` - Auto-fill district from township
- `_compute_l10n_mm_township_id()` - Auto-fill township from ward
- `_onchange_l10n_mm_pcode()` - P-code validation and auto-fill
- `_onchange_l10n_mm_ward_id()` - Ward cascade logic
- `_onchange_l10n_mm_township_id()` - Township cascade logic
- `_onchange_l10n_mm_district_id()` - District cascade logic
- `_onchange_state_id()` - State change handling
- `_onchange_country_id()` - Country change handling
- `_address_fields()` - Include Myanmar fields in address
- `_formatting_address_fields()` - Address formatting integration

### View Modifications

- Inherits `base.view_partner_form`
- Adds Myanmar fields before city field
- Hides city/zip when Myanmar is selected
- Uses address-specific CSS classes
- Kanban view integration
- Child contact address support

### Security

- Read access: All users (`base.group_user`)
- Write/Create/Delete: Contact managers (`base.group_partner_manager`)

### Key Features

- SQL constraints for unique codes
- Computed fields with cascade logic
- Custom name search implementation
- Integrated address formatting
- Dynamic domain filtering
- Hierarchical data structure

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Python 3.10+
- Dependencies:
  - `base` (Odoo standard)
  - `contacts` (Odoo standard)

---

## Data Source

Myanmar Information Management Unit (MIMU)  
Official Myanmar Place Codes (P-codes)

https://themimu.info/mm/place-codes

---

## Reporting

Myanmar address fields are available in:
- Contact reports
- Sales analysis
- Custom filters and grouping
- Export functionality
- Geographic segmentation

---

## Related Modules

- **l10n_mm_crm**: Myanmar address fields for CRM leads/opportunities
- **l10n_mm_hr**: Myanmar address fields for employee private addresses

---

## Author

Zenonia

## License

LGPL-3

---

## Support

GitHub: https://github.com/Zenonia-9/Myanmar-Administrative-Localization