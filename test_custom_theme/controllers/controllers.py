# -*- coding: utf-8 -*-
# from odoo import http


# class ../../hsplTraining/testCustomTheme(http.Controller):
#     @http.route('/../../hspl_training/test_custom_theme/../../hspl_training/test_custom_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../hspl_training/test_custom_theme/../../hspl_training/test_custom_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../hspl_training/test_custom_theme.listing', {
#             'root': '/../../hspl_training/test_custom_theme/../../hspl_training/test_custom_theme',
#             'objects': http.request.env['../../hspl_training/test_custom_theme.../../hspl_training/test_custom_theme'].search([]),
#         })

#     @http.route('/../../hspl_training/test_custom_theme/../../hspl_training/test_custom_theme/objects/<model("../../hspl_training/test_custom_theme.../../hspl_training/test_custom_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../hspl_training/test_custom_theme.object', {
#             'object': obj
#         })
