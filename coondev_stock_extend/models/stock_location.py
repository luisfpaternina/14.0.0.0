# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockLocation(models.Model):
    _inherit = 'stock.location'

    is_transfer = fields.Boolean(
        string="Is transfer")
