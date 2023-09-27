from odoo import api,models, fields

class Partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    is_instructor = fields.Boolean("Is Instructor" ,default=True)