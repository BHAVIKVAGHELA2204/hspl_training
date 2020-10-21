from odoo import models, fields, api, _

class StudentSubject(models.Model):
    _name = "subject.subject"
    _description = "subject Table"

    name = fields.Char(string="Subject Name")
    code = fields.Char(string="subject Code")

    _sql_constraints = [("name_unique", "UNIQUE(name)", "Field Name must be unique")]