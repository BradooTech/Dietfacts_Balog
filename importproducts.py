#!/usr/bin/python
import xmlrpclib
import csv

server = 'http://localhost:8069'
database = 'dietfacts3'
user = 'admin'
password = 'admin'


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(server))
#print common.version()

uid = common.authenticate(database, user, password, {})

#print uid


OdooApi = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(server))

filter = [('categ_id.id','=',7)]
'''
product_count = OdooApi.execute_kw(database, uid, password,
	'product.template', 'search_read',
	[filter],
	{'fields': ['name', 'calories', 'nutrition_score']})

'''

'''
product_count = OdooApi.execute_kw(database, uid, password,
	'res.users.meal', 'search_read', [[['totalcalories','>',600],[]]],
	{'fields': ['name', 'meal_date', 'notes','totalcalories']})


Filename = 'importdata.csv'
reader = csv.reader(open(Filename, 'rb'))

for row in reader:

		product_name = row[0]
		calories = row[1]
		categ_id = row[2]
		
		filter = [('name','=',product_name)]
		product_id = OdooApi.execute_kw(database, uid, password,
			'product.template', 'search_read', [filter])
		if product_id:
			record = [product_id, {'calories': calories, 'categ_id':[0]}]
			print "Found the product id=" + str(product_name)
		else:
			print "Adding Product: " + product_name
			record = [{'name': product_name, 'calories': calories, 'categ_id': categ_id}]
			OdooApi.execute_kw(database, uid, password, 'product.template', 'create', record)
0
OdooApi.execute_kw(database, uid, password, 'product.template', 'write', [[46], {
			'calories': "100"}])

id = 46
OdooApi.execute_kw(database, uid, password, 'product.template', 'unlink', [[id]])
ver = OdooApi.execute_kw(database, uid, password,
    'product.template', 'search', [[['id', '=', id]]])
product_count = OdooApi.execute_kw(database, uid, password,
	'product.template', 'search_read',
	[],
	{'fields': ['name', 'id','calories']}
	)
print product_count
print ver
'''
product_ids = OdooApi.execute_kw(database, uid, password, 'product.template', 'search',[[['categ_id','=',7]]])
report = xmlrpclib.ServerProxy('{}/xmlrpc/2/report'.format(server))
result = report.render_report(
    database, uid, password, 'product.nutrition', product_ids)
report_data = result['result'].decode('base64')

#arquivo = open('report','w')
#arquivo.write(report_data)

print report_data