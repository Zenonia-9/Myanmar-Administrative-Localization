# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    use_myanmar_language = fields.Boolean(
        string="Use Myanmar Language",
        config_parameter='l10n_mm_address.use_myanmar_language'
    )
