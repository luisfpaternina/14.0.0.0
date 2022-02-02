from signal import valid_signals
from odoo import models, fields, api
from datetime import tzinfo, timedelta, datetime

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    sale_type_origin_id = fields.Many2one('sale.order.type','Sale Type Origin')
    sale_order_id = fields.Many2one('sale.order', 'Sale Order')
    start_date_project = fields.Datetime('Start date project')


    def update_fields_service_dates(self):
        for record in self:
            dates_beging = [x.planned_date_begin for x in record.task_ids]
            date_min = min(dates_beging)
            diff_dates =record.start_date_project - date_min
            for task in record.task_ids:
                if date_min == task.planned_date_begin:
                    task.planned_date_begin = record.start_date_project
                    task.planned_date_end = task.planned_date_end + timedelta(days=diff_dates.days)
                else:
                    task.planned_date_begin = task.planned_date_begin + timedelta(days=diff_dates.days)
                    task.planned_date_end = task.planned_date_end + timedelta(days=diff_dates.days)
    
    def write(self,vals):
        update_dates = False
        if 'start_date_project' in vals:
            update_dates = True
        res = super(ProjectProject, self).write(vals)
        for record in self:
            if update_dates == True:
                record.update_fields_service_dates()

        return res