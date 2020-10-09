from odoo import fields, models

class HospitalPractice(models.Model):
    _name = "hospital.practice"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Practice Table"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Name", required=True)
    image = fields.Binary(string="Image")
    primary_color = fields.Char(string="Primary Color")
    phone = fields.Char(string="Phone", required=True)
    time_duration = fields.Integer(string="Time Duration")
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string="Status", readonly=True, copy=False, default='draft')
    payment_type = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque')], required=True)
    google_url = fields.Char(string="Google Url")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="Date of Birth")
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


