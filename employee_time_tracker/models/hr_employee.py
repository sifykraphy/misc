# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _name = 'hr.employee'
    _inherit = ['hr.employee', 'data.track.thread']