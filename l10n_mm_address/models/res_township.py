from odoo import api, fields, models
from odoo.fields import Domain


class ResTownship(models.Model):
    _name = 'res.township'
    _description = 'Myanmar Township'
    _order = 'name'
    _rec_names_search = ['name', 'name_mm']

    name = fields.Char(required=True)
    name_mm = fields.Char()
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
    state_id = fields.Many2one('res.country.state', related='district_id.state_id', store=True)
    country_id = fields.Many2one('res.country', related='state_id.country_id', store=True)
    latitude = fields.Float(string="Latitude", digits=(10, 7))
    longitude = fields.Float(string="Longitude", digits=(10, 7))

    _code_uniq = models.Constraint('UNIQUE (code)', 'Township code must be unique!')

    @api.depends('name', 'name_mm')
    def _compute_display_name(self):
        use_mm = self.env['ir.config_parameter'].sudo().get_param('l10n_mm_address.use_myanmar_language')
        for rec in self:
            rec.display_name = rec.name_mm if use_mm and rec.name_mm else rec.name

    @api.model
    def _search_display_name(self, operator, value):
        return Domain('|', ('name', operator, value), ('name_mm', operator, value))
