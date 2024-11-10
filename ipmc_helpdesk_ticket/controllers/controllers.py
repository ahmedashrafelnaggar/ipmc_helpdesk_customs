# -*- coding: utf-8 -*-
# from odoo import http


# class IpmcHelpdeskTicket(http.Controller):
#     @http.route('/ipmc_helpdesk_ticket/ipmc_helpdesk_ticket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipmc_helpdesk_ticket/ipmc_helpdesk_ticket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipmc_helpdesk_ticket.listing', {
#             'root': '/ipmc_helpdesk_ticket/ipmc_helpdesk_ticket',
#             'objects': http.request.env['ipmc_helpdesk_ticket.ipmc_helpdesk_ticket'].search([]),
#         })

#     @http.route('/ipmc_helpdesk_ticket/ipmc_helpdesk_ticket/objects/<model("ipmc_helpdesk_ticket.ipmc_helpdesk_ticket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipmc_helpdesk_ticket.object', {
#             'object': obj
#         })
