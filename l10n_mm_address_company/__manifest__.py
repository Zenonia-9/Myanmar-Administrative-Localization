# -*- coding: utf-8 -*-
{
    'name': 'Myanmar Company Address Localization',
    'version': '19.0.1.0',
    'category': 'Localization/Contacts',
    'summary': 'Myanmar address hierarchy fields for company settings with MIMU P-code integration.',
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
