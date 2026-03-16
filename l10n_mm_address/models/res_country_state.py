from odoo import api, fields, models


class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    name_mm = fields.Char(string='Myanmar Name')

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_address.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name

    def _search_display_name(self, operator, value):
        return [
            '|',
            ('name', operator, value),
            ('name_mm', operator, value),
        ]
