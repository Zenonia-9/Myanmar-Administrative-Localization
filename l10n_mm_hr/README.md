# Myanmar HR Localization

## Description

This module extends Odoo HR to support Myanmar address fields for employee private addresses using the Myanmar MIMU P-code system.

## Features

- Myanmar-specific address fields for employee private addresses:
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

- `hr` - Odoo HR module
- `l10n_mm_pcode` - Myanmar P-code base module

## Installation

1. Ensure `l10n_mm_pcode` module is installed
2. Install this module from Apps menu

## Usage

1. Go to Employees
2. Open an employee form
3. In the Private Information tab, set Private Country to "Myanmar"
4. Myanmar address fields will appear
5. Enter P-Code or select Ward to auto-fill address fields

## Author

Zenonia

## License

LGPL-3
