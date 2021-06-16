# import urllib.request as request
# import json


# result = request.urlopen('https://challenges.hackajob.co/swapi/api/')
# print(result)
# print(dir(result))
# # print(result.data)

# print(result.read())
# # print(result.read().info().get_content_charset('utf-8'))
# json_obj = json.loads(result.read())

# # print(json_obj)

# import json
# import requests
# response = requests.get("https://challenges.hackajob.co/swapi/api/people/?search=Luke Skywalker")
# print(dir(response))
# js_obj = response.json()
# print(dir(js_obj))
# print(js_obj)
# print(js_obj['results'])
# print(dir(js_obj['results']))

# print(js_obj['results'].pop()['films'])


import requests
class Solution:

	def run(self, character):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		response = requests.get("https://challenges.hackajob.co/swapi/api/people/?search="+character)
		js_obj = response.json()
		results = js_obj['results'].pop()
		films = results['films']
		
		numberOfFilms = len(films)
		return numberOfFilms