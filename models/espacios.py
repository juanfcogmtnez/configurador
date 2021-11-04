# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Espacios(models.Model):
	_name = "espacios"
	_inherit = ['image.mixin']
	name = fields.Char(string='Local')
	sub_name = fields.Char(string='Sub-local')
	active = fields.Boolean(string = 'Activo',default=True)
	codigo = fields.Char(string="codigo")
	description = fields.Text(string='Descripción')
	superficie = fields.Float(string='Superficie')
	bloque = fields.Char(string='Bloque')
	planta = fields.Char(string='Planta')
	proyecto_id = fields.Many2one(comodel_name='configurador', string = 'Proyecto')
	equipacion_ids = fields.One2many(
		comodel_name='equipacion',
		inverse_name = 'espacio_id',
		string = "Equipamiento",
	)
