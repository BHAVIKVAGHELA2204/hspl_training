{
    'name': 'Tutorial theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_theme_install', 'website_blog', 'sale', 'portal'],

    'data': [
        'views/assets.xml',
        'views/home.xml',
        'views/layout.xml',
        'views/services.xml',
        'views/careers.xml',
        'views/about.xml',
        'views/profile.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
