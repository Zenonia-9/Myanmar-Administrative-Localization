# Myanmar CRM Address Localization (l10n_mm_address_crm)

Odoo module that extends CRM leads and opportunities with Myanmar administrative hierarchy fields using the official **MIMU P-code system**.

Integrates with `l10n_mm_address` module to provide structured address management for sales pipeline with State/Region → District → Township → Town → Ward → Zip Code data.

---

## Features

- **CRM Integration**
  - Myanmar address fields in Extra Information tab
  - Lead and opportunity address support
  - Country-based field visibility
  - Seamless CRM workflow integration

- **Address Fields**
  - Ward / Village Tract
  - Town (optional)
  - Township
  - District
  - P-Code
  - Zip Code
  - State / Region (auto-filled)

- **Smart Field Behavior**
  - Auto-fill from P-code entry
  - Auto-fill from ward selection
  - Cascading updates on level changes
  - Dynamic field visibility (Myanmar only)
  - Validation against MIMU database

- **User Experience**
  - Replaces city/zip with Myanmar fields
  - Dropdown selection with hierarchy
  - P-code quick entry
  - Error handling for invalid codes

---

## Use Cases

- **Sales Teams**: Accurate lead location tracking
- **Territory Management**: Geographic lead assignment
- **Market Analysis**: Regional opportunity reporting
- **Customer Profiling**: Detailed address information

---

## Usage

### Lead/Opportunity Form

1. Navigate to **CRM → Leads** or **CRM → Pipeline**
2. Open or create a lead/opportunity
3. Go to **Extra Information** tab
4. Set **Country** to "Myanmar"
5. Myanmar address fields appear automatically

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

---

## Installation

### Prerequisites

1. Install `l10n_mm_address` module first (required dependency)
2. Ensure `crm` module is installed (Odoo standard)

### Install Steps

1. Place `l10n_mm_address_crm` in your Odoo addons path
2. Update apps list: **Apps → Update Apps List**
3. Search for **"Myanmar CRM Address Localization"**
4. Click **Install**

No additional configuration required.

---

## Technical Details

### Models Extended

- `crm.lead` - Leads and opportunities model

### New Fields

| Field | Type | Description |
|-------|------|-------------|
| `l10n_mm_district_id` | Many2one | District reference (computed) |
| `l10n_mm_township_id` | Many2one | Township reference (computed) |
| `l10n_mm_town_id` | Many2one | Town reference (optional) |
| `l10n_mm_ward_id` | Many2one | Ward reference |
| `l10n_mm_ward_ids` | Many2many | Ward dropdown filter (computed) |
| `l10n_mm_zip_id` | Many2one | Zip code reference |
| `l10n_mm_pcode` | Char | MIMU P-code |
| `l10n_mm_postalcode` | Char | Postal code (7 digits) |
| `l10n_mm_is_myanmar` | Boolean | Myanmar country check (computed) |

### Key Methods

- `_compute_l10n_mm_is_myanmar()` - Country detection
- `_compute_l10n_mm_district_id()` - Auto-fill district from township
- `_compute_l10n_mm_township_id()` - Auto-fill township from ward
- `_compute_ward_ids()` - Dynamic ward filtering
- `_onchange_l10n_mm_pcode()` - P-code validation and auto-fill
- `_onchange_l10n_mm_ward_id()` - Ward cascade logic
- `_onchange_l10n_mm_town_id()` - Town cascade logic
- `_onchange_l10n_mm_township_id()` - Township cascade logic
- `_onchange_l10n_mm_district_id()` - District cascade logic
- `_onchange_state_id()` - State change handling
- `_onchange_country_id()` - Country change handling

### View Modifications

- Inherits `crm.crm_lead_view_form`
- Adds Myanmar fields before city field
- Hides city/zip when Myanmar is selected
- Uses address-specific CSS classes

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Dependencies:
  - `crm` (Odoo standard)
  - `l10n_mm_address` (required)

---

## Data Source

Myanmar Information Management Unit (MIMU)  
Official Myanmar Place Codes (P-codes)

https://themimu.info/mm/place-codes

---

## Reporting

Myanmar address fields are available in:
- Lead/opportunity reports
- Pipeline analysis
- Custom filters and grouping
- Export functionality

---

## Author

Zenonia

## License

LGPL-3

---

## Support

GitHub: https://github.com/Zenonia-9/Myanmar-Administrative-Localization
