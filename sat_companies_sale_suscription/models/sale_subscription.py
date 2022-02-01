# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from pytz import timezone

class SaleSuscriptionInherit(models.Model):
    _inherit = 'sale.subscription'

    active_cron_invoice = fields.Boolean()

    @api.onchange('team_id')
    def _onchange_team(self):
        for record in self:
            print('team')

    """
    @api.model
    def _cron_recurring_create_invoice(self):
        self.active_cron_invoice = True
        res = super(SaleSuscriptionInherit, self)._cron_recurring_create_invoice()
        return res
    """

    def _recurring_create_invoice(self):
        res = super(SaleSuscriptionInherit, self)._recurring_create_invoice()
        for record in self:
            month_exclude = False
            if record.template_id.exclude_months == True:
                if record.active_cron_invoice == True:
                    date_today = datetime.now().month
                else:
                    date_today = record.recurring_next_date.month
    
                if date_today == 1 and record.template_id.jan == True:
                    month_exclude = True
                elif date_today == 2 and record.template_id.feb == True:
                    month_exclude = True
                elif date_today == 3 and record.template_id.mar == True:
                    month_exclude = True
                elif date_today == 4 and record.template_id.apr == True:
                    month_exclude = True
                elif date_today == 5 and record.template_id.may == True:
                    month_exclude = True
                elif date_today == 6 and record.template_id.jun == True:
                    month_exclude = True
                elif date_today == 7 and record.template_id.jul == True:
                    month_exclude = True
                elif date_today == 8 and record.template_id.aug == True:
                    month_exclude = True
                elif date_today == 9 and record.template_id.sep == True:
                    month_exclude = True
                elif date_today == 10 and record.template_id.oct == True:
                    month_exclude = True
                elif date_today == 11 and record.template_id.nov == True:
                    month_exclude = True
                elif date_today == 12 and record.template_id.dec == True:
                    month_exclude = True
                
                if month_exclude == True:
                    print('test')
                    #res.amount_untaxed = 0.0
                    #res.amount_untaxed_signed = 0.0
                    res.amount_by_group = False
                    #res.amount_total = 0.0
                    total = 0
                    for line in res.invoice_line_ids:
                        total = line.price_subtotal
                    
                    free_month_product =self.env.ref(
                    'sat_companies_sale_suscription.free_month_product_service'
                    )
                    line_last_product = res.invoice_line_ids[-1]
                    vals = {
                            'invoice_line_ids': [(0, 0, {
                                'name': 'Descuento total por mes',
                                'product_id': free_month_product.id,
                                'tax_ids': line_last_product.tax_ids.ids,
                                'price_unit': -total,
                                'quantity': 1,
                                })]
                            }
                    res.write(vals)
                        #line.amount_currency = 0.0
                        #line.price_unit = 0.0
                        #line.discount = 100
                        #line.recompute_tax_line = True
                        #line._onchange_mark_recompute_taxes()
                        #line.tax_ids = False
                        #res._compute_base_line_taxes(line)

                    #res._compute_invoice_taxes_by_group()
                    #res._onchange_invoice_line_ids()
                        #break
                    #res._recompute_dynamic_lines(recompute_all_taxes=True, recompute_tax_base_amount=True)
                    #res._recompute_tax_lines(recompute_tax_base_amount=False)

            record.active_cron_invoice = False

        return res