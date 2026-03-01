from odoo import _, api, fields, models


class ResWard(models.Model):
    _name = 'res.ward'
    _description = 'Myanmar Ward / Village Tract'
    _rec_name = 'name'

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

    @api.depends(
        "name",
        "township_id.name",
        "township_id.district_id.name",
    )
    def _compute_display_name(self):
        for rec in self:
            parts = [rec.name or ""]
            if rec.township_id:
                parts.append(rec.township_id.name)
            if rec.township_id.district_id:
                parts.append(rec.township_id.district_id.name)
            rec.display_name = ", ".join(p for p in parts if p)
