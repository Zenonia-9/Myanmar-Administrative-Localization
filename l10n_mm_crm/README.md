# Myanmar CRM Localization

## Description

This module extends Odoo CRM to support Myanmar address fields for leads/opportunities using the Myanmar MIMU P-code system.

## Features

- Myanmar-specific address fields in Extra Information tab:
  - Ward
  - Town
  - Township
  - District
  - P-Code

- Auto-fill address from P-Code entry
- Auto-fill address from Ward selection
- Cascade updates when changing administrative levels
- Automatic show/hide based on country selection (Myanmar)

## Dependencies

- `crm` - Odoo CRM module
- `l10n_mm_pcode` - Myanmar P-code base module

## Installation

1. Ensure `l10n_mm_pcode` module is installed
2. Install this module from Apps menu

## Usage

1. Go to CRM → Leads or Opportunities
2. Open a lead/opportunity form
3. In the Extra Information tab, set Country to "Myanmar"
4. Myanmar address fields will appear
5. Enter P-Code or select Ward to auto-fill address fields

## Author

Zenonia

## License

LGPL-3
