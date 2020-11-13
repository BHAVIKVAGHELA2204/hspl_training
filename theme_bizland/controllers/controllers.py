# -*- coding: utf-8 -*-
# from odoo import http


# class ../../hsplTraining/themeBizland(http.Controller):
#     @http.route('/../../hspl_training/theme_bizland/../../hspl_training/theme_bizland/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../hspl_training/theme_bizland/../../hspl_training/theme_bizland/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../hspl_training/theme_bizland.listing', {
#             'root': '/../../hspl_training/theme_bizland/../../hspl_training/theme_bizland',
#             'objects': http.request.env['../../hspl_training/theme_bizland.../../hspl_training/theme_bizland'].search([]),
#         })

#     @http.route('/../../hspl_training/theme_bizland/../../hspl_training/theme_bizland/objects/<model("../../hspl_training/theme_bizland.../../hspl_training/theme_bizland"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../hspl_training/theme_bizland.object', {
#             'object': obj
#         })
