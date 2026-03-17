from odoo import api, models, fields

class ResZip(models.Model):
    _name = 'res.zip'
    _description = "Myanmar Post Code"

    name = fields.Char(required=True)
    postcode = fields.Char(
        string="Postcode",
        size=5,
        required=True,
    )
    township_id = fields.Many2one(
        'res.township',
        string='Township',
        required=True,
    )
    district_id = fields.Many2one('res.district', related='township_id.district_id', store=True)
    state_id = fields.Many2one('res.country.state', related='district_id.state_id', store=True)
    country_id = fields.Many2one('res.country', related='state_id.country_id', store=True)

    @api.depends(
        "name",
        "postcode",
    )
    def _compute_display_name(self):
        # Compute display name with hierarchical structure: Ward, Township, District
        for rec in self:
            parts = [rec.postcode or ""]
            if rec.name:
                parts.append(rec.name)
            rec.display_name = ", ".join(p for p in parts if p)

    def _search_display_name(self, operator, value):
        return [
            '|',
            ('name', operator, value),
            ('postcode', operator, value),
        ]
