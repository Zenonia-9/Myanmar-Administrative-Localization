# -*- coding: utf-8 -*-
{
    'name': 'Myanmar Address Localization',
    'version': '18.0.2.5',
    'category': 'Localization',
    'summary': 'Myanmar address hierarchy (State/Region, District, Township, Town, Ward/Village Tract)',
    'description': """
Myanmar Address Localization
=============================

This module provides the Myanmar administrative address hierarchy:

- States / Regions
- Districts
- Townships (with postal codes, latitude, longitude)
- Towns
- Wards and Village Tracts (with P-Code support)
""",
    'author': 'Zenonia',
    'website': 'https://github.com/Zenonia-9/Myanmar-Administrative-Localization',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',

        'data/res_country_data.xml',

        'data/res.country.state.csv',
        'data/res.district.csv',
        'data/res.township.csv',
        'data/res.town.csv',
        'data/res.zip.csv',
        'data/res.ward.csv',

        'views/res_district_views.xml',
        'views/res_township_views.xml',
        'views/res_town_views.xml',
        'views/res_ward_views.xml',
        'views/res_zip_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}