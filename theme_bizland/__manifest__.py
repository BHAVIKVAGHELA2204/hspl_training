{
    'name': 'Theme Bizland',
    'description': 'A Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Business',
    'summary': '',
    'version': '1.0',
    'depends': ['website', 'website_theme_install', 'portal'],
    'data': [
        'data/menu.xml',
        'views/assets.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/snippets.xml',
        # 'views/index.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/bizland_logo.png',
    ],
    'qweb': [
        'static/src/xml/index.xml',
    ],

    'author': 'Bhavik Vaghela',
    'maintainer': 'Bhavik Vaghela',

    'application': False,
    'installable': True,
    'auto_install': False,
}
