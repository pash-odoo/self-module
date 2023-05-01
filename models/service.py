from odoo import fields,models

class Service(models.Model):
    _name="service"
    _description="data related to available services and it's price"

    name=fields.Char()
    price=fields.Float()
    