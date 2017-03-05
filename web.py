from flask import Flask, render_template, request
import weather
import os
import Yelp_results

app = Flask(__name__)

@app.route("/")
def index():
	location = request.values.get('location')
	restaurants = None
	if location:
		restaurants = Yelp_results.get_business('location')
	return render_template('index.html', location=location, food=food)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)