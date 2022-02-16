# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_transfer = fields.Boolean(
        string="Is transfer",
        related="picking_type_id.is_transfer")


    @api.onchange('is_transfer','picking_type_id')
    def transfer_domain(self):
        for record in self:
            if record.location_dest_id and record.is_transfer:
                locations = self.env['stock.location'].search([('is_transfer','=', record.is_transfer)])
                logging.info("?????????????????")
                logging.info(locations)
                return {'domain': {'location_dest_id': [('is_transfer', '=', locations.is_transfer)]}}
