from odoo import _, api, fields, models


class ResTown(models.Model):
    _name = 'res.town'
    _description = 'Myanmar Town'

    name = fields.Char(required=True)
    code = fields.Char(
        string='Town Code',
        required=True,
        size=12,
        help='Official MIMU Town-level Place Code identifying this town. '
            'Example: MMR013010701. '
            'Structured hierarchically under its Township and District.',
    )
    township_id = fields.Many2one(
        'res.township',
        string='Township',
        required=True,
    )