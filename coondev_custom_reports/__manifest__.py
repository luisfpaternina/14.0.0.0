{
    'name': 'Coondev custom reports',

    'version': '14.0.1.0',

    'author': "Coondev",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.coondev.com",

    'category': 'reports',

    'depends': [

        'sale_management',
        'mrp',

    ],

    'data': [
       
        'reports/mrp_report.xml',
        'reports/sale_order_report.xml',
        
    ],
    'installable': True
}

