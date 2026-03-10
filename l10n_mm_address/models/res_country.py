from odoo import fields, models


class ResCountry(models.Model):
    _inherit = "res.country"

    enforce_townships = fields.Boolean(
        string="Enforce Townships",
        help="When enabled, addresses in this country will require "
        "selecting a township from the predefined list.",
    )
