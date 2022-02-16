# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking.type'

    is_transfer = fields.Boolean(
        string="Is transfer")
    res_groups_id = fields.Many2one(
        'res.groups',
        string="Groups")
    check_user = fields.Boolean(
        string='user',
        compute='_compute_user_check',
        default=False,
        store=True)


    @api.depends('name')
    def _compute_user_check(self):
        if self.env.user.has_group('base.user_admin'):
            self.check_user = True
        else:
            self.check_user = False
