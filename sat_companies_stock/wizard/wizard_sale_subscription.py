from odoo import models, fields, api
import logging
from odoo.exceptions import ValidationError

class WizardSaleSubscription(models.TransientModel):
    _name = 'wizard.sale.subscription'

    name = fields.Char('')
    subscription_id = fields.Many2one('sale.subscription')

    def accept_task_type_sale_subscription(self):
        for record in self.subscription_id:    
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
            print('test')
            if record.recurring_invoice_line_ids:
                for line in record.recurring_invoice_line_ids.order_line:
                    line.task_id = new_task.id

    def start_subscription_wizard(self):
        for record in self:
            record.subscription_id.start_subscription()