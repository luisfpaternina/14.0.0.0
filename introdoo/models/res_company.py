
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResCompany(models.Model):
    _inherit = 'res.company'

    terms = fields.Text(string="Terminos y condiciones")
    test = fields.Char(string="Test")
    phone = fields.Char(string="Phone")
    company_line_ids = fields.One2many(
        'res.company.line',
        'company_id',
        string="Company lines")

    @api.constrains('company_line_ids')
    def _exist_record_in_lines(self):
        for record in self:
            exis_record_lines = []
            for line in record.company_line_ids:
                if line.partner_id.id in exis_record_lines:
                    raise ValidationError('No se puede repetir el registro')
                exis_record_lines.append(line.partner_id.id)
