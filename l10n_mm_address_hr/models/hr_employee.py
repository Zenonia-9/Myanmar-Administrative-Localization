from odoo import api, fields, models
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    private_l10n_mm_district_id = fields.Many2one(
        'res.district',
        string='Private District',
        compute='_compute_private_l10n_mm_district_id',
        readonly=False,
        store=True,
        groups="hr.group_hr_user",
        domain="[('state_id', '=', private_state_id)]"
    )
    private_l10n_mm_township_id = fields.Many2one(
        'res.township',
        string='Private Township',
        compute='_compute_private_l10n_mm_township_id',
        readonly=False,
        store=True,
        groups="hr.group_hr_user",
        domain="[('district_id', '=', private_l10n_mm_district_id)]"
    )
    private_l10n_mm_town_id = fields.Many2one(
        'res.town',
        string='Private Town',
        groups="hr.group_hr_user",
        domain="[('township_id', '=', private_l10n_mm_township_id)]"
    )
    private_l10n_mm_ward_id = fields.Many2one(
        'res.ward',
        string='Private Ward',
        groups="hr.group_hr_user"
    )
    private_l10n_mm_ward_ids = fields.Many2many(
        'res.ward',
        compute='_compute_private_ward_ids',
        string='Private Wards for Dropdown'
    )
    private_l10n_mm_zip_id = fields.Many2one(
        'res.zip',
        string='Private Zip Code',
        groups="hr.group_hr_user",
        domain="[('township_id','=',private_l10n_mm_township_id)]"
    )
    private_l10n_mm_pcode = fields.Char(
        string='Private P-Code',
        groups="hr.group_hr_user",
        help='Myanmar MIMU P-code for auto-filling address'
    )
    private_l10n_mm_postalcode = fields.Char(
        string="Private Postal Code",
        groups="hr.group_hr_user",
        help="7 digits Postal Code"
    )
    private_l10n_mm_is_myanmar = fields.Boolean(
        compute='_compute_private_l10n_mm_is_myanmar'
    )

    @api.depends('private_country_id')
    def _compute_private_l10n_mm_is_myanmar(self):
        mm = self.env.ref('base.mm', raise_if_not_found=False)
        for emp in self:
            emp.private_l10n_mm_is_myanmar = mm and emp.private_country_id == mm

    @api.depends('private_l10n_mm_township_id')
    def _compute_private_l10n_mm_district_id(self):
        for emp in self:
            if emp.private_l10n_mm_township_id:
                emp.private_l10n_mm_district_id = emp.private_l10n_mm_township_id.district_id
            elif not emp.private_l10n_mm_district_id:
                emp.private_l10n_mm_district_id = False

    @api.depends('private_l10n_mm_ward_id')
    def _compute_private_l10n_mm_township_id(self):
        for emp in self:
            if emp.private_l10n_mm_ward_id:
                emp.private_l10n_mm_township_id = emp.private_l10n_mm_ward_id.township_id
            elif not emp.private_l10n_mm_township_id:
                emp.private_l10n_mm_township_id = False

    @api.depends('private_l10n_mm_ward_id', 'private_l10n_mm_township_id', 'private_l10n_mm_district_id', 'private_state_id', 'private_country_id')
    def _compute_private_ward_ids(self):
        for emp in self:
            domain = []
            if emp.private_l10n_mm_town_id:
                domain = [('town_id', '=', emp.private_l10n_mm_town_id.id)]
            elif emp.private_l10n_mm_township_id:
                domain = [('township_id', '=', emp.private_l10n_mm_township_id.id)]
            elif emp.private_l10n_mm_district_id:
                domain = [('district_id', '=', emp.private_l10n_mm_district_id.id)]
            elif emp.private_state_id:
                domain = [('state_id', '=', emp.private_state_id.id)]
            elif emp.private_country_id:
                domain = [('country_id', '=', emp.private_country_id.id)]
            emp.private_l10n_mm_ward_ids = self.env['res.ward'].search(domain)

    @api.onchange('private_l10n_mm_pcode')
    def _onchange_private_l10n_mm_pcode(self):
        if self.private_l10n_mm_pcode:
            ward = self.env['res.ward'].search([('p_code', '=', self.private_l10n_mm_pcode)], limit=1)
            if ward:
                self.private_l10n_mm_ward_id = ward
                self.private_l10n_mm_town_id = ward.town_id
                self.private_l10n_mm_township_id = ward.township_id
                self.private_l10n_mm_district_id = ward.township_id.district_id
                self.private_l10n_mm_postalcode = ward.postal_code
                self.private_state_id = ward.township_id.district_id.state_id
                self.private_country_id = self.private_state_id.country_id
            else:
                raise UserError(f'Invalid P-Code: {self.private_l10n_mm_pcode}. Please enter a valid Myanmar MIMU P-code.')

    @api.onchange('private_l10n_mm_ward_id')
    def _onchange_private_l10n_mm_ward_id(self):
        if self.private_l10n_mm_ward_id:
            self.private_l10n_mm_pcode = self.private_l10n_mm_ward_id.p_code
            self.private_l10n_mm_postalcode = self.private_l10n_mm_ward_id.postal_code
            self.private_state_id = self.private_l10n_mm_ward_id.township_id.district_id.state_id
            self.private_country_id = self.private_state_id.country_id
            if self.private_l10n_mm_zip_id and self.private_l10n_mm_zip_id.township_id != self.private_l10n_mm_township_id:
                self.private_l10n_mm_zip_id = False

    @api.onchange('private_l10n_mm_town_id')
    def _onchange_private_l10n_mm_town_id(self):
        if self.private_l10n_mm_town_id:
            self.private_state_id = self.private_l10n_mm_town_id.township_id.district_id.state_id
            self.private_country_id = self.private_state_id.country_id
            if self.private_l10n_mm_ward_id and self.private_l10n_mm_ward_id.town_id != self.private_l10n_mm_town_id:
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_postalcode = False
                self.private_l10n_mm_pcode = False

    @api.onchange('private_l10n_mm_township_id')
    def _onchange_private_l10n_mm_township_id(self):
        if self.private_l10n_mm_township_id:
            self.private_state_id = self.private_l10n_mm_township_id.district_id.state_id
            self.private_country_id = self.private_state_id.country_id
            if self.private_l10n_mm_ward_id and self.private_l10n_mm_ward_id.township_id != self.private_l10n_mm_township_id:
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_postalcode = False
                self.private_l10n_mm_pcode = False
                self.private_l10n_mm_zip_id = False
            if self.private_l10n_mm_town_id and self.private_l10n_mm_town_id.township_id != self.private_l10n_mm_township_id:
                self.private_l10n_mm_town_id = False

    @api.onchange('private_l10n_mm_district_id')
    def _onchange_private_l10n_mm_district_id(self):
        if self.private_l10n_mm_district_id:
            self.private_state_id = self.private_l10n_mm_district_id.state_id
            self.private_country_id = self.private_state_id.country_id
            if self.private_l10n_mm_township_id and self.private_l10n_mm_township_id.district_id != self.private_l10n_mm_district_id:
                self.private_l10n_mm_township_id = False
                self.private_l10n_mm_town_id = False
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_postalcode = False
                self.private_l10n_mm_pcode = False
                self.private_l10n_mm_zip_id = False

    @api.onchange('private_state_id')
    def _onchange_private_state_id(self):
        if self.private_l10n_mm_is_myanmar and self.private_state_id:
            if self.private_l10n_mm_district_id and self.private_l10n_mm_district_id.state_id != self.private_state_id:
                self.private_l10n_mm_district_id = False
                self.private_l10n_mm_township_id = False
                self.private_l10n_mm_town_id = False
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_postalcode = False
                self.private_l10n_mm_pcode = False
                self.private_l10n_mm_zip_id = False

    @api.onchange('private_country_id')
    def _onchange_private_country_id(self):
        mm = self.env.ref('base.mm', raise_if_not_found=False)
        if mm and self.private_country_id != mm:
            self.private_state_id = False
            self.private_l10n_mm_district_id = False
            self.private_l10n_mm_township_id = False
            self.private_l10n_mm_town_id = False
            self.private_l10n_mm_ward_id = False
            self.private_l10n_mm_postalcode = False
            self.private_l10n_mm_pcode = False
            self.private_l10n_mm_zip_id = False
