# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_transfer = fields.Boolean(
        string="Is transfer",
        related="picking_type_id.is_transfer")


    @api.onchange('is_transfer')
    def transfer_domain(self):
        for record in self:
            if record.location_dest_id and record.is_transfer:
                locations = self.env['stock.location'].search([('is_transfer','=', record.is_transfer)])
                return {'domain': {'location_dest_id': [('id', 'in', locations)]}}
