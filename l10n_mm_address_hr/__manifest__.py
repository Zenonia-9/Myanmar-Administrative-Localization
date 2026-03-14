# -*- coding: utf-8 -*-
{
    'name': "Myanmar HR Address Localization",
    'version': "18.0.1.0",
    'summary': "Myanmar address fields for employee private addresses",
    'description': """
Myanmar HR Address Localization

Extends employee private addresses with Myanmar administrative hierarchy fields.
""",
    'category': 'Human Resources/Localization',
    'author': "Zenonia",
    'license': 'LGPL-3',
    'depends': ['hr', 'l10n_mm_address'],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
