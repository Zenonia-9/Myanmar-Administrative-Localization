# -*- coding: utf-8 -*-
{
    'name': 'Myanmar HR Address Localization',
    'version': '18.0.1.5',
    'category': 'Human Resources/Localization',
    'summary': 'Myanmar address hierarchy fields for employee private addresses with MIMU P-code integration.',
    'description': """
Myanmar HR Address Localization
================================

This module extends Odoo HR employee records with the complete Myanmar
administrative address hierarchy for private addresses, powered by MIMU P-code data.

Main Features
-------------
* Myanmar address fields in the Private Information tab of employee records
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
        'hr',
        'l10n_mm_address',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        # Views
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
} # type: ignore
