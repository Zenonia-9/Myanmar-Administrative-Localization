from odoo import api, fields, models


class ResDistrict(models.Model):
    _name = 'res.district'
    _description = 'Myanmar District'
    _order = 'name'

    name = fields.Char(required=True)
    name_mm = fields.Char(string='Myanmar Name')
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

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_pcode.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name