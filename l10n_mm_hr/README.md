# Myanmar HR Localization (l10n_mm_hr)

Odoo module that extends HR employee records with Myanmar administrative hierarchy fields for private addresses using the official **MIMU P-code system**.

Provides structured employee address management with State/Region → District → Township → Town → Ward data.

---

## Features

- **HR Integration**
  - Myanmar address fields in Private Information tab
  - Employee private address support
  - Country-based field visibility
  - Seamless HR workflow integration

- **Private Address Fields**
  - Ward / Village Tract
  - Town (optional)
  - Township
  - District
  - P-Code
  - State / Region (auto-filled)

- **Smart Field Behavior**
  - Auto-fill from P-code entry
  - Auto-fill from ward selection
  - Cascading updates on level changes
  - Dynamic field visibility (Myanmar only)
  - Validation against MIMU database

- **Security**
  - Respects HR access rights
  - Fields restricted to `hr.group_hr_user`
  - Private information protection

---

## Use Cases

- **HR Management**: Accurate employee home addresses
- **Payroll**: Location-based allowances
- **Emergency Contact**: Detailed address information
- **Compliance**: Government reporting requirements
- **Analytics**: Employee geographic distribution

---

## Usage

### Employee Form

1. Navigate to **Employees → Employees**
2. Open or create an employee record
3. Go to **Private Information** tab
4. Set **Private Country** to "Myanmar"
5. Myanmar address fields appear automatically

### P-code Entry Method

1. Enter P-code in the P-Code field (e.g., `MMR017024040`)
2. All private address fields populate automatically:
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

1. Install `l10n_mm_pcode` module first (required dependency)
2. Ensure `hr` module is installed (Odoo standard)

### Install Steps

1. Place `l10n_mm_hr` in your Odoo addons path
2. Update apps list: **Apps → Update Apps List**
3. Search for **"Myanmar HR Localization"**
4. Click **Install**

No additional configuration required.

---

## Technical Details

### Models Extended

- `hr.employee` - Employee model

### New Fields

| Field | Type | Description |
|-------|------|-------------|
| `private_l10n_mm_district_id` | Many2one | District reference (computed) |
| `private_l10n_mm_township_id` | Many2one | Township reference (computed) |
| `private_l10n_mm_town_id` | Many2one | Town reference (optional) |
| `private_l10n_mm_ward_id` | Many2one | Ward reference |
| `private_l10n_mm_pcode` | Char | MIMU P-code |
| `private_l10n_mm_is_myanmar` | Boolean | Myanmar country check (computed) |

**Note**: All fields prefixed with `private_` to align with Odoo HR conventions.

### Key Methods

- `_compute_private_l10n_mm_is_myanmar()` - Country detection
- `_compute_private_l10n_mm_district_id()` - Auto-fill district from township
- `_compute_private_l10n_mm_township_id()` - Auto-fill township from ward
- `_onchange_private_l10n_mm_pcode()` - P-code validation and auto-fill
- `_onchange_private_l10n_mm_ward_id()` - Ward cascade logic
- `_onchange_private_l10n_mm_township_id()` - Township cascade logic
- `_onchange_private_l10n_mm_district_id()` - District cascade logic
- `_onchange_private_state_id()` - State change handling
- `_onchange_private_country_id()` - Country change handling

### View Modifications

- Inherits `hr.view_employee_form`
- Adds Myanmar fields before private_city field
- Hides private_city/private_zip when Myanmar is selected
- Uses address-specific CSS classes
- Respects HR security groups

### Security

All Myanmar fields inherit HR module security:
- Read/Write: `hr.group_hr_user`
- Follows Odoo HR access control patterns

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Dependencies:
  - `hr` (Odoo standard)
  - `l10n_mm_pcode` (required)

---

## Data Source

Myanmar Information Management Unit (MIMU)  
Official Myanmar Place Codes (P-codes)

https://themimu.info/mm/place-codes

---

## Reporting

Myanmar private address fields are available in:
- Employee reports
- HR analytics
- Custom filters and grouping
- Export functionality
- Payroll integration

---

## Privacy Considerations

- Private address data follows Odoo HR security model
- Access restricted to HR users
- Complies with data protection requirements
- Audit trail via Odoo standard logging

---

## Author

Zenonia

## License

LGPL-3

---

## Support

GitHub: https://github.com/Zenonia-9/Myanmar-Administrative-Localization
