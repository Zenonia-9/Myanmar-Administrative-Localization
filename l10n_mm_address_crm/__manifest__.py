# -*- coding: utf-8 -*-
{
    'name': 'Myanmar CRM Address Localization',
    'version': '19.0.1.0',
    'category': 'Sales/CRM/Localization',
    'summary': 'Myanmar address hierarchy fields for CRM leads and opportunities with MIMU P-code integration.',
    'description': """
Myanmar CRM Address Localization
==================================

This module extends Odoo CRM leads and opportunities with the complete Myanmar
administrative address hierarchy, powered by MIMU P-code data from l10n_mm_address.

Main Features
-------------
* Myanmar address fields in the Extra Information tab of leads and opportunities
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
        'crm',
        'l10n_mm_address',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        # Views
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
} # type: ignore
