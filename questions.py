import requests
from datetime import date, timedelta, datetime


class Question():
    def __init__(self, site: str):
        self.tags = []
        self.site = site

    def get_timeinterval(self, days):
        fromdate = datetime.today().date()
        todate = fromdate + timedelta(days)
        params = {'fromdate': f'{fromdate}', 'order': 'desc', 'sort': 'activity','todate': f'{todate}', 'tagged': self.tags, 'site': self.site}
        url = 'http://api.stackexchange.com/2.3/questions'
        response = requests.get(url, params=params)
        response_json = response.json()
        return response_json


site = 'stackoverflow'
question_py = Question(site)
question_py.tags = ['python']
questions_py = question_py.get_timeinterval(2)
print(questions_py)





