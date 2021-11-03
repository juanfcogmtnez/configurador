# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Configurador(models.Model):
	_name = "configurador"
	_inherits = {'project.task':'plan_id'}
	name = fields.Many2one(string="Nombre")
	plan_id = fields.Many2one('project.task') 	
	active = fields.Boolean(string="Activo",default=True)
