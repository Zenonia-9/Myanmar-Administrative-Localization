from odoo import api, fields, models


class ResDistrict(models.Model):
    _name = 'res.district'
    _description = 'Myanmar District'
    _order = 'code'

    name = fields.Char(required=True)
    code = fields.Char(
        string='District Code',
        required=True,
        size=10,
        help='Official Myanmar Information Management Unit (MIMU) '
            'District P-code. Example: MMR001D001 where '
            'MMR001 = State/Region and D001 = District.',
    )
    state_id = fields.Many2one(
        'res.country.state',
        string='Region / State',
        required=True,
    )
    district_type = fields.Selection([
        ('district', 'District'),
        ('saz', 'Self-Administered Zone'),
        ('sad', 'Self-Administered Division'),
    ],  default='district')

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'District code must be unique!'),
    ]