from odoo import api, fields, models

class IpmcQualifications(models.Model):
    _description = "Qualifications for Applicants"
    _inherit = 'hr.recruitment.degree'

    certificate_id = fields.Many2one('ipmc.certificates', string="Certificate",help="The certificate associated with this degree")
