from odoo import models, fields, api

class Product(models.Model):
    _name = 'demo_website.product'

    name = fields.Char()
    teacher_id = fields.Many2one('demo_website.teachers', string="Teacher")