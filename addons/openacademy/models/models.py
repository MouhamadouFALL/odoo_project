# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Course(models.Model):
    _name = "openacademy.course"

    name = fields.Char(string="Title", requiired=True)
    description = fields.Text(placeholder="Description du cours")
    responsible_id = fields.Many2one("res.users", ondelete="set null", string="Responsable", index=True)
    session_ids = fields.One2many("openacademy.session", "course_id", string="Sessions")

    _sql_constraints = [
        (
            "name_description_check",
            "CHECK (name != description)",
            "Le nom et la description du cours doivent être différent."
        ),
        (
            "uniq_name",
            "UNIQUE (name)",
            "Le nom du Cours doit être unique"
        )
    ]

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count([("name", "=like", u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char("Title", required=True)
    start_date = fields.Date("Satart Date")
    duration = fields.Float("Duree", digits=(6, 2), help="Duration in days")
    seats = fields.Integer("Nommbre de place")
    instructor_id =fields.Many2one("res.partner", domain=['|', ("instructor", "=", True), ('category_id.name', 'ilike', 'Teacher')],string="Instructeur")
    course_id = fields.Many2one("openacademy.course", ondelete="cascade", string="Cours", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Participants")
    # champs calculés
    taken_seats = fields.Float("Places occupées", compute="_compute_taken_seats")

    @api.depends("seats", "attendee_ids")
    def _compute_taken_seats(self):

        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = len(record.attendee_ids) * 100 / record.seats

    @api.onchange("seats", "attendee_ids")
    def _onchange_verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Valeur Incorrecte 'nombre de places' ",
                    'message': " Le nombre de place disponible ne doit pas être négatif. "
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Beaucoup de participant",
                    'message': "Supprimer des participants supplémentaores ou augmenter le nombre de places"
                }
            }

    @api.constrains("instructor_id", "attendee_ids")
    def _check_instrutor_not_in_attendee_ids(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.attendee_ids:
                raise ValidationError("L'instructor ne pas êtres dans les participants")
