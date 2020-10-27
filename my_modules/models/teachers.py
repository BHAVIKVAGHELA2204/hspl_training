from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'my_modules.teachers'

    name = fields.Char()
    biography = fields.Html()
