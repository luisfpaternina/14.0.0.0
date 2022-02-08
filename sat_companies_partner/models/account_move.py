# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_potential_client = fields.Boolean(
        string="Is a potential client")
    is_validate = fields.Boolean(
        string="Validate")
    has_account = fields.Boolean(
        string="Has a account",
        related="partner_id.has_account")
