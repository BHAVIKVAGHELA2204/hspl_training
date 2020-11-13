{
    'name': 'Theme Bizland',
    'description': 'A Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Business',
    'summary': '',
    'version': '1.0',
    'depends': ['website', 'website_theme_install'],
    'data': [
        'views/assets.xml',
        'views/header.xml',
    ],
    'images': [
        'static/description/bizland_logo.png',
    ],

    'author': 'Bhavik Vaghela',
    'maintainer': 'Bhavik Vaghela',

    'application': False,
    'installable': True,
    'auto_install': False,
}
