# Myanmar Address Localization Module (l10n_mm_address)

## Overview
This Odoo 18 module provides complete Myanmar address hierarchy support with MIMU P-code integration for precise address management.

## Features
- **18 States/Regions** - Myanmar administrative divisions
- **86 Districts** - Linked to States/Regions
- **358 Townships** - With postal codes (5-digit), latitude, and longitude coordinates
- **Towns** - Linked to Townships
- **Wards and Village Tracts** - Single model with type differentiation
  - Ward: 4-digit P-code suffix
  - Village Tract: Last 3 digits P-code suffix
  - Full MIMU P-code support (15-character hierarchical code)
- **Postal Codes** - 5-digit format linked to Townships
- **Map View Integration** - Using township-level coordinates (latitude/longitude centroid)

## Address Hierarchy
```
State/Region (res.country.state)
  └── District (res.district)
      └── Township (res.township)
          ├── Town (res.town)
          │   └── Ward/Village Tract (res.ward)
          └── Ward/Village Tract (res.ward)
```

## P-Code Structure
MIMU P-codes are hierarchical 15-character codes:
- **MMR** - Country code (Myanmar)
- **001-018** - State/Region code
- **D001-D333** - District code (or S/SAD for special zones)
- **001-358** - Township code
- **0001-9999** - Ward/Village Tract code

Example: `MMR017024040` = Myanmar → Ayeyarwady (017) → Pyapon District (024) → Ward/Village Tract (040)

## Installation
1. Copy the `l10n_mm_address` folder to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Myanmar - Address Localization" module

## Data Import
The module automatically imports:
- 18 States/Regions
- 86 Districts (including Self-Administered Zones and Divisions)
- 358 Townships (with postal codes and coordinates)
- 800+ Towns
- 16,000+ Wards and Village Tracts
- 900+ Postal Codes

## Usage
After installation, you can:
- Browse Myanmar addresses via **Contacts > Configuration > Myanmar Localization**
- Filter hierarchically: State → District → Township → Town → Ward
- Use in contact forms for precise address selection
- Auto-fill address using P-Code (searches by ward P-code)
- Auto-fill address using Ward selection
- Select postal codes linked to townships
- View contacts on map using township-level coordinates

## Address Fields in Contacts
When country is set to Myanmar, the following fields appear:
- **District** - Filtered by selected State
- **Township** - Filtered by selected District
- **Town** - Filtered by selected Township
- **Ward** - Filtered by selected Town or Township
- **P-Code** - Auto-fills from ward selection or manual entry
- **Postal Code** - Filtered by selected Township
- **Myanmar Address** - Computed full address display

## Map View
The map view displays partner locations using **township-level accuracy**. Coordinates (latitude/longitude) are stored at the township level and represent the centroid of villages within each township. This provides accurate regional positioning while maintaining data simplicity.

## Technical Details
- **Models**: 
  - `res.district` - Districts/SAZ/SAD
  - `res.township` - Townships with coordinates
  - `res.town` - Towns
  - `res.ward` - Wards and Village Tracts
  - `res.zip` - Post codes
  - `res.country` - Enhanced with `enforce_townships` field
- **CSV Data**: All data loaded via CSV files in `data/` folder
- **Security**: Read access for all users (base.group_user), write access for partner managers
- **Code Preservation**: All codes maintain leading zeros (ward 4-digit, postal 5-digit)
- **Map Coordinates**: Township-level latitude/longitude (centroid-based)
- **Postal Code Format**: 5-digit format

## District Types
- **District** - Regular administrative district
- **SAZ** - Self-Administered Zone
- **SAD** - Self-Administered Division

## Ward Types
- **Ward** - Urban administrative ward
- **Village Tract** - Rural administrative division

## Future Enhancements
- Myanmar language name support (fields ready: `name_mm`)
- Village-level coordinate precision
- Enhanced map clustering for dense areas
- Enforcement of township selection at country level

## License
LGPL-3

## Author
Zenonia

## Repository
https://github.com/Zenonia-9/Myanmar-Administrative-Localization
