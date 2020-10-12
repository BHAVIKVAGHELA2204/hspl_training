from odoo import fields, models, api, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Table"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
    contact = fields.Char(string="Contact", required=True)
    blood_group = fields.Char(string="Blood Group")
    address = fields.Text(string="Address")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    m_status = fields.Selection([
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
    ], string='Marital status', default='unmarried')
    image = fields.Binary(string="Image")
    state = fields.Selection([
        ('new', 'New'),
        ('old', 'Old'),
    ], string='Status', copy=False, default='new')

    def act_move_old(self):
        for rec in self:
            rec.state = 'old'

    def act_move_new(self):
        for rec in self:
            rec.state = 'new'
