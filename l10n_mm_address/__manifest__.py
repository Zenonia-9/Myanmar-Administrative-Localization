# -*- coding: utf-8 -*-
{
    'name': 'Myanmar Address Localization',
    'version': '19.0.0.2',
    'category': 'Localization/Contacts',
    'summary': 'Complete Myanmar address hierarchy with MIMU P-code integration for States, Districts, Townships, Towns, Wards and Village Tracts.',
    'description': """
Myanmar Address Localization
=============================

This module provides the complete Myanmar administrative address hierarchy
with full MIMU P-code support for precise address management in Odoo.

Main Features
-------------
* 18 States / Regions
* 86 Districts (including Self-Administered Zones and Divisions)
* 358 Townships with postal codes, latitude, and longitude coordinates
* 800+ Towns linked to Townships
* 16,000+ Wards and Village Tracts with full MIMU P-code support
* 900+ Postal Codes linked to Townships
* Map view integration using township-level coordinates
* Myanmar language name support (name_mm fields)
* Auto-fill address from P-Code or Ward selection
* Hierarchical cascading dropdowns in contact forms

Address Hierarchy
-----------------
State/Region → District → Township → Town → Ward / Village Tract

District Types
--------------
* District - Regular administrative district
* SAZ - Self-Administered Zone
* SAD - Self-Administered Division

Ward Types
----------
* Ward - Urban administrative ward
* Village Tract - Rural administrative division

Company
-------
Automated Resources Integrator Co., Ltd (ARI)
Repository: https://github.com/Zenonia-9/Myanmar-Administrative-Localization
""",
    'author': 'Thein Htoo Aung',
    'company': 'Automated Resources Integrator Co., Ltd',
    'maintainer': 'Automated Resources Integrator Co., Ltd',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Country Data
        'data/res_country_data.xml',

        # Master Data
        'data/res.country.state.csv',
        'data/res.district.csv',
        'data/res.township.csv',
        'data/res.town.csv',
        'data/res.zip.csv',
        'data/res.ward.csv',

        # Views
        'views/res_country_views.xml',
        'views/res_district_views.xml',
        'views/res_township_views.xml',
        'views/res_town_views.xml',
        'views/res_ward_views.xml',
        'views/res_zip_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
} # type: ignore