# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    is_maintenance = fields.Boolean(
        string="Is a maintenance",
        tracking=True)
    type_contract = fields.Selection([
        ('normal','Normal'),
        ('all_risk','All risk')],string="Type of contract",tracking=True)
    type_service_id = fields.One2many(
        'sale.check.type.contract',
        'suscription_id',
        string='Type service'
        )
