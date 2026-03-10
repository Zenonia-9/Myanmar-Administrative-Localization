from odoo import api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_mm_district_id = fields.Many2one(
        'res.district', 
        string='District', 
        compute='_compute_l10n_mm_district_id', 
        readonly=False, 
        store=True, 
        domain="[('state_id', '=', state_id)]"
    )
    l10n_mm_township_id = fields.Many2one(
        'res.township',
        string='Township',
        compute='_compute_l10n_mm_township_id',
        readonly=False,
        store=True,
        domain="[('district_id', '=', l10n_mm_district_id)]"
    )
    l10n_mm_town_id = fields.Many2one(
        'res.town',
        string='Town',
        domain="[('township_id', '=', l10n_mm_township_id)]"
    )
    l10n_mm_ward_id = fields.Many2one(
        'res.ward',
        string='Ward'
    )
    l10n_mm_ward_name = fields.Char(
        related='l10n_mm_ward_id.name',
        readonly=True
    )
    l10n_mm_town_name = fields.Char(
        related='l10n_mm_town_id.name',
        readonly=True
    )
    l10n_mm_township_name = fields.Char(
        related='l10n_mm_township_id.name',
        readonly=True
    )
    l10n_mm_district_name = fields.Char(
        related='l10n_mm_district_id.name',
        readonly=True
    )
    l10n_mm_pcode = fields.Char(
        string='P-Code',
        help='Myanmar MIMU P-code for auto-filling address'
    )
    l10n_mm_postalcode = fields.Char(
        string="Postal Code",
        help="7 digits Postal Code"
    )
    l10n_mm_is_myanmar = fields.Boolean(
        compute='_compute_l10n_mm_is_myanmar'
    )

    @api.depends('country_id')
    def _compute_l10n_mm_is_myanmar(self):
        mm = self.env.ref('base.mm', raise_if_not_found=False)
        for rec in self:
            rec.l10n_mm_is_myanmar = mm and rec.country_id == mm

    @api.depends('l10n_mm_township_id')
    def _compute_l10n_mm_district_id(self):
        for rec in self:
            if rec.l10n_mm_township_id:
                rec.l10n_mm_district_id = rec.l10n_mm_township_id.district_id
            elif not rec.l10n_mm_district_id:
                rec.l10n_mm_district_id = False

    @api.depends('l10n_mm_ward_id')
    def _compute_l10n_mm_township_id(self):
        for rec in self:
            if rec.l10n_mm_ward_id:
                rec.l10n_mm_township_id = rec.l10n_mm_ward_id.township_id
            elif not rec.l10n_mm_township_id:
                rec.l10n_mm_township_id = False

    @api.onchange('l10n_mm_pcode')
    def _onchange_l10n_mm_pcode(self):
        if self.l10n_mm_pcode:
            ward = self.env['res.ward'].search([('p_code', '=', self.l10n_mm_pcode)], limit=1)
            if ward:
                self.l10n_mm_ward_id = ward
                self.l10n_mm_town_id = ward.town_id
                self.l10n_mm_township_id = ward.township_id
                self.l10n_mm_district_id = ward.township_id.district_id
                self.l10n_mm_postalcode = self.l10n_mm_ward_id.postal_code
                self.zip = ward.township_id.zip
                self.state_id = ward.township_id.district_id.state_id
                self.country_id = self.state_id.country_id
            else:
                raise UserError(f'Invalid P-Code: {self.l10n_mm_pcode}. Please enter a valid Myanmar MIMU P-code.')

    @api.onchange('l10n_mm_ward_id')
    def _onchange_l10n_mm_ward_id(self):
        if self.l10n_mm_ward_id:
            self.l10n_mm_pcode = self.l10n_mm_ward_id.p_code
            self.l10n_mm_postalcode = self.l10n_mm_ward_id.postal_code
            self.zip = self.l10n_mm_ward_id.township_id.zip
            self.state_id = self.l10n_mm_ward_id.township_id.district_id.state_id
            self.country_id = self.state_id.country_id

    @api.onchange('l10n_mm_township_id')
    def _onchange_l10n_mm_township_id(self):
        if self.l10n_mm_township_id:
            self.zip = self.l10n_mm_township_id.zip
            self.state_id = self.l10n_mm_township_id.district_id.state_id
            self.country_id = self.state_id.country_id
            if self.l10n_mm_ward_id and self.l10n_mm_ward_id.township_id != self.l10n_mm_township_id:
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False
            if self.l10n_mm_town_id and self.l10n_mm_town_id.township_id != self.l10n_mm_township_id:
                self.l10n_mm_town_id = False

    @api.onchange('l10n_mm_district_id')
    def _onchange_l10n_mm_district_id(self):
        if self.l10n_mm_district_id:
            self.state_id = self.l10n_mm_district_id.state_id
            self.country_id = self.state_id.country_id
            if self.l10n_mm_township_id and self.l10n_mm_township_id.district_id != self.l10n_mm_district_id:
                self.l10n_mm_township_id = False
                self.l10n_mm_town_id = False
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False
                self.zip = False

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.l10n_mm_is_myanmar and self.state_id:
            if self.l10n_mm_district_id and self.l10n_mm_district_id.state_id != self.state_id:
                self.l10n_mm_district_id = False
                self.l10n_mm_township_id = False
                self.l10n_mm_town_id = False
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False
                self.zip = False

    @api.onchange('country_id')
    def _onchange_country_id(self):
        mm = self.env.ref('base.mm', raise_if_not_found=False)
        if mm and self.country_id != mm:
            self.state_id = False
            self.l10n_mm_district_id = False
            self.l10n_mm_township_id = False
            self.l10n_mm_town_id = False
            self.l10n_mm_ward_id = False
            self.l10n_mm_postalcode = False
            self.l10n_mm_pcode = False
            self.zip = False

    def _address_fields(self):
        fields_list = super()._address_fields()
        return fields_list + ['l10n_mm_district_id', 'l10n_mm_township_id', 'l10n_mm_town_id', 'l10n_mm_ward_id']

    @api.model
    def _formatting_address_fields(self):
        return super()._formatting_address_fields() + [
            'l10n_mm_district_name',
            'l10n_mm_township_name',
            'l10n_mm_town_name',
            'l10n_mm_ward_name',
            'l10n_mm_pcode',
        ]

    def _display_address_depends(self):
        return super()._display_address_depends() + [
            'l10n_mm_district_id',
            'l10n_mm_township_id',
            'l10n_mm_town_id',
            'l10n_mm_ward_id',
        ]