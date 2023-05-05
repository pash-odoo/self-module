from odoo import fields,models

class CarCompany(models.Model):
    _name="car.company"
    _description="data related to company of car"

    name=fields.Char()

    _sql_constraints=[('check_company_name','unique(name)','please enter unique car name')]