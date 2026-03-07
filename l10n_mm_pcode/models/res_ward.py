from odoo import _, api, fields, models


class ResWard(models.Model):
    _name = 'res.ward'
    _description = 'Myanmar Ward / Village Tract'
    _rec_name = 'name'
    _order = 'p_code'

    name = fields.Char(required=True)
    p_code = fields.Char(
        string='P-Code',
        required=True,
        size=15,
        help='Official MIMU Place Code (P-code) uniquely identifying this '
            'administrative unit. Example: MMR017024040. '
            'Structured hierarchically by Country → State/Region → District → '
            'Township → Ward/Village Tract.',
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
    ward_type = fields.Selection([
        ('ward', 'Ward'),
        ('village_tract', 'Village Tract')],
    string='Type',
    required=True,
    default='ward',
    help='Specifies whether this record is a Ward or a Village Tract.'
    )

    _sql_constraints = [
        ('p_code_uniq', 'unique(p_code)', 'P-code must be unique!'),
    ]

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

    @api.model
    def _name_search(self, name='', domain=None, operator='ilike', limit=None, order=None):
        # Search by name, p_code, township, or district
        domain = domain or []
        if name:
            domain = ['|', '|', '|',
                      ('name', operator, name),
                      ('p_code', operator, name),
                      ('township_id.name', operator, name),
                      ('township_id.district_id.name', operator, name)] + domain
        return self._search(domain, limit=limit, order=order)
