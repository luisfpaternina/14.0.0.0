# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_transfer = fields.Boolean(
        string="Is transfer",
        related="picking_type_id.is_transfer")
