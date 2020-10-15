# -*- coding: utf-8 -*-
# from odoo import http


# class ../../hsplTraining/ecommerce(http.Controller):
#     @http.route('/../../hspl_training/ecommerce/../../hspl_training/ecommerce/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../hspl_training/ecommerce/../../hspl_training/ecommerce/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../hspl_training/ecommerce.listing', {
#             'root': '/../../hspl_training/ecommerce/../../hspl_training/ecommerce',
#             'objects': http.request.env['../../hspl_training/ecommerce.../../hspl_training/ecommerce'].search([]),
#         })

#     @http.route('/../../hspl_training/ecommerce/../../hspl_training/ecommerce/objects/<model("../../hspl_training/ecommerce.../../hspl_training/ecommerce"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../hspl_training/ecommerce.object', {
#             'object': obj
#         })
