# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
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


    @api.constrains('percentaje_mto', 'percentaje_rep')
    def _validate_has_account(self):
        for record in self:
            if record.has_account:
                raise ValidationError(_(
                    'Validate potencial client has account!'))
