
from odoo import models, fields, api

class StudentDetailes(models.Model):
    _inherit = 'student.student'

    marks3 = fields.Char(string="Marks3")
    marks4 = fields.Char(string="Marks4")
    extra_marks_show = fields.Boolean(string="Extra")