'''
HTTP Status Code v0.1

Github: https://github.com/ilstar/http_status_code
Author: Fred Liang
'''

import csv

from feedback import Feedback

query = '{query}'
query = query.lower()
baseurl = 'https://devcenter.heroku.com/articles/error-codes'

fb = Feedback()

with open('status_code.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        code, desc = row
        lower_code = code.lower()
        lower_desc = desc.lower()
        # https://devcenter.heroku.com/articles/error-codes#h18-request-interrupted
        urlized= "{0}#{1}-{2}".format(baseurl, lower_code, lower_desc.replace(' ', '-'))

        if lower_code.find(query) != -1:
            fb.add_item(desc, code, arg=urlized)
        elif lower_desc.find(query) != -1:
            fb.add_item(code, desc, arg=urlized)

print fb
