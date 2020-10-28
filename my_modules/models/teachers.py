from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'my_modules.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('my_modules.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
    _name = 'my_modules.courses'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('my_modules.teachers', string="Teacher")
