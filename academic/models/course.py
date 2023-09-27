from odoo import models, fields

class Course(models.Model):
    _name = 'odoo14.course'  # Gantilah 'your_module' sesuai dengan nama modul Anda
    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    responsible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        required=True
    )

    session_ids = fields.One2many(
    comodel_name="odoo14.session",
    string="Sessions",
    inverse_name="course_id",
    )
