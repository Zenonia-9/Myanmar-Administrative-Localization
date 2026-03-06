# -*- coding: utf-8 -*-
{
    'name': "Myanmar HR Localization",
    'version': "18.0.0.1",
    'summary': "Myanmar address fields for employee private addresses",
    'description': """
Myanmar HR Localization

Extends employee private addresses with Myanmar administrative hierarchy fields.
""",
    'category': 'Human Resources/Localization',
    'author': "Zenonia",
    'website': "https://github.com/Zenonia-9/Myanmar-Administrative-Localization",
    'license': 'LGPL-3',
    'depends': ['hr', 'l10n_mm_pcode'],
    'images': [
        'static/description/icon.png',
    ],
    'data': [
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}  # type: ignore
