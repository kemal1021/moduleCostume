from odoo import api,models, fields

class Session(models.Model):
    _name = 'odoo14.session'
    _description = 'Session'

    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one(comodel_name="odoo14.course", string="Course")
    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor")
    start_date = fields.Date(string="Start Date")
    duration = fields.Integer(string="Duration")
    seats = fields.Integer(string="Seats")
    active = fields.Boolean(string="Is Active", default=True)


    attendee_ids = fields.One2many(
        comodel_name="odoo14.attendee",
        string = "Attendees",
        inverse_name = "session_id"
    )

    taken_seats = fields.Float(
        string = "Taken Seats",
        compute = "_compute_taken_seats"
        )
    
    def _compute_taken_seats(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.0 * len(x.attendee_ids) / x.seats
            else:
                x.taken_seats = 0.0

    @api.onchange('seats')
    def onchange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
        else:
            self.taken_seats = 0.0

    @api.constrains('instructor_id', 'attendee_ids')
    def _cek_instruktur(self):
        for session in self:
            x = [att.partner_id.id for att in session.attende_ids]
            for session.instructor_id.id in x:
                return False
        return True
    
    _constraints = [(_cek_instruktur,
                     'instructur tidak boleh sama dengan attende',
                     ['instructor_id','attenndee_ids'])]