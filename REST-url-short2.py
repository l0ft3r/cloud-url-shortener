from pyshorteners.shorteners  import Shortener
from flask import Flask, jsonify, request, redirect
import sys

app = Flask(__name__)

#how to let user put in their own url, which needs to be shorten?
#use dictionary to generate key. ",".join(key())
urls = ['https://www.google.nl', 'https://github.com/SOA-cloud-course/rest']


#include url id
@app.route('/<int:post_id>', methods = ['GET']) #
def url_short(post_id): 
	url = urls[post_id]
	shortener = Shortener('TinyurlShortener')
	return redirect(url, code=301)#"My short url is {}".format(shortener.short(url))
#curl -X GET http://127.0.0.1:5000/1

@app.route('/<int:post_id>', methods = ['PUT'])
def url_put(post_id):

	urls[post_id] = request.form['url_update']
	shortener = Shortener('TinyurlShortener')
	return "My short url is {}".format(shortener.short(urls[post_id]))
	return 
#curl -X PUT --form 'url_update=http://google.com' http://localhost:5000/1
#Global name 'url_update' is not defined????

@app.route('/', methods = ['POST'])	
def upost():
	#url = 'https://translate.google.nl/?hl=de#auto/zh-CN/render'
	urls.append(url_new)
	return "Add new url" + url_new
#curl -X POST --form 'url_new=http://google.com' http://localhost:5000/1	

@app.route('/<int:post_id>', methods = ['DELETE'])	
def url_delete(post_id):
	del urls[post_id]
	return "My urls are {} now.".format(urls)
		

if __name__ == '__main__':
    app.run(debug=True)