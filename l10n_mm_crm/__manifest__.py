# -*- coding: utf-8 -*-
{
    'name': "Myanmar CRM Localization",
    'version': "18.0.0.1",
    'summary': "Adds Myanmar administrative fields to CRM leads/opportunities",
    'description': """
Myanmar CRM Localization

Extends CRM leads/opportunities with Myanmar administrative hierarchy fields
in the Extra Information tab.
""",
    'category': 'Sales/CRM',
    'author': "Zenonia",
    'website': "https://github.com/Zenonia-9/Myanmar-Administrative-Localization",
    'license': 'LGPL-3',
    'depends': ['crm', 'l10n_mm_pcode'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}  # type: ignore
