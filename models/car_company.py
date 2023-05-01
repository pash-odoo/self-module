from odoo import fields,models

class CarCompany(models.Model):
    _name="car.company"
    _description="data related to company of car"

    name=fields.Char()