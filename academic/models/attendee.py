from odoo import models, fields

class Attende(models.Model):
    _name = "odoo14.attendee"  # Gantilah 'your_module' sesuai dengan nama modul Anda
    name = fields.Char(string="Name",required=True)

    session_id = fields.Many2one(
        comodel_name = "odoo14.session",
        string = "Session"
    )
    partner_id = fields.Many2one(
        comodel_name = "res.partner",
        string = "Partner"
    )