{
    'name': 'Test Custom Theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'portal'],

    'data': [
        'views/assets.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
