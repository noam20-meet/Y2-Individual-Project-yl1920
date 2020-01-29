from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

@app.route('/study_image', methods = ['POST'])
def study_image():
	
	image_url = request.form['url-input']

	api_url = "https://chess-api-chess.herokuapp.com/api/v1"
	# this is content of the message(data) you are sending to clarifai
	data ={"inputs": [
		  {
			"data": {
			  "image": {
				"url": "https://samples.clarifai.com/metro-north.jpg"
			  }
			}
		  }
		]}

	# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))

	somehing = response.content
	elsii = str(somehing, 'utf-8').split('outputs')
	return render_template('home.html', results=elsii)
	string.split('name')

if __name__ == '__main__':
	app.run(debug=True)