from odoo import fields, models


class Book(models.Model):
    _inherit = "student.book"

    price = fields.Char(string="Price", required=True)
    bdate = fields.Date(string="Bdate")