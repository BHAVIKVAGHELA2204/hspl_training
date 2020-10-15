# -*- coding: utf-8 -*-
# from odoo import http


# class ../../hsplTraining/traineeStudent(http.Controller):
#     @http.route('/../../hspl_training/trainee_student/../../hspl_training/trainee_student/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../hspl_training/trainee_student/../../hspl_training/trainee_student/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../hspl_training/trainee_student.listing', {
#             'root': '/../../hspl_training/trainee_student/../../hspl_training/trainee_student',
#             'objects': http.request.env['../../hspl_training/trainee_student.../../hspl_training/trainee_student'].search([]),
#         })

#     @http.route('/../../hspl_training/trainee_student/../../hspl_training/trainee_student/objects/<model("../../hspl_training/trainee_student.../../hspl_training/trainee_student"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../hspl_training/trainee_student.object', {
#             'object': obj
#         })
