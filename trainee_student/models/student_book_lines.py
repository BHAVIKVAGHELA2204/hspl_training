from odoo import fields, models

class StudentBook(models.Model):
    _name = "student.book.lines"
    _description = "student book lines Table"

    student_id = fields.Many2one('student.student', strint="student")
    book_id = fields.Many2one('student.book', string="Book")
    book_author = fields.Char(related="book_id.author", string="Author Name", store=True)