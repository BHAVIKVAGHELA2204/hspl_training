from odoo import models, fields, api

class Courses(models.Model):
    _name = 'demo_website.courses'

    name = fields.Char()
    teacher_id = fields.Many2one('demo_website.teachers', string="Teacher")