from odoo import api, fields, models
from odoo.fields import Domain


class ResTown(models.Model):
    _name = 'res.town'
    _description = 'Myanmar Town'
    _order = 'name'
    _rec_names_search = ['name', 'name_mm']

    name = fields.Char(required=True)
    name_mm = fields.Char()
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

    _code_uniq = models.Constraint('UNIQUE (code)', 'Town code must be unique!')

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_address.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name

    @api.model
    def _search_display_name(self, operator, value):
        return Domain('name', operator, value) | Domain('name_mm', operator, value)