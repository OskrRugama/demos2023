{
    'name': 'Precio ETD',
    'version': '1.0.0',
    'category': 'Sales',
    'summary': 'Módulo para la actualización de precios de venta y tarifas',
    'author': 'Oscar Rugama',
    'website': 'https://www.ak.com.ni',
    'depends': ['base','stock', 'product', 'sale','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        #'views/price_history_report_views.xml',
    ],
    'installable': True,
    'application': False,
}
