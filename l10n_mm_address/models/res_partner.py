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
        store=True
    )
    l10n_mm_township_ids = fields.Many2many(
        'res.township', compute='_compute_township_ids', string='Townships for Dropdown'
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
        'res.ward', compute='_compute_ward_ids', string='Wards for Dropdown'
    )
    l10n_mm_zip_id = fields.Many2one(
        'res.zip',
        string='Zip Code',
        domain="[('township_id','=', l10n_mm_township_id)]"
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
    l10n_mm_postcode = fields.Char(
        related='l10n_mm_zip_id.postcode',
        readonly=True,
    )
    partner_latitude = fields.Float(
        related="l10n_mm_township_id.latitude",
        store=True
    )
    partner_longitude = fields.Float(
        related="l10n_mm_township_id.longitude",
        store=True
    )
    l10n_mm_is_myanmar = fields.Boolean(
        compute='_compute_l10n_mm_is_myanmar'
    )
    l10n_mm_full_address = fields.Text(string="Myanmar Address", compute="_compute_mm_address")

    @api.depends('street', 'street2', 'l10n_mm_ward_name', 'l10n_mm_town_name', 'l10n_mm_township_name', 'l10n_mm_district_name', 'state_id', 'l10n_mm_postcode', 'country_id')
    def _compute_mm_address(self):
        for rec in self:
            lines = []
            if rec.street:
                lines.append(rec.street)
            if rec.street2:
                lines.append(rec.street2)
            if rec.l10n_mm_ward_name:
                lines.append(rec.l10n_mm_ward_name)
            # Handle town + township with conditional comma
            town_line = ''
            if rec.l10n_mm_town_name:
                town_line += rec.l10n_mm_town_name
                if rec.l10n_mm_township_name:
                    town_line += ', ' + rec.l10n_mm_township_name
            elif rec.l10n_mm_township_name:
                town_line += rec.l10n_mm_township_name
            if town_line:
                lines.append(town_line)
            # district + state
            district_line = ''
            if rec.l10n_mm_district_name:
                district_line += rec.l10n_mm_district_name
                if rec.state_id:
                    district_line += ', ' + rec.state_id.name
            elif rec.state_id:
                district_line += rec.state_id.name
            if district_line:
                lines.append(district_line)
            # postcode
            if rec.l10n_mm_postcode:
                lines.append(rec.l10n_mm_postcode)
            # country
            if rec.country_id:
                lines.append(rec.country_id.name)
            rec.l10n_mm_full_address = '\n'.join(lines)

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
    
    @api.depends('l10n_mm_district_id', 'state_id', 'country_id')
    def _compute_township_ids(self):
        for rec in self:
            domain = []
            if rec.l10n_mm_district_id:
                domain = [('district_id', '=', rec.l10n_mm_district_id.id)]
            elif rec.state_id:
                domain = [('state_id', '=', rec.state_id.id)]
            elif rec.country_id:
                domain = [('country_id', '=', rec.country_id.id)]
            rec.l10n_mm_township_ids = self.env['res.township'].search(domain)

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
            # Set state & country
            self.state_id = self.l10n_mm_township_id.district_id.state_id
            self.country_id = self.state_id.country_id
            self.l10n_mm_zip_id = False

            # Reset ward if it doesn't belong to this township
            if self.l10n_mm_ward_id and self.l10n_mm_ward_id.township_id != self.l10n_mm_township_id:
                self.l10n_mm_ward_id = False
                self.l10n_mm_postalcode = False
                self.l10n_mm_pcode = False

            # Reset town if it doesn't belong to township
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
            

    # def _address_fields(self):
    #     fields_list = super()._address_fields()
    #     return fields_list + ['l10n_mm_district_id', 'l10n_mm_township_id', 'l10n_mm_town_id', 'l10n_mm_ward_id']

    @api.model
    def _formatting_address_fields(self):
        return super()._formatting_address_fields() + [
            'l10n_mm_full_address',
        ]

    # def _display_address_depends(self):
    #     return super()._display_address_depends() + [
    #         'l10n_mm_district_id',
    #         'l10n_mm_township_id',
    #         'l10n_mm_town_id',
    #         'l10n_mm_ward_id',
    #         'l10n_mm_postcode',
    #     ]