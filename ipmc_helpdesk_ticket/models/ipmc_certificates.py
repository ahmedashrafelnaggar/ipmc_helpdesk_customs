from odoo import api, fields, models


class IpmcCertificates(models.Model):
    _name = 'ipmc.certificates'
    _description = "Certificates for Applicants"

    name = fields.Char(string="Certificate Name", required=True, help="Name of the certificate")


