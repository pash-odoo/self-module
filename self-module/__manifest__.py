{
    'name':'Car Repair Service',
    'version':'1.0',
    'depends':['base','mail'],
    'auther':'Shubh Patel (Pash)',
    'category': 'Repair Service/Car Repair Service',
    'description':"""This module is related to Car Repair Service.""",
    'data':[
        'security/ir.model.access.csv',
        'views/car_repair_views.xml',
        'views/car_repair_company.xml',
        'views/car_repair_tag.xml',
        'views/car_repair_service.xml',
        'views/res_user.xml',
        'views/car_repair_menus.xml',
    ],
    'demo':[
        'demo/car_repair_demo_data.xml'
    ],
    'application':True
}