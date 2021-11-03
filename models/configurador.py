# -*- coding:utf-8 -*-

from odoo import fields, models, api


class Configurador(models.Model):
	_name = "configurador"
	plan = fields.Char(string="configuración") 	
	active = fields.Boolean(string="Activo",default=False)
