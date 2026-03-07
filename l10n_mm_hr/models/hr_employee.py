
from odoo import api, fields, models
from odoo.exceptions import UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    private_l10n_mm_district_id = fields.Many2one(
        'res.district',
        compute='_compute_private_l10n_mm_district_id',
        readonly=False,
        store=True,
        groups="hr.group_hr_user"
    )
    private_l10n_mm_township_id = fields.Many2one(
        'res.township',
        compute='_compute_private_l10n_mm_township_id',
        readonly=False,
        store=True,
        groups="hr.group_hr_user"
    )
    private_l10n_mm_town_id = fields.Many2one('res.town', groups="hr.group_hr_user")
    private_l10n_mm_ward_id = fields.Many2one('res.ward', groups="hr.group_hr_user")
    private_l10n_mm_pcode = fields.Char(groups="hr.group_hr_user")
    private_l10n_mm_is_myanmar = fields.Boolean(compute='_compute_private_l10n_mm_is_myanmar')

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

    @api.onchange('private_l10n_mm_pcode')
    def _onchange_private_l10n_mm_pcode(self):
        if self.private_l10n_mm_pcode:
            ward = self.env['res.ward'].search([('p_code', '=', self.private_l10n_mm_pcode)], limit=1)
            if ward:
                self.private_l10n_mm_ward_id = ward
                self.private_l10n_mm_town_id = ward.town_id
                self.private_l10n_mm_township_id = ward.township_id
                self.private_l10n_mm_district_id = ward.township_id.district_id
                self.private_state_id = ward.township_id.district_id.state_id
                self.private_country_id = self.private_state_id.country_id
            else:
                raise UserError(f'Invalid P-Code: {self.private_l10n_mm_pcode}. Please enter a valid Myanmar MIMU P-code.')

    @api.onchange('private_l10n_mm_ward_id')
    def _onchange_private_l10n_mm_ward_id(self):
        if self.private_l10n_mm_ward_id:
            self.private_l10n_mm_pcode = self.private_l10n_mm_ward_id.p_code
            self.private_state_id = self.private_l10n_mm_ward_id.township_id.district_id.state_id
            self.private_country_id = self.private_state_id.country_id

    @api.onchange('private_l10n_mm_township_id')
    def _onchange_private_l10n_mm_township_id(self):
        if self.private_l10n_mm_township_id:
            self.private_state_id = self.private_l10n_mm_township_id.district_id.state_id
            self.private_country_id = self.private_state_id.country_id
            if self.private_l10n_mm_ward_id and self.private_l10n_mm_ward_id.township_id != self.private_l10n_mm_township_id:
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_pcode = False
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
                self.private_l10n_mm_pcode = False

    @api.onchange('private_state_id')
    def _onchange_private_state_id(self):
        if self.private_l10n_mm_is_myanmar and self.private_state_id:
            if self.private_l10n_mm_district_id and self.private_l10n_mm_district_id.state_id != self.private_state_id:
                self.private_l10n_mm_district_id = False
                self.private_l10n_mm_township_id = False
                self.private_l10n_mm_town_id = False
                self.private_l10n_mm_ward_id = False
                self.private_l10n_mm_pcode = False

    @api.onchange('private_country_id')
    def _onchange_private_country_id(self):
        mm = self.env.ref('base.mm', raise_if_not_found=False)
        if mm and self.private_country_id != mm:
            self.private_state_id = False
            self.private_l10n_mm_district_id = False
            self.private_l10n_mm_township_id = False
            self.private_l10n_mm_town_id = False
            self.private_l10n_mm_ward_id = False
            self.private_l10n_mm_pcode = False
