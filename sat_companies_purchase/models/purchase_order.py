from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_type_id = fields.Many2one(
        'purchase.order.type',
        string="Purchase order type",
        tracking=True)
    is_validate_reception = fields.Boolean(
        string="Validate reception",
        tracking=True)


    @api.onchange('date_planned')
    def _onchange_date_planned(self):
        now = datetime.now()
        for record in self:
            record.is_validate_reception = False
            if record.date_planned:
                if record.date_planned >= now:
                    record.is_validate_reception = True
