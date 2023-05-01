from odoo import fields,models,api

class CarRepair(models.Model):
    _name="car.repair"
    _description="data related to car repair appointment"

    name=fields.Char(required=True,string="Name")
    notes=fields.Text()


    expected_date=fields.Date(copy=False,string="Expected Date")

    #compute field
    cost=fields.Float(string="Expected Cost",compute="_compute_cost")
    
    #customer and car Details
    customer_name=fields.Char(required=True,string="Customer Name")
    customer_phone=fields.Char(required=True,string="Customer Phone")
    customer_email=fields.Char(string="Customer Email")
    car_name = fields.Char(string="Car Name")
    vehicle_number=fields.Char(required=True,string="Vehicle Number")

    #many2one
    car_company=fields.Many2one("car.company",string="company")

    #worker detail
    employee_name=fields.Many2one("res.users")
    employee_email=fields.Char(related="employee_name.email",string="Mechanic Email")
    employee_phone=fields.Char(related="employee_name.phone",string="Mechanic Phone")

    #many2many
    tag_ids = fields.Many2many("car.service.tag",string="tags")
    service_ids=fields.Many2many("service",string="Service")

    state=fields.Selection(
        string="state",
        selection=[('new','New'),('work Started','Work Started'),('done','Done'),('canceled','Canceled')],
        copy=False,
        default='new'
    )
    

    @api.depends("service_ids.price")
    def _compute_cost(self):
        if(self and self.mapped("service_ids.price")):
            self.cost=sum(self.mapped("service_ids.price"))
        else:
            self.cost=0
