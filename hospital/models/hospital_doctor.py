from odoo import fields, models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "doctor Table"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    blood_group = fields.Char(string="Blood Group")
    address = fields.Text(string="Address")
    from_time = fields.Integer(string="From Time")
    to_time = fields.Integer(strinng="To Time")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    image = fields.Binary(string="Image")