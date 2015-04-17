from pyshorteners.shorteners  import Shortener
from flask import Flask, jsonify, request, redirect, make_response, render_template
import sys
import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

app = Flask(__name__)

#use dictionary to generate key. ",".join(key())
keys = []



urls = {'a':'https://www.google.nl', 'b':'https://github.com/SOA-cloud-course/rest'}
#urls.update({id_generator(): 'xkcd.com'})


#include url id
@app.route('/<string:post_id>', methods = ['GET']) #
def url_short(post_id):
	if post_id not in urls:
		return make_response('', 404)
	url = urls[post_id]
	shortener = Shortener('TinyurlShortener')
	return redirect(url, code=301)#"My short url is {}".format(shortener.short(url))
#curl -X GET http://127.0.0.1:5000/a

@app.route('/<string:post_id>', methods = ['PUT'])
def url_put(post_id):
	if post_id not in urls:
		return make_response('', 404)
	urls[post_id] = request.form['url']
	shortener = Shortener('TinyurlShortener')
	return make_response('', 200)
#curl -X PUT --form 'url=http://google.com' http://localhost:5000/a

@app.route('/', methods = ['POST'])	
def upost():
	if request.form['url'] in urls.values():
		return make_response('error', 400)
	post_id = id_generator()
	while post_id in urls:
		post_id = id_generator()
	urls[post_id] = request.form['url']
	return make_response(post_id, 201)
#curl -X POST --form 'url_new=http://google.com' http://localhost:5000/a	

@app.route('/', methods = ['GET'])	
def uget():
	keys = ""
	for key in urls.keys():
		keys += key
	return make_response(keys, 200)
#curl -X GET http://127.0.0.1:5000/


@app.route('/<string:post_id>', methods = ['DELETE'])	
def url_delete(post_id):
	if post_id in urls:
		del urls[post_id]
		return make_response(post_id + '.html', 204)
	return make_response('', 404)
#curl -X DELETE http://localhost:5000/a


@app.route('/', methods = ['DELETE'])	
def all_delete():
	urls.clear()
	return make_response('', 204)
#curl -X DELETE http://localhost:5000/
    
if __name__ == '__main__':
    app.run(debug=True)