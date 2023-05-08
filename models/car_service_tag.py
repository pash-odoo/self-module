from odoo import fields,models

class CarServiceTag(models.Model):
    _name="car.service.tag"
    _description="add tags for car priority"
    _order="price desc"

    name=fields.Char(required=True,string="Name")
    description=fields.Char()
    price=fields.Float(string="Price")

    _sql_constraints=[('check_tag_name','unique(name)','please create tag with unique name')]