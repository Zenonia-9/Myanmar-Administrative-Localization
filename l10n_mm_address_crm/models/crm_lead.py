from odoo import api, fields, models
from odoo.exceptions import UserError


class Lead(models.Model):
    _inherit = 'crm.lead'

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
    l10n_mm_ward_ids = fields.Many2many(
        'res.ward',
        compute='_compute_ward_ids',
        string='Wards for Dropdown'
    )
    l10n_mm_zip_id = fields.Many2one(
        'res.zip',
        string='Zip Code',
        domain="[('township_id','=',l10n_mm_township_id)]"
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

    @api.depends('l10n_mm_town_id', 'l10n_mm_township_id', 'l10n_mm_district_id', 'state_id', 'country_id')
    def _compute_ward_ids(self):
        for rec in self:
            domain = []
            if rec.l10n_mm_town_id:
                domain = [('town_id', '=', rec.l10n_mm_town_id.id)]
            elif rec.l10n_mm_township_id:
                domain = [('township_id', '=', rec.l10n_mm_township_id.id)]
            elif rec.l10n_mm_district_id:
                domain = [('district_id', '=', rec.l10n_mm_district_id.id)]
            elif rec.state_id:
                domain = [('state_id', '=', rec.state_id.id)]
            elif rec.country_id:
                domain = [('country_id', '=', rec.country_id.id)]
            rec.l10n_mm_ward_ids = self.env['res.ward'].search(domain)

    @api.onchange('l10n_mm_pcode')
    def _onchange_l10n_mm_pcode(self):
        if self.l10n_mm_pcode:
            ward = self.env['res.ward'].search([('p_code', '=', self.l10n_mm_pcode)], limit=1)
            if ward:
                self.l10n_mm_ward_id = ward
                self.l10n_mm_town_id = ward.town_id
                self.l10n_mm_township_id = ward.township_id
                self.l10n_mm_district_id = ward.township_id.district_id
                self.l10n_mm_postalcode = ward.postal_code
                self.state_id = ward.township_id.district_id.state_id
                self.country_id = self.state_id.country_id
            else:
                raise UserError(f'Invalid P-Code: {self.l10n_mm_pcode}. Please enter a valid Myanmar MIMU P-code.')

    @api.onchange('l10n_mm_ward_id')
    def _onchange_l10n_mm_ward_id(self):
        if self.l10n_mm_ward_id:
            self.l10n_mm_pcode = self.l10n_mm_ward_id.p_code
            self.l10n_mm_postalcode = self.l10n_mm_ward_id.postal_code
            self.state_id = self.l10n_mm_ward_id.township_id.district_id.state_id
            self.country_id = self.state_id.country_id
            if self.l10n_mm_zip_id and self.l10n_mm_zip_id.township_id != self.l10n_mm_township_id:
                self.l10n_mm_zip_id = False

    @api.onchange('l10n_mm_town_id')
    def _onchange_l10n_mm_town_id(self):
        if self.l10n_mm_town_id:
            self.state_id = self.l10n_mm_town_id.township_id.district_id.state_id
            self.country_id = self.state_id.country_id
            if self.l10n_mm_ward_id and self.l10n_mm_ward_id.town_id != self.l10n_mm_town_id:
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False

    @api.onchange('l10n_mm_township_id')
    def _onchange_l10n_mm_township_id(self):
        if self.l10n_mm_township_id:
            self.state_id = self.l10n_mm_township_id.district_id.state_id
            self.country_id = self.state_id.country_id
            if self.l10n_mm_ward_id and self.l10n_mm_ward_id.township_id != self.l10n_mm_township_id:
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False
                self.l10n_mm_zip_id = False
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
                self.l10n_mm_zip_id = False

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
                self.l10n_mm_zip_id = False

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
            self.l10n_mm_zip_id = False
