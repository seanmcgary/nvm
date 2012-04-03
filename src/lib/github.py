import requests
import json

def get_tags():
	url = 'https://api.github.com/repos/joyent/node/tags'

	return json.loads(requests.get(url).text);

def get_tag_tarball_url(tag):
	
	tags = get_tags()

	for i in tags:
		if i == tag:
			return i['tarball_url']

def is_valid_tag(tag):
	tags = get_tags()

	for i in tags:
		if i['name'] == tag:
			return True
	
	return False
