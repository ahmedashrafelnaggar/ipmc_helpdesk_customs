from odoo import api, fields, models



class helpdesk_ticket(models.Model):
    _inherit = 'helpdesk.ticket'
    _description = "Helpdesk ticket"



    description = fields.Html(string="Description")
