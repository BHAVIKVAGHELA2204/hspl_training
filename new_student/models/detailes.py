
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class StudentDetailes(models.Model):
    _inherit = 'student.student'

    marks3 = fields.Integer(string="Marks3")
    marks4 = fields.Integer(string="Marks4")
    subject_id = fields.Many2one('subject.subject', string="subject")
    selected_value = fields.Char(string="Selected Value", readonly=True)
    extra_marks_show = fields.Boolean(string="Extra Field")

    @api.constrains('marks3', 'marks4')
    def _check_marks(self):
        for rec in self:
            if rec.marks3 > 20 and rec.marks4 < 30:
                raise UserError(_('Please Enter min 20 and marks 4 max 30.'))

    @api.onchange("subject_id")
    def _onchange_subject_id(self):
        if self.subject_id:
            if self.subject_id.id == 1:
                self.selected_value = "Maths"
            elif self.subject_id.id == 2:
                self.selected_value = "Science"
            elif self.subject_id.id == 3:
                self.selected_value = "SS"
            elif self.subject_id.id == 4:
                self.selected_value = "Computer"
            else:
                self.selected_value = "test"
