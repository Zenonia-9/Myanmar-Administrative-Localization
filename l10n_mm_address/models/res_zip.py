from odoo import models, fields

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

