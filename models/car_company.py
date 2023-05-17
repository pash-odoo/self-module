from odoo import fields,models,api

class CarCompany(models.Model):
    _name="car.company"
    _description="data related to company of car"

    name=fields.Char()
    appointment=fields.One2many('car.repair','car_company')
    appointment_count=fields.Integer(compute="_compute_count_appointment",string="Appointment count")

    _sql_constraints=[('check_company_name','unique(name)','please enter unique car name')]


    @api.depends('appointment')
    def _compute_count_appointment(self):
        self.appointment_count=len(self.appointment)


    #to apply filter of car company by stat button
    def action_open_company_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name': ('appointment'),
            'res_model': 'car.repair',
            'view_type': 'list',
            'view_mode': 'list',
            'domain': [('id', 'in', self.appointment.ids)],
        }