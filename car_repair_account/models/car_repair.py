from odoo import fields,models,Command

class CarRepair(models.Model):
    _inherit="car.repair"

    def done_appointment(self):
        lst = []
        for i in self.service_ids:
            lst.append(Command.create({
                        "name":i.name,
                        # "quantity":1,
                        "price_unit":i.price
                    }))

        lst.append(Command.create({
                    "name":"service Charges",
                    "price_unit":self.tag_ids.price
                }))


        self.env["account.move"].create({
            "partner_id":self.customer_name.id,
            "move_type":'out_invoice',
            "invoice_line_ids":lst

                
        })
        return super().done_appointment()