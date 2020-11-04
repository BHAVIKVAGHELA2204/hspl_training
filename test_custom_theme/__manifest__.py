{
    'name': 'Test Custom Theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'portal'],

    'data': [
        'views/assets.xml',
        'templates/headers.xml',
        'templates/footer.xml',
        'templates/snippets.xml',
        'views/home.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
