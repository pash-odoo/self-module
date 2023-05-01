from odoo import fields,models

class Employee(models.Model):
    _name="employee"
    _description="data related to Employee"

    name=fields.Char(required=True)
    phone=fields.Char(required=True)
    email=fields.Char()
    Experience=fields.Integer(required=True)
    
