# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    total_cost = fields.Float(
        string="Total",
        compute="_compute_total")

    @api.depends('product_id')
    def _compute_total(self):
        for record in self:
            if record.product_id:
                record.total_cost = record.product_qty * record.product_id.standard_price
            else:
                record.total_cost = 0.0
