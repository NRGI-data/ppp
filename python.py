#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

# Put the details of the dataset we're going to create into a dict.
'{"resource": {"package_id": "ppp-test-1"}, "fields": [ {"id": "a"}, {"id": "b"} ], "records": [ { "a": 1, "b": "xyz"}, {"a": 2, "b": "zzz"} ]}'

dataset_dict = {
				'name': 'ppp-test-2',
				'title': 'Purchasing power parity (PPP)',
				'description': 'Data are sourced from the World Bank, International Comparison Program database. One dataset is provided: PPP conversion factor, GDP (LCU per international $).',
				'version': '0.1.0',
				'license': 'ODC-PDDL-1.0'
				# 'resources': [{
				# 	'name': 'ppp-gdp',
				# 	'path': 'data/ppp-gdp.csv',
				# 	'format': 'csv',
				# 	'mediatype': 'text/csv',
				# 	'schema': {
				# 		'fields': [
				# 			{
				# 				'name': 'Country',
				# 				'type': 'string'
				# 			},
				# 			{
				# 				'name': 'Country_ID',
				# 				'type': 'string',
				# 				'description': 'ISO 3166-1 alpha-2 code'
				# 			},
				# 			{
				# 				'name': 'Year',
				# 				'type': 'date',
				# 				'description': 'YYYY'
				# 			},
				# 			{
				# 				'name': 'PPP',
				# 				'type': 'number',
				# 				'description': 'PPP conversion factor, GDP (LCU per international $)'
				# 			}
				# 		]
				# 	}
				# }]
			}
# dataset_dict = {
#     'name': 'my_dataset_name',
#     'notes': 'A long description of my dataset',
# }


# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(
    'http://boot2docker:5462/api/action/package_create')

# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
request.add_header('Authorization', 'ea8de489-11f3-4c30-afaf-480e3fafd422')

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']
pprint.pprint(created_package)

created_package['id']

request_load = urllib2.Request(
    'http://boot2docker:5462/api/action/resource_update=' + created_package['id'] )
http --json POST http://demo.ckan.org/api/3/action/resource_update?id=<resource id> upload=@updated_file.csv Authorization:<api key>





curl -X POST http://boot2docker:5462/api/3/action/datastore_create -H "Authorization: ea8de489-11f3-4c30-afaf-480e3fafd422" -d '{"resource": {"package_id": "ppp-test-1"}, "fields": [ {"id": "a"}, {"id": "b"} ], "records": [ { "a": 1, "b": "xyz"}, {"a": 2, "b": "zzz"} ]}'
http://boot2docker:5462















