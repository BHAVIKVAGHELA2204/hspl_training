{
    'name': 'My Module',
    'description': 'A description for your theme.',
    'version': '1.0',
    'author': 'Bhavik vaghela',
    'category': 'Theme/Creative',

    'depends': ['website', 'website_sale'],

    'data': [
        'security/ir.model.access.csv',
        'data/data_view.xml',
        'views/demo.xml',
        'views/templates.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
