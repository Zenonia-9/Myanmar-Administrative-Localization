# Myanmar Address Localization Module (l10n_mm_address)

## Overview
This Odoo 18 module provides complete Myanmar address hierarchy support with Pcode integration.

## Features
- **18 States/Regions** (Myanmar administrative divisions)
- **Districts** linked to States/Regions
- **Townships** with postal codes (7-digit with leading zeros), latitude, and longitude (centroid of villages)
- **Towns** linked to Townships
- **Wards and Village Tracts** in a single model with type differentiation
  - Ward: 4-digit code with leading zeros
  - Village Tract: Last 3 digits code
  - Full Pcode support (ward_pcode field)

## Address Hierarchy
```
State/Region (res.country.state)
  └── District (res.district)
      └── Township (res.township)
          ├── Town (res.town)
          │   └── Ward/Village Tract (res.ward)
          └── Ward/Village Tract (res.ward)
```

## Installation
1. Copy the `l10n_mm_address` folder to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Myanmar - Address Localization" module

## Data Import
The module automatically imports:
- 18 States/Regions
- 80+ Districts
- 330+ Townships (with postal codes, coordinates)
- 800+ Towns
- 16,000+ Wards and Village Tracts

## Usage
After installation, you can:
- Browse Myanmar addresses via Contacts > Configuration menu
- Filter data by State → District → Township → Town → Ward
- Use in contact forms for precise address selection
- Access latitude/longitude data for townships

## Technical Details
- **Models**: res.district, res.township, res.town, res.ward
- **CSV Data**: All data loaded via CSV files in data/ folder
- **Security**: Read access for all users (base.group_user)
- **Code Preservation**: All codes maintain leading zeros (ward 4-digit, postal 7-digit)

## Future Enhancements
- Myanmar language name support (fields ready: name_mm)
- Integration with res.partner for address selection
- Map view integration using township coordinates

## License
LGPL-3

## Author
Your Company
