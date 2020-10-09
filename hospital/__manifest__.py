{
    'name': 'hospital',
    'version': '13.0.0.1',
    'category': 'Extra Tools',
    'author': 'Odoo mates',
    'website': 'hospital.com',
    'license': 'AGPL-3',
    'summary': 'Hospital Management System',
    'description': """Module to Manage School""",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient.xml',
        'views/hospital_doctor.xml',
        'views/hospital_appointment.xml',
        'views/hospital_practice.xml',
        'views/doctor_timeing.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}