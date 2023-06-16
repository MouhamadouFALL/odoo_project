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
    description = fields.Text()


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char("Title", required=True)
    start_date = fields.Date("Satart Date")
    duration = fields.Float("Duree", digits=(6, 2), help="Duration in days")
    seats = fields.Integer("Nommbre de place")