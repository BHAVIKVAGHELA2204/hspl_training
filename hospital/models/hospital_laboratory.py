from odoo import fields, models

class Hospitallaboratory(models.Model):
    _name = "hospital.laboratory"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "laboratory Table"

    patient_id = fields.Many2one(
        'hospital.appointment', string="Name", required=True)
    age = fields.Integer(related="patient_id.age", string="Age", store=True)
    doctor = fields.Many2one('hospital.doctor', related="patient_id.doctor_id", string="Doctor Name")
    dob = fields.Date(related="patient_id.dob", string="Date of Birth", store=True)
    date_of_appointment = fields.Date(related="patient_id.date_of_appointment", string="Date of Appointment", store=True)
    contact = fields.Char(related="patient_id.contact", string="Contact", store=True)
    blood_group = fields.Char(related="patient_id.blood_group", string="Blood Group", store=True)
    address = fields.Text(related="patient_id.address", string="Address", store=True)
    gender = fields.Selection(related="patient_id.gender", string='Gender', default='male', store=True)
    m_status = fields.Selection(related="patient_id.m_status", string='Marital status', default='unmarried',
                                store=True)
    image = fields.Binary(related="patient_id.image", string="Image", store=True)
    illness = fields.Selection(related="patient_id.illness", string='Illness')
    report = fields.Selection([
        ('blood', 'Blood'),
        ('urine', 'Urine'),
        ('mri', 'MRI'),
    ], string='Report', default='blood')