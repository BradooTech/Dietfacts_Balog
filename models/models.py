# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dietfacts_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	
	calories = fields.Integer("Calories")










# class dietfacts(models.Model):
#     _name = 'dietfacts.dietfacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
