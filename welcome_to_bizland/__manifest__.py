{
    'name': 'Welcome to Bizland theme',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_theme_install', 'website_blog', 'portal', 'web_editor'],

    'data': [
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/index.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
