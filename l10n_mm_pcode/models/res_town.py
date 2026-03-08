from odoo import _, api, fields, models


class ResTown(models.Model):
    _name = 'res.town'
    _description = 'Myanmar Town'
    _order = 'name'

    name = fields.Char(required=True)
    name_mm = fields.Char(string='Myanmar Name')
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

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'Town code must be unique!'),
    ]

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_pcode.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name