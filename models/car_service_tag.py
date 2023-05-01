from odoo import fields,models

class CarServiceTag(models.Model):
    _name="car.service.tag"
    _description="add tags for car priority"

    name=fields.Char(required=True,string="Name")