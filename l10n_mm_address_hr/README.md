# Myanmar HR Address Localization (l10n_mm_address_hr)

Odoo module that extends HR employee records with Myanmar administrative hierarchy fields for private addresses using the official **MIMU P-code system**.

Integrates with `l10n_mm_address` module to provide structured employee address management with State/Region → District → Township → Town → Ward → Zip Code data.

---

## Features

- **HR Integration**
  - Myanmar address fields in Private Information tab
  - Employee private address support
  - Country-based field visibility
  - Seamless HR workflow integration

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

- **Security**
  - Respects HR access rights
  - Fields restricted to `hr.group_hr_user`
  - Private information protection

---

## Installation

### Prerequisites

1. Install `l10n_mm_address` module first (required dependency)
2. Ensure `hr` module is installed (Odoo standard)

### Install Steps

1. Place `l10n_mm_address_hr` in your Odoo addons path
2. Update apps list: **Apps → Update Apps List**
3. Search for **"Myanmar HR Address Localization"**
4. Click **Install**

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
2. All private address fields populate automatically

### Manual Selection Method

1. Select **Ward** from dropdown
2. Upper levels auto-fill (Township, District, State)
3. Or select **Township** first, then choose Ward

---

## Requirements

- Odoo 18.0+
- Dependencies:
  - `hr` (Odoo standard)
  - `l10n_mm_address` (required)

---

## Author

Zenonia

## License

LGPL-3
