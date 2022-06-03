# -*- coding: utf-8 -*-
{
    'name': 'Trasnporte Marítimo',
    'summary': """Transportes en Barco""",
    'description': """
     
===================================================
    """,
    'author': "Botello Bryan",
    'website': "",
    'category': 'Transport',
    'version': '1.0',
    'depends': ['base', 'stock'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/transportes_view.xml',
        'views/menu_view.xml',


        
    ],
    'application': True,
    'auto_install': False,
}
