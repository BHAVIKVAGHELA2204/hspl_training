# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'demo_website.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('demo_website.courses', 'teacher_id', string="Courses")