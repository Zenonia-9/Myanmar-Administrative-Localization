from odoo import api, fields, models
from odoo.fields import Domain


class ResWard(models.Model):
    _name = 'res.ward'
    _description = 'Myanmar Ward / Village Tract'
    _rec_name = 'name'
    _order = 'name'
    _rec_names_search = ['name', 'name_mm', 'township_id.name', 'township_id.name_mm', 'state_id.name', 'state_id.name_mm']

    name = fields.Char(required=True)
    name_mm = fields.Char()
    p_code = fields.Char(
        string='Ward P-Code',
        required=True,
        size=15,
        help='Official MIMU Place Code (P-code) uniquely identifying this '
            'administrative unit. Example: MMR017024040. '
            'Structured hierarchically by Country → State/Region → District → '
            'Township → Ward/Village Tract.',
    )
    postal_code = fields.Char(
        string='Postal Code',
        size=7,
        help='',
    )
    ward_type = fields.Selection(
        [
        ('ward', 'Ward'),
        ('village_tract', 'Village Tract')
        ],
        string='Type',
        required=True,
        default='ward',
        help='Specifies whether this record is a Ward or a Village Tract.'
    )
    township_id = fields.Many2one(
        'res.township',
        string='Township',
        required=True,
    )
    town_id = fields.Many2one(
        'res.town',
        string='Town',
    )
    district_id = fields.Many2one('res.district', related='township_id.district_id', store=True)
    state_id = fields.Many2one('res.country.state', related='district_id.state_id', store=True)
    country_id = fields.Many2one('res.country', related='state_id.country_id', store=True)

    _sql_constraints = [
        ('p_code_uniq', 'unique(p_code)', 'P-code must be unique!'),
    ]

    @api.depends(
        'name', 'name_mm',
        'township_id.name', 'township_id.name_mm',
        'state_id.name', 'state_id.name_mm',
    )
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_address.use_myanmar_language')
        for rec in self:
            parts = [rec.name_mm if use_mm and rec.name_mm else rec.name]
            if rec.township_id:
                parts.append(rec.township_id.name_mm if use_mm and rec.township_id.name_mm else rec.township_id.name)
            if rec.state_id:
                parts.append(rec.state_id.name_mm if use_mm and rec.state_id.name_mm else rec.state_id.name)
            rec.display_name = ', '.join(p for p in parts if p)

    @api.model
    def _search_display_name(self, operator, value):
        return Domain(
            '|', ('name', operator, value),
            '|', ('name_mm', operator, value),
            '|', ('township_id.name', operator, value),
            '|', ('township_id.name_mm', operator, value),
            '|', ('state_id.name', operator, value),
                 ('state_id.name_mm', operator, value),
        )
