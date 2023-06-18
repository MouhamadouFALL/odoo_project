#-*- coding: utf-8 -*-

from odoo import api, models, fields, _


class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many("openacademy.session", string="Sessions", readonly=True)