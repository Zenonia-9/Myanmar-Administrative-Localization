from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestResPartnerAddressImport(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Partner = cls.env['res.partner']
        cls.Township = cls.env['res.township']
        cls.Ward = cls.env['res.ward']
        cls.township = cls.Township.search([('code', '=', 'MMR001001')], limit=1)
        cls.ward = cls.Ward.search([('p_code', '=', 'MMR001001001')], limit=1)
        cls.unique_ward = next(
            ward for ward in cls.Ward.search([], limit=100)
            if cls.Ward.search_count([('name', '=', ward.name)]) == 1
        )

    def _load(self, fields, rows):
        return self.Partner.with_context(import_file=True).load(fields, rows)

    def test_import_township_by_name_and_code(self):
        for value in (self.township.name, self.township.code):
            result = self._load(
                ['name', 'l10n_mm_township_id'],
                [[f'Import Township {value}', value]],
            )
            self.assertFalse(result['messages'])
            partner = self.Partner.browse(result['ids'])
            self.assertEqual(partner.l10n_mm_township_id, self.township)
            self.assertEqual(partner.l10n_mm_district_id, self.township.district_id)
            self.assertEqual(partner.state_id, self.township.state_id)
            self.assertEqual(partner.l10n_mm_region, self.township.state_id.l10n_mm_region)
            self.assertEqual(partner.country_id, self.township.country_id)

    def test_import_ward_by_name_and_pcode(self):
        for value in (self.unique_ward.name, self.unique_ward.p_code):
            result = self._load(
                ['name', 'l10n_mm_ward_id'],
                [[f'Import Ward {value}', value]],
            )
            self.assertFalse(result['messages'])
            partner = self.Partner.browse(result['ids'])
            self.assertEqual(partner.l10n_mm_ward_id, self.unique_ward)
            self.assertEqual(partner.l10n_mm_township_id, self.unique_ward.township_id)
            self.assertEqual(partner.l10n_mm_district_id, self.unique_ward.district_id)
            self.assertEqual(partner.state_id, self.unique_ward.state_id)
            self.assertEqual(partner.l10n_mm_region, self.unique_ward.state_id.l10n_mm_region)
            self.assertEqual(partner.country_id, self.unique_ward.country_id)
            self.assertEqual(partner.l10n_mm_pcode, self.unique_ward.p_code)
            self.assertEqual(partner.l10n_mm_postalcode, self.unique_ward.postal_code)

    def test_import_pcode_fills_ward(self):
        result = self._load(
            ['name', 'l10n_mm_pcode'],
            [['Import P-Code', self.unique_ward.p_code]],
        )
        self.assertFalse(result['messages'])
        partner = self.Partner.browse(result['ids'])
        self.assertEqual(partner.l10n_mm_pcode, self.unique_ward.p_code)
        self.assertEqual(partner.l10n_mm_ward_id, self.unique_ward)
        self.assertEqual(partner.l10n_mm_township_id, self.unique_ward.township_id)
        self.assertEqual(partner.state_id, self.unique_ward.state_id)

    def test_import_rejects_conflicting_township_and_ward(self):
        other_ward = self.Ward.search(
            [('township_id', '!=', self.ward.township_id.id)], limit=1
        )
        result = self._load(
            ['name', 'l10n_mm_township_id', 'l10n_mm_ward_id'],
            [['Conflicting hierarchy', self.township.code, other_ward.p_code]],
        )
        self.assertFalse(result['ids'])
        self.assertTrue(result['messages'])

    def test_import_rejects_ambiguous_township_name(self):
        district = self.township.district_id
        self.Township.create([
            {
                'name': 'Ambiguous Import Township',
                'code': 'TST000001',
                'district_id': district.id,
            },
            {
                'name': 'Ambiguous Import Township',
                'code': 'TST000002',
                'district_id': district.id,
            },
        ])
        with self.assertRaises(ValidationError):
            self.Township.with_context(import_file=True).name_search(
                name='Ambiguous Import Township', operator='='
            )

    def test_import_updates_existing_partner(self):
        partner = self.Partner.create({'name': 'Import Update Target'})
        self.env['ir.model.data'].create({
            'module': 'test_l10n_mm_address',
            'name': 'import_update_target',
            'model': 'res.partner',
            'res_id': partner.id,
        })
        result = self._load(
            ['id', 'l10n_mm_township_id'],
            [['test_l10n_mm_address.import_update_target', self.township.code]],
        )
        self.assertFalse(result['messages'])
        partner.invalidate_recordset()
        self.assertEqual(partner.l10n_mm_township_id, self.township)
        self.assertEqual(partner.state_id, self.township.state_id)
