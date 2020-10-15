from odoo import fields, models

class Subject(models.Model):
    _name = "student.subject"
    _description = "subject Table"

    name = fields.Char(string="Subject", required=True)
    sub_code = fields.Char(string="Subject Code")