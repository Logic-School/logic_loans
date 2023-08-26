{
    'name': "Loans",
    'author': 'Rizwaan',
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'logic_base','admission','faculty'],
    'data': [
        'security/ir.model.access.csv',
        'views/loan_letter_views.xml',
        'views/inherited_views.xml',
        'report/custom_paperformat.xml',
        'report/loan_letter_report.xml',

    ],
    'demo': [],
    'summary': "Logic Loans",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}