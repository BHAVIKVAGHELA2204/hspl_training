{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_theme_install', 'website_blog', 'sale'],

    'data': [
        'views/layout.xml',
        'views/pages.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
