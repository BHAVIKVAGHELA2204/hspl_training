from odoo import fields, models, api, _


class StudentSubject(models.Model):
    _name = "student.subject.lines"
    _description = "student subject lines Table"

    subject_id = fields.Many2one('student.subject', string="Subject")
    subject_code = fields.Char(related="subject_id.sub_code", string="Subject Code", store=True)
    student_id = fields.Many2one('student.student', strint="student")
    author = fields.Char(string="Author", readonly=True)

    @api.model
    def create(self, vals):
        vals.update({"author": "bhavik Vaghela"})
        res = super(StudentSubject, self).create(vals)
        return res

    # def write(self, vals):
    #     if vals.get("subject_id"):
    #         vals.update({"author": "Harish vispute"})
    #     res = super(StudentSubject, self).write(vals)
    #     return res


    # print(self, self.subject_id.name, self.subject_id.id)
    @api.onchange("subject_id")
    def _onchange_subject_id(self):
        if self.subject_id:
            if self.subject_id.id == 4:
                self.author = "J"
            elif self.subject_id.id == 5:
                self.author = "PY"
            elif self.subject_id.id == 6:
                self.author = "PH"
            elif self.subject_id.id == 7:
                self.author = "ASP"


