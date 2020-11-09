# -*- coding: utf-8 -*-
# from odoo import http


# class ../../hsplTraining/welcomeToBizland(http.Controller):
#     @http.route('/../../hspl_training/welcome_to_bizland/../../hspl_training/welcome_to_bizland/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../hspl_training/welcome_to_bizland/../../hspl_training/welcome_to_bizland/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../hspl_training/welcome_to_bizland.listing', {
#             'root': '/../../hspl_training/welcome_to_bizland/../../hspl_training/welcome_to_bizland',
#             'objects': http.request.env['../../hspl_training/welcome_to_bizland.../../hspl_training/welcome_to_bizland'].search([]),
#         })

#     @http.route('/../../hspl_training/welcome_to_bizland/../../hspl_training/welcome_to_bizland/objects/<model("../../hspl_training/welcome_to_bizland.../../hspl_training/welcome_to_bizland"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../hspl_training/welcome_to_bizland.object', {
#             'object': obj
#         })
