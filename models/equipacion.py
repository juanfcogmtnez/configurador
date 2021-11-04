# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Equipacion(models.Model):
	_name = "equipacion"
	_inherit = ['image.mixin']
	name = fields.Char(string='Nombre equipo')
	active = fields.Boolean(string = 'Activo',default=True)
	codigo = fields.Char(string="codigo")
	description = fields.Text(string='Descripción')
	superficie = fields.Float(string='Superficie')
	espacio_id = fields.Many2one(comodel_name='espacios', string = 'Proyecto')
