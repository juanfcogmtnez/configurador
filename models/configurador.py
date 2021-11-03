# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Configurador(models.Model):
	_name = "configurador"
	_inherits = {'project.task':'tarea'}
	name = fields.Char(string="Nombre")
	tarea = fields.Many2one('project.task')
	active = fields.Boolean(string="Activo",default=True)
	espacios_ids = fields.One2many(
		comodel_name='espacios',
		inverse_name = 'name',
		string = "Espacios",
	)
