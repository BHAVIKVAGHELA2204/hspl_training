from odoo import fields, models, api

class Student(models.Model):
    _name = "student.student"
    _description = "student Table"

    name = fields.Char(string="student", required=True)
    roll_no = fields.Integer(string="Roll No")
    std_class = fields.Char(strint="Class")

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
        vals.update({"name" : vals.get("name")+" vaghela"})
        res = super(Student, self).create(vals)
        return res

    def write(self, vals):
        print("test :", self, vals)
        vals.update({"name": vals.get("name") + " 123"})
        res = super(Student, self).write(vals)
        print("test :", self, vals)
        return res
