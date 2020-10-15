{
    'name': 'Student',
    'version': '13.0.0.1',
    'category': 'Extra Tools',
    'author': 'Bhavik Vaghela',
    'website': '',
    'summary': 'School Management',
    'description': """Module to Manage School""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/subject.xml',
        'views/student_subject_lines.xml',
        'views/student_info.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
