from odoo import api, fields, models


class ResTownship(models.Model):
    _name = 'res.township'
    _description = 'Myanmar Township'
    _order = 'code'

    name = fields.Char(required=True)
    code = fields.Char(
        string='Township Code',
        required=True,
        size=9,
        help='Official Myanmar Information Management Unit (MIMU) '
            'Township P-code. Example: MMR017024 where '
            'MMR017 = State/Region and 024 = Township.',
    )
    zip_ids = fields.One2many(
        'res.zip',
        'township_id',
        string='Zip Code',
        readonly=True,
    )
    ward_ids = fields.One2many(
        'res.ward',
        'township_id',
        string='Wards',
        readonly=True,
    )
    district_id = fields.Many2one(
        'res.district',
        string='District',
        required=True,
    )
    latitude = fields.Float(string="Latitude", digits=(16, 6))
    longitude = fields.Float(string="Longitude", digits=(16, 6))

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Township code must be unique!'),
    ]
