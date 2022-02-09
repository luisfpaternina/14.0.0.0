{
    'name': 'SAT COMPANIES PURCHASE',

    'version': '14.0.1.0',

    'author': "Process Control",

    'contributors': ['Luis Felipe Paternina'],

    'website': "https://www.processcontrol.es/",

    'category': 'stock',

    'depends': [

        'sale_management',
        'stock',
        'purchase',
        'base_automation',

    ],

    'data': [
       
        'security/ir.model.access.csv',
        'reports/purchase_order.xml',
        
    ],
    'installable': True
}
