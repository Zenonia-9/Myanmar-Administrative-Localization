from odoo import api, fields, models


class ResTownship(models.Model):
    _name = 'res.township'
    _description = 'Myanmar Township'
    _order = 'name'

    name = fields.Char(required=True)
    name_mm = fields.Char(string='Myanmar Name')
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

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Township code must be unique!'),
    ]

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_pcode.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name
