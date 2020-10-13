{
    'name': 'hospital',
    'version': '13.0.0.1',
    'category': 'Extra Tools',
    'author': 'Bhavik Vaghela',
    'website': '',
    'summary': 'Hospital Management System',
    'description': """Module to Manage School""",
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/website.xml',
        'views/demo.xml',
        'views/views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}