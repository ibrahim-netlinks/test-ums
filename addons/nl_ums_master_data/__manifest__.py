# -*- coding: utf-8 -*-
{

    'name': "Master",

    'summary': """
                Master table for Test University Management System
                """,

    'description': """
                    Master table for Test University Management System
                    """,

    'author': "Test Author",
    'website': "http://www.testcompany.com",

    'name': "nl_ums_master_data",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list

    'category': 'Education',

    'category': 'Uncategorized',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        # 'security/ir.model.access.csv',
        'views/topic_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
            'views/master_view.xml',
            'views/course_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}