from odoo import api, fields, models


class ResTownship(models.Model):
    _name = 'res.township'
    _description = 'Myanmar Township'

    name = fields.Char(required=True)
    code = fields.Char(
        string='Township Code',
        required=True,
        size=9,
        help='Official Myanmar Information Management Unit (MIMU) '
            'Township P-code. Example: MMR017024 where '
            'MMR017 = State/Region and 024 = Township.',
    )
    district_id = fields.Many2one(
        'res.district',
        string='District',
        required=True,
    )
