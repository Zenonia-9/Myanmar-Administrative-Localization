# -*- coding: utf-8 -*-
{
    'name': "Myanmar Administrative Localization",
    'version': "1.0.0",
    'summary': "Adds Myanmar administrative hierarchy (MIMU P-codes) for contacts",
    'description': """
Myanmar Administrative Localization (l10n_mm_pcode)

Provides structured State/Region → District/SAZ/SAD → Township → Ward/Village Tract
hierarchy using official MIMU P-codes.

- Automatic cascade selection for ward → township → district → state
- Optional town field for urban wards
- Myanmar-only visibility
- Supports reporting and data standardization
""",
    'category': 'Localization',
    'author': "Your Name",
    'website': "https://github.com/Zenonia-9/Myanmar-Administrative-Localization",
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Data
        'data/res.country.state.csv',
        'data/res.district.csv',
        'data/res.township.csv',
        'data/res.town.csv',
        'data/res.ward.csv',
        # Views
        'views/res_district_views.xml',
        'views/res_township_views.xml',
        'views/res_town_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}  # type: ignore
