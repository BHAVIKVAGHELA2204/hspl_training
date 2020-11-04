{
    'name': 'Theme Emerald',
    'description': 'A Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Business',
    'summary': '',
    'version': '1.0',
    'license' : 'LGPL-3',
    'depends': ['website', 'website_theme_install','website_crm'],
    'data': [
        'templates/assets.xml',
        'templates/headers.xml',
        'templates/footer.xml',
        'templates/customize_options.xml',
        'templates/snippets.xml',
        'templates/contact.xml',
    ],
    'images': [
        'static/description/screenshot.png',
    ],

    'author': 'HSPL',
    'maintainer': 'HSPL',

    'application': False,
    'installable': True,
    'auto_install': False,

}
