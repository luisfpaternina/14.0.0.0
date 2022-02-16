# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import base64
from io import BytesIO
import qrcode
import logging

class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    gadget_contract_type = fields.Many2one(
        'stock.gadgets.contract.type',
        string="Contract type")
    is_potential_client = fields.Boolean(
        string="Is a potential client",
        tracking=True,
        related="partner_id.is_potential_client")
    
    product_id = fields.Many2one('product.template', 'Gadgets')
    task_user_id = fields.Many2one('res.users')
    sale_type_id = fields.Many2one('sale.order.type')
    gadgest_contract_type_id = fields.Many2one('stock.gadgets.contract.type')
    date_begin = fields.Datetime(string = 'Date asigned')
    date_end = fields.Datetime(string = 'Date End asingned')

    check_contract_type = fields.Boolean(
        compute="_compute_check_contract_type",
        )

    """
    _sql_constraints = [
        (
            'client_code_uniq',
            'check(1=1)',
            'The client code is unique!'
        )
    ]
    """

    def set_wizard_sale_subscription(self):
        for record in self:
            order_type_form = record.env.ref('sat_companies_stock.wizard_wizard_sale_subscription_form',raise_if_not_found=False)
            ctx = dict(
                    default_name = str('Nombre Tarea Servicio Externo'),
                    default_model='wizard.sale.subscription',
                    default_subscription_id=record.id,
                    )
            return {
                    'name': ('Generar Tarea Servicio Externo'),
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'wizard.sale.subscription',
                    'views': [(order_type_form.id, 'form')],
                    'view_id': order_type_form.id,
                    'context': ctx,
                    'target': 'new',
                    }
    """
    def start_subscription(self):
        res = super(SaleSubscription, self).start_subscription()
        for record in self:
            project_fsm = self.env.ref('industry_fsm.fsm_project', raise_if_not_found=False)

            new_task = self.env['project.task'].create({
                'name': 'GENERADO DESDE SUBSCRIPTION',
                'partner_id': record.partner_id.id,
                'ot_type_id': record.gadgest_contract_type_id.id,
                'project_id': project_fsm.id,
                'user_id': record.task_user_id.id,
                'product_id': record.product_id.id,
                'planned_date_begin': record.date_begin, 
                'planned_date_end': record.date_end,
                'is_fsm': True
                
            })
            if record.recurring_invoice_line_ids:
                for line in record.recurring_invoice_line_ids.order_line:
                    line.task_id = new_task.id
        return res
    """
    @api.onchange('product_id')
    def onchange_check_product(self):
        for record in self:
            if record.product_id.employee_notice_id.user_id:
                record.task_user_id = record.product_id.employee_notice_id.user_id
            sale_type = record.product_id.subscription_template_id.sale_type_id
            gadgets_contract = record.product_id.subscription_template_id.gadgets_contract_type_id
            record.sale_type_id = sale_type
            record.gadgest_contract_type_id = gadgets_contract

    @api.depends('sale_type_id')
    def _compute_check_contract_type(self):
        for record in self:
            record.type_contract = False
            if record.sale_type_id.code == '01':
                record.check_contract_type = True
            else:
                record.check_contract_type = False

    @api.constrains('partner_id')
    def _validate_is_potential_client(self):
        for record in self:
            if record.is_potential_client:
                raise ValidationError(_(
                    'Validate potential client in partner'))
