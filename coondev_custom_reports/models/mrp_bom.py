# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    total_cost = fields.Float(
        string="Total")
