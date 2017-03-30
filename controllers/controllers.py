# -*- coding: utf-8 -*-
from odoo import http

# class OdooWger(http.Controller):
#     @http.route('/odoo_wger/odoo_wger/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_wger/odoo_wger/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_wger.listing', {
#             'root': '/odoo_wger/odoo_wger',
#             'objects': http.request.env['odoo_wger.odoo_wger'].search([]),
#         })

#     @http.route('/odoo_wger/odoo_wger/objects/<model("odoo_wger.odoo_wger"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_wger.object', {
#             'object': obj
#         })