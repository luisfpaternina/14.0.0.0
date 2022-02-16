# -*- coding: utf-8 -*-
{
    'name': "stock ext",

    'summary': """
        stock""",

    'author': "Coondev",

    'website': "",

    'contributors': ['Luis Felipe Paternina'],

    'category': 'Operations/Inventory',

    'version': '14.0.0.1.3',

    'depends': [
        'stock',
    ],

    'data': [

        "security/security.xml",
        "views/stock_picking_type.xml",
        "views/stock_picking.xml",
        "views/stock_location.xml",
    ],
    
    'installable': True,
}
