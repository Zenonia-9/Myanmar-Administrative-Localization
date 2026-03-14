# -*- coding: utf-8 -*-
{
    'name': "Myanmar CRM Address Localization",
    'version': "18.0.4.0",
    'summary': "Myanmar address fields for CRM leads and opportunities",
    'description': """
Myanmar CRM Address Localization

Extends CRM leads/opportunities with Myanmar administrative hierarchy fields
using the l10n_mm_address module.
""",
    'category': 'Sales/CRM/Localization',
    'author': "Zenonia",
    'license': 'LGPL-3',
    'depends': ['crm', 'l10n_mm_address'],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
} # type: ignore
