# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    This module copyright (c) 2013 Therp BV <http://therp.nl>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# from osv import fields, osv

# class fetchmail_server(osv.Model):
#     """
#     Add a company field to fetchmail_server.
#     """
#     _inherit = 'fetchmail.server'
#     _columns = {
#         'company_id': fields.many2one('res.company', 'Company'),
#         }


from openerp import api, fields, models, _

class FetchmailServer(models.Model):
    _inherit = 'fetchmail.server'

    company_id = fields.Many2one('res.company', 'Company')
