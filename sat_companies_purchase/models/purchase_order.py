from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_type_id = fields.Many2one(
        'purchase.order.type',
        string="Purchase order type")
