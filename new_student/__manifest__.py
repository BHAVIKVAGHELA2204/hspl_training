{
    'name': 'New Student',
    'version': '13.0.0.1',
    'category': 'Extra Tools',
    'author': 'Bhavik Vaghela',
    'website': '',
    'summary': 'School Management',
    'description': """Module to Manage School""",
    'depends': ['base', 'trainee_student'],
    'data': [
        'security/ir.model.access.csv',
        'views/detailes.xml',
        'views/subject.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
