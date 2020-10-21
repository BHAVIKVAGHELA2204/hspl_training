from odoo import fields, models


class Book(models.Model):
    _name = "student.book"
    _description = "Book Table"
    _rec_name = "author"

    name = fields.Char(string="Book", required=True)
    author = fields.Char(string="Author Name")
