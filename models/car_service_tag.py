from odoo import fields,models

class CarServiceTag(models.Model):
    _name="car.service.tag"
    _description="add tags for car priority"

    name=fields.Char(required=True,string="Name")
    price=fields.Float(string="Price")

    _sql_constraints=[('check_tag_name','unique(name)','please create tag with unique name')]