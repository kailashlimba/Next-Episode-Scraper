import config
import requests

class ApiDetails:

	def __init__(self,tvseries):
		self.tvseries = tvseries
		api_url = config.API_KEY + tvseries
		self.key = requests.get(api_url).json()



	def response(self):
		return self.key['response']

	def imdbID(self):
		return self.key['imdbID']

	def title(self):
		return self.key['Title']

	def year(self):
		api_year = self.key['Year']
		return api_year.strip()

	def type(self):
        return self.key['Type']