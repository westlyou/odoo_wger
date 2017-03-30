# -*- coding: utf-8 -*-
{
    'name': "odoo_wger",

    'summary': """
        Implements Wger features into odoo""",

    'description': """
        Implements features of wger software into odoo 10.
    """,

    'author': "BoxCoder",
    'website': "http://www.boxcoder.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Gym',
    'version': '0.1',

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
