{
    'name': 'Cloud CTI Integration',
    'version': '17.2',
    'summary': 'Integrate Cloud CTI with Odoo CRM',
    'author': 'Harihara Pandi',
    'category': 'CRM',
    'depends': ['crm'],
    'data': [
        'views/cloud_cti_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cloud_cti/static/src/js/cloud_cti.js',
        ],
    },
    'installable': True,
    'application': True,
}

    