# __manifest__.py

{
    'name': 'Odoo 14 Academic Management',
    'version': '1.0',
    'summary': 'Manage academic in Odoo 14',
    'description': 'This module allows you to manage academic in Odoo 14.',
    'category': 'Education',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': 
    [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/course.xml",
        "views/session.xml",
        "views/attendee.xml",
        "views/partner.xml",
    ],
}
