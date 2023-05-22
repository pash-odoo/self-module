from odoo import fields,models,api
from datetime import datetime,date
from odoo.exceptions import UserError,ValidationError

class CarRepair(models.Model):
    _name="car.repair"
    _description="data related to car repair appointment"
    _order="expected_date"
    _inherit = ['mail.thread','mail.activity.mixin']

    name=fields.Char(required=True,string="Name",tracking=True)
    notes=fields.Text()


    expected_date=fields.Date(copy=False,string="Expected Date",tracking=True,required=True)

    #compute field
    cost=fields.Float(string="Expected Cost",compute="_compute_cost")
    remaining_days=fields.Integer(string="Remaining Days",compute="_compute_days")
    
    #customer and car Details
    # customer_name=fields.Char(required=True,string="Customer Name")
    # customer_phone=fields.Char(required=True,string="Customer Phone")
    # customer_email=fields.Char(string="Customer Email")

    customer_name=fields.Many2one("res.partner",required=True,string="Customer Name")
    customer_phone=fields.Char(related="customer_name.phone",string="Customer Phone")
    customer_email=fields.Char(related="customer_name.email",string="Customer Email")
    car_name = fields.Char(string="Car Name")
    vehicle_number=fields.Char(required=True,string="Vehicle Number")

    #many2one
    car_company=fields.Many2one("car.company",string="company")
    tag_ids = fields.Many2one("car.service.tag",string="tags",required=True)

    #worker detail
    employee_name=fields.Many2one("res.users")
    employee_email=fields.Char(related="employee_name.email",string="Mechanic Email")
    employee_phone=fields.Char(related="employee_name.phone",string="Mechanic Phone")

    #many2many
    service_ids=fields.Many2many("service",string="Service")

    state=fields.Selection(
        string="state",
        selection=[('new','New'),('work Started','Work Started'),('done','Done'),('canceled','Canceled')],
        copy=False,
        default='new',
        tracking=True
    )

    tag_description=fields.Char(compute="_find_description")
    

    @api.depends("service_ids.price","tag_ids.name")
    def _compute_cost(self):
        if(self and self.mapped("service_ids.price")):
            self.cost=sum(self.mapped("service_ids.price"))+self.tag_ids.price

        else:
            self.cost=0

    @api.depends("expected_date")
    def _compute_days(self):
        # if(self and self.expected_date):
        #     self.remaining_days=(self.expected_date-date.today()).days
        # else:
        #     self.remaining_days=0
        for record in self:
            if record and record.expected_date:
                record.remaining_days=(record.expected_date-date.today()).days
            else:
                record.remaining_days=0

    
    # compute value for finding desciption of tags
    @api.depends("tag_ids.description")
    def _find_description(self):
        if self and self.tag_ids.name:
            self.tag_description=self.tag_ids.description
        else:
            self.tag_description=""

    #button

    def cancel_appointment(self):
        if (self.state not in ['work Started','done']) and (self.expected_date-date.today()).days>1:
            self.state='canceled'
        else:
            raise UserError("You Can not cancel appointment if work is done or repair going on or delivery date is less then 2 days")
        
    def done_appointment(self):
        self.state='done'
    
    def start_appointment(self):
        self.state='work Started'
    

    @api.constrains('expected_date')
    def _check_date(self):
        if self.expected_date< date.today():
            raise ValidationError("Please select valid date!")

    @api.constrains('customer_phone')
    def _check_phone_number(self):
        if len(self.customer_phone)!=10 or not self.customer_phone.isnumeric():
            raise ValidationError('please Enter Valid Phone Number')

    @api.constrains('service_ids')
    def _check_service_select(self):
        if not self.service_ids:
            raise ValidationError('please select atleast one services')

    
    # on delete (python inheritance)
    @api.ondelete(at_uninstall=False)
    def _unlink_if_state(self):
        for record in self:
            if record.state not in ['new','canceled']:
                raise UserError("Appointment can not be deleted if work is started or done!")


