from odoo import fields, models

class StudentSubject(models.Model):
    _name = "student.subject.lines"
    _description = "student subject lines Table"

    name = fields.Char(string="student subject lines", required=True)
    subject_id = fields.Many2one('student.subject', string="Subject")
    student_id = fields.Many2one('student.student', strint="student")

