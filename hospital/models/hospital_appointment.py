from odoo import fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "appointment Table"

    patient_name = fields.Many2one(
        'hospital.patient', string="Name", required=True)
    age = fields.Integer(string="Age")
    doctor_id = fields.Many2one(
        'hospital.doctor', string="Doctor Name")
    dob = fields.Date(related="patient_name.dob", string="Date of Birth", store="True")
    date_of_appointment = fields.Date(string="Date of Appointment", store="True", required=True)
    appointment_date = fields.Date(string="Appointment Date")
    sequence = fields.Integer(string="Sequence")
    contact = fields.Char(related="patient_name.contact", string="Contact", store="True")
    blood_group = fields.Char(related="patient_name.blood_group", string="Blood Group", store="True")
    address = fields.Text(related="patient_name.address", string="Address", store="true")
    gender = fields.Selection(related="patient_name.gender", string='Gender', default='male', store="True")
    m_status = fields.Selection(related="patient_name.m_status", string='Marital status', default='unmarried',
                                store="True")
    image = fields.Binary(related="patient_name.image", string="Image", store="True")
