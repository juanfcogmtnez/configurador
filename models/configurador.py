# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Configurador(models.Model):
	_name = "configurador"
	name = fields.Many2one(string="Nombre")
	plan_ids = fields.Many2one(
		comodel_name='project.task',
		string = 'Plan de espacios'
	) 	
	active = fields.Boolean(string="Activo",default=True)
