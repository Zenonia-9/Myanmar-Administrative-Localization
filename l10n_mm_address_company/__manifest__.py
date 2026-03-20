# -*- coding: utf-8 -*-
{
    'name': 'Myanmar Company Address Localization',
    'version': '19.0.1.0',
    'category': 'Localization/Contacts',
    'summary': 'Myanmar address hierarchy fields for company settings with MIMU P-code integration.',
    'description': """
Myanmar Company Address Localization
======================================

This module extends Odoo company settings with the complete Myanmar
administrative address hierarchy, powered by MIMU P-code data from l10n_mm_address.

Main Features
-------------
* Myanmar address fields in the company form (Settings > Companies)
* Cascading dropdowns: State/Region → District → Township → Town → Ward
* Auto-fill address from P-Code or Ward selection
* Dynamic field visibility (Myanmar country only)
* Inherits all MIMU P-code data from l10n_mm_address

Address Hierarchy
-----------------
State/Region → District → Township → Town → Ward / Village Tract

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
        'l10n_mm_address',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        'views/res_company_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
} # type: ignore
