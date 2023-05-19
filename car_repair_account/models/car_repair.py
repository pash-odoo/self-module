from odoo import fields,models,Command

class CarRepair(models.Model):
    _inherit="car.repair"

    def done_appointment(self):
        self.env["account.move"].create({
            "partner_id":self.customer_name.id,
            "move_type":'out_invoice',
            "invoice_line_ids":[
                Command.create({
                        "name":i.name,
                        # "quantity":1,
                        "price_unit":i.price
                    }) for i in self.service_ids]
        })
        return super().done_appointment()