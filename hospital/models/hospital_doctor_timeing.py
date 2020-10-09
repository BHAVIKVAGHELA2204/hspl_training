from odoo import fields, models

class hospitalDoctorTimeing(models.Model):
    _name = "hospital.doctor.timeing"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Timeing Table"

    name = fields.Char(string="Name")
    from_time = fields.Integer(string="From Time")
    to_time = fields.Integer(strinng="To Time")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    doctor_ids = fields.Many2many('hospital.doctor', string="Doctor")