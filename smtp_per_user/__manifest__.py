# -*- coding: utf-8 -*-
# Author: Andrius Laukavičius. Copyright: Andrius Laukavičius.
# See LICENSE file for full copyright and licensing details.

{
    'name': "SMTP Per User",
    'version': '0.1.0',
    'summary': 'Send letters from Odoo using your own mail',
    'category': 'Mail',
    'description': """Can configure different mail servers per user""",
    'author': 'Andrius Laukavičius',
    'license': 'LGPL-3',
    'website': "https://github.com/oerp-odoo",
    "depends": ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/smtp_per_user_view.xml',
    ],
    "installable": True
}
