# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import logging


class AccountMove(models.Model):
    _inherit = 'account.move'

    product_id = fields.Many2one('product.template', 'Gadgets')
    task_user_id = fields.Many2one('res.users')
    sale_type_id = fields.Many2one('sale.order.type')
    gadgest_contract_type_id = fields.Many2one('stock.gadgest.contract.type')
    date_begin = fields.Datetime(string = 'Date asigned')
    date_end = fields.Datetime(string = 'Date End asingned')
    gadget_contract_type = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Contract type")
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True,
        related="partner_id.is_potential_client")

    @api.onchange('product_id')
    def onchange_check_product(self):
        for record in self:
            if record.product_id.employee_notice_id.user_id:
                record.task_user_id = record.product_id.employee_notice_id.user_id
            sale_type = record.product_id.subscription_template_id.sale_type_id
            gadgets_contract = record.product_id.subscription_template_id.gadgets_contract_type_id
            record.sale_type_id = sale_type
            record.gadgets_contract_type_id = gadgets_contract