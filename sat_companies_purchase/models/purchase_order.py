from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_type_id = fields.Many2one(
        'purchase.order.type',
        string="Purchase order type")
