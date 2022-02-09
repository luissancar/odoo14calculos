# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejemplo(models.Model):
#     _name = 'ejemplo.ejemplo'
#     _description = 'ejemplo.ejemplo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class persona(models.Model):
	_name = 'ejemplo.persona'
	_description = 'model persona'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
	fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
	precio = fields.Integer(string='Precio',required=True)
	cantidad = fields.Integer(string='Cantidad',required=True)
	fecha_nacimiento = fields.Date(string='Fecha de nacimiento',required=True)
	annos = fields.Integer("Años", compute="_get_annos")
	total = fields.Integer("Total", compute="_get_total")


	@api.depends('fecha_nacimiento')
	def _get_annos(self):
		for pers in self:
			hoy=date.today()
			pers.annos = relativedelta(hoy, pers.fecha_nacimiento).years



	@api.depends('precio')
	def _get_total(self):
		for pers in self:
			pers.total =  pers.precio * pers.cantidad


