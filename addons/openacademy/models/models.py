# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


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


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char("Title", required=True)
    start_date = fields.Date("Satart Date")
    duration = fields.Float("Duree", digits=(6, 2), help="Duration in days")
    seats = fields.Integer("Nommbre de place")
    instructor_id =fields.Many2one("res.partner", domain=['|', ("instructor", "=", True), ('category_id.name', 'ilike', 'Teacher')],string="Instructeur")
    course_id = fields.Many2one("openacademy.course", ondelete="cascade", string="Cours", required=True)
    attendee_ids = fields.Many2many("res.partner", string="Participants")