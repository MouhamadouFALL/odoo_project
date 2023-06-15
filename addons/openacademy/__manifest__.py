# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
       Gérer les Formations """,

    'description': """
        Module Open Academy de gestion des formations: 
            - cours de formation
            - session de formation
            - inscription des participants
    """,

    'author': "MouhamadouFall",
    'website': "https://www.siggidieuf.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SIGGI/Open Academy',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
