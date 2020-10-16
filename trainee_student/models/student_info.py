from odoo import fields, models, api, _


class Student(models.Model):
    _name = "student.student"
    _description = "student Table"

    name = fields.Char(string="student", required=True)
    roll_no = fields.Integer(string="Roll No")
    std_class = fields.Char(strint="Class")
    subject_line_ids = fields.One2many("student.subject.lines", "student_id", string="Student Subject Lines")
    book_line_ids = fields.One2many("student.book.lines", "student_id", string="Student Book Lines")
    admission_date = fields.Date("Admission Date")
    marks1 = fields.Integer(string="Marks 1")
    marks2 = fields.Integer(string="Marks 2")
    res_total = fields.Integer(string="Total", compute="compute_total_of_marks", store=True)
    res_per = fields.Char(string="Percentage", compute="compute_per_of_student", store=True)

    # @api.model
    # def create(self, vals):
    #     # print ("bhavik :" , vals)
    #     vals.update({"name" : vals.get("name")+" 123"})
    #     # print("new val: ", vals)
    #     res = super(Student, self).create(vals)
    #     # print("val 1 : ", res)
    #     # print("value", res.roll_no, "Name :" + res.name + " vaghela")
    #     return res
    #
    # def write(self, vals):
    #     print("test :", self, vals)
    #     res = super(Student, self).write(vals)
    #     print("=====", res)
    #     return res

    @api.model
    def create(self, vals):
        vals.update({"name": vals.get("name") + " vaghela"})
        res = super(Student, self).create(vals)
        return res

    # def write(self, vals):
    #     # print("test :", self, vals)
    #     if vals.get("name"):
    #         vals.update({"name": vals.get("name") + " 123"})
    #     res = super(Student, self).write(vals)
    #     # print("test :", self, vals)
    #     return res

    @api.depends('marks1', 'marks2')
    def compute_total_of_marks(self):
        for rec in self:
            # if rec.marks1 and rec.marks2:
            rec.res_total = rec.marks1 + rec.marks2
            # else:
            #     rec.res_total = 0

    @api.depends('res_total')
    def compute_per_of_student(self):
        for rec in self:
            rec.res_per = str((rec.res_total * 100) / 200) + "%"

