# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions

class DietFacts_product_template(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	
	calories = fields.Integer('Calories')
	servingsize = fields.Float('Serving Size')
	lastupdate = fields.Date('Last Update')
	meal_nutrient_ids = fields.One2many('product.template.nutrient','product_id')
	nutrition_score = fields.Float(string='Nutrition Score', store=True, compute='_calcscore')
	
	@api.multi
	@api.depends('meal_nutrient_ids','meal_nutrient_ids.value','meal_nutrient_ids.uom')
	def _calcscore(self):
		currentscore = 0
		i = 0
		for nutrient in self.meal_nutrient_ids:
			try:
				if nutrient.uom == 'g' or nutrient.uom == 'mg' or nutrient.uom == 'Kg':
					if nutrient.uom == 'g':
						nutrient.value *= 1000
						currentscore += nutrient.value
					i += 1		
				else:
					raise ValidationError(_("Erro"))
			except:
				raise exceptions.ValidationError(_("Erro"))
		if i == 0:
			currentscore = 0	
		else:
			currentscore /= i
		self.nutrition_score = currentscore


	#dietitem = fields.Boolean("Diet Item")

class DietFacts_res_users_meal(models.Model):
	_name = 'res.users.meal'
	name = fields.Char('Meal Name')
	meal_date = fields.Datetime('Menu Date')
	item_ids = fields.One2many('res_users_mealitem','meal_id')
	user_id = fields.Many2one('res.users','Meal User')
	totalcalories = fields.Integer(string='Total Meal Calories', store=True, compute='_calccalories')
	totalitems = fields.Integer(string='Total Meal Items', store=True, compute='_totalitems')
	notes = fields.Text('Meal Notes')
	dailyvalue = fields.Float('Daily Value')
	largemeal = fields.Boolean('Large Meal', readonly=True)


	@api.multi
	@api.depends('notes')
 	def _msg_ola(self):
 		msg = 'Olá'
 		self.notes = msg

 	@api.multi
 	def _atualiza(self):
 		action1 = {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

	@api.onchange('totalcalories')
	def check_totalcalories(self):
		if self.totalcalories > 500:
			self.largemeal = True
		else:
			self.largemal = False
	@api.multi
	@api.depends('item_ids','item_ids.servings')
	def _calccalories(self):
		currentcalories = 0
		for mealitem in self.item_ids:
			currentcalories += mealitem.calories * mealitem.servings
		self.totalcalories = currentcalories

	@api.multi
	@api.depends('item_ids')
	def _totalitems(self):
		total = 0
		for i in self.item_ids:
			total += 1
		self.totalitems = total



class DietFacts_res_users_mealitem(models.Model):
	_name = 'res_users_mealitem'
	meal_id = fields.Many2one('res.users.meal')
	item_id = fields.Many2one('product.template','Meal Item')
	servings = fields.Float('Servings')
	notes = fields.Text('Meal item notes')
	calories = fields.Integer(related='item_id.calories', string='Calories Per Serving', store=True, readonly=True)

class DietFacts_product_nutrient(models.Model):
	_name = 'product.nutrient'
	name = fields.Char('Nutrient Name')
	uom_id = fields.Many2one('product.uom','Unity of Measure')
	description = fields.Text('Nutrient Description')


class DietFacts_product_template_nutrients(models.Model):
	_name = 'product.template.nutrient'
	nutrient_id = fields.Many2one('product.nutrient')
	product_id = fields.Many2one('product.template')
	value = fields.Float('Value')
	dailypercent = fields.Float('Daily Percentage')
	uom = fields.Char(related='nutrient_id.uom_id.name', string='UOM', readonly=True)


# class dietfacts(models.Model):
#     _name = 'dietfacts.dietfacts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute='_value_pc', store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
