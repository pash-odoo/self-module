from odoo import fields,models

class Service(models.Model):
    _name="service"
    _description="data related to available services and it's price"
    _order="price desc"

    name=fields.Char()
    price=fields.Float()

    _sql_constraints=[('check_service_name','unique(name)','please enter unique service name'),('check_price_service','check(price>0)','Please make price more than 0')]
    