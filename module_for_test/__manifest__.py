{
    "name": "Automatic acceptance of applications",
    'version': '1.0.0',
    'category': 'Test',
    'sequence': -101,
    'summary': 'Model of automatic acceptance of applications',
    'description': """Module consist of model data with fields of name customer and description requests""",
    'depends': ['mail', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'actions/actions.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3'
}