from odoo import fields,models

class ResUser(models.Model):
    _inherit = "res.users"

    car_appointment=fields.One2many("car.repair","employee_name")