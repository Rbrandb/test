{
    'name': "Portal user to developer",
    'version': "16.0.0.0",
    'author': "SMART",
    'category': "Tools",
    'summary': "Allow access to portal users",
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'static/src/xml/portal_template_inherit.xml',
        'views/res_users.xml',
        # 'views/portal_view.xml',
        'views/employee_hub.xml',
        'views/portal_time_off.xml',
        'views/time_off_types.xml',
        'static/src/xml/portal_payslip.xml'
    ],
    'demo': [],
    'depends': ['website', 'portal', 'hr_holidays', 'hr', 'web', 'base', 'portal', 'account_payment', 'hr_payroll'],
    'assets': {
        'web.assets_frontend': [
            '/portal_user_to_developer/static/src/js/portal_time_off.js',
            '/portal_user_to_developer/static/src/js/portal_payslip.js',
            '/portal_user_to_developer/static/src/css/portal.css',
            '/portal_user_to_developer/static/src/css/time_off_request.scss'
        ],
        'web.assets_backend': [
            'portal_user_to_developer/static/src/js/documents_inspector.js',
            'portal_user_to_developer/static/src/xml/documentsInspector_extend.xml'
        ],
        'web.assets_qweb': [

        ],
    },
    'installable': True,
}
