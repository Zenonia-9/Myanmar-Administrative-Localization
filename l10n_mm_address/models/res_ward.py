from odoo import _, api, fields, models


class ResWard(models.Model):
    _name = 'res.ward'
    _description = 'Myanmar Ward / Village Tract'
    _rec_name = 'name'
    _order = 'p_code'

    name = fields.Char(required=True)
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
    # country_id = fields.Many2one(
    #     'res.country', string='Country', compute='_compute_country_id', store=True
    # )

    _sql_constraints = [
        ('p_code_uniq', 'unique(p_code)', 'P-code must be unique!'),
    ]

    # @api.depends('township_id', 'township_id.district_id.state_id', 'township_id.district_id.state_id.country_id')
    # def _compute_country_id(self):
    #     for rec in self:
    #         rec.country_id = rec.township_id.district_id.state_id.country_id if rec.township_id and rec.township_id.district_id and rec.township_id.district_id.state_id else False
    
    @api.depends(
        "name",
        "township_id.name",
        "township_id.district_id.name",
    )
    def _compute_display_name(self):
        # Compute display name with hierarchical structure: Ward, Township, District
        for rec in self:
            parts = [rec.name or ""]
            if rec.township_id:
                parts.append(rec.township_id.name)
            if rec.township_id.district_id:
                parts.append(rec.township_id.district_id.name)
            rec.display_name = ", ".join(p for p in parts if p)
