# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, date
import logging

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_external = fields.Boolean(
        string="Is external",
        tracking=True,
        compute="_compute_is_external")
    sale_type_id = fields.Many2one(
        'sale.order.type',
        string="Sale type",
        tracking=True)
    oportunity_type_id = fields.Many2one(
        'crm.lead.type',
        string="Oportunity type")
    client_type = fields.Selection(
        [('neighborhood_community','Neighborhood community'),
        ('companies','Companies/builders'),
        ('public_organisms','Public organisms'),
        ('family_home','Single-family private homes')],string="Client type")
    managed_by = fields.Selection([
        ('president','President'),
        ('admin','Administrator')],string="Managed by")
    is_medium_website = fields.Boolean(
        string="Website medium",
        compute="_compute_check_medium_id")
    is_medium_email = fields.Boolean(
        string="Email medium",
        compute="_compute_check_email_medium_id")
    partner_admin_id = fields.Many2one(
        'res.partner',
        string="Farm administrator")
    quote_date_sent_min = fields.Date(
        string="Quote date sent min",
        compute="_compute_quote_date_sent_min")
    opportunity_days = fields.Integer(
        string="Opportunity days",
        compute="_calculated_days")


    @api.depends('medium_id')
    def _compute_check_medium_id(self):
        for record in self:
            record.is_medium_website = True if record.medium_id and record.medium_id[0].name  == 'Website' else False


    @api.depends('medium_id')
    def _compute_check_email_medium_id(self):
        for record in self:
            record.is_medium_email = True if record.medium_id and record.medium_id[0].name  == 'Email' else False


    @api.depends('medium_id')
    def _compute_is_external(self):
        for record in self:
            if record.is_medium_email == True or record.is_medium_website == True:
                record.is_external = True
            else:
                record.is_external = False


    def _compute_quote_date_sent_min(self):
        for record in self:
            dt_orders = []
            min_date = False
            for line in record.order_ids:
                dt_orders.append(line.quote_date_sent)
            if dt_orders:
                min_date = min(dt_orders)
            
            record.quote_date_sent_min = min_date


    @api.depends('quote_date_sent_min')
    def _calculated_days(self):
        for record in self:
            if record.quote_date_sent_min:
                record.opportunity_days = (record.quote_date_sent_min - date.today()).days
            else:
                record.quote_date_sent_min = False
