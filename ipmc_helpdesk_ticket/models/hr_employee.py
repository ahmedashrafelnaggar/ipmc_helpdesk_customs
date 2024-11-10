from odoo import api, fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    certificate_id = fields.Many2one('ipmc.certificates', string="Certificate",help="The certificate associated with this degree")






