{
    'name': 'My Module',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
