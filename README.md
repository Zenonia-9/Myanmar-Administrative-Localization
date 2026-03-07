# Myanmar Administrative Localization Addons

Complete suite of Odoo 18 modules for Myanmar administrative hierarchy integration using official **MIMU P-code system**.

---

## Modules

### 1. l10n_mm_pcode (Base Module)
Core module providing Myanmar administrative hierarchy for contacts.

**Features:**
- Complete MIMU P-code database (States, Districts, Townships, Towns, Wards)
- Partner address integration
- Cascading field selection
- P-code auto-fill

### 2. l10n_mm_crm
Extends CRM leads/opportunities with Myanmar address fields.

**Features:**
- Myanmar fields in Extra Information tab
- Lead/opportunity address management
- Auto-fill from P-code or ward selection

### 3. l10n_mm_hr
Adds Myanmar address fields to employee private addresses.

**Features:**
- Employee private address localization
- Private Information tab integration
- Full P-code support

---

## Installation

1. Copy all modules to your Odoo addons directory
2. Update apps list: **Apps → Update Apps List**
3. Install modules in order:
   - `l10n_mm_pcode` (required base)
   - `l10n_mm_crm` (optional)
   - `l10n_mm_hr` (optional)

---

## Data Source

Myanmar Information Management Unit (MIMU)  
https://themimu.info/mm/place-codes

---

## Requirements

- Odoo 18.0 Community or Enterprise
- Python 3.10+

---

## Author

Zenonia

## License

LGPL-3

---

## Support

GitHub: https://github.com/Zenonia-9/Myanmar-Administrative-Localization
