from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		restaurant = request.form['restaurant']
		print(restaurant)
		if restaurant == "mexican":
			return redirect(url_for('mexican'))
		elif restaurant == "chinese":
			return redirect(url_for('chinese'))
		elif restaurant == "japanese":
			return redirect(url_for('japanese'))
		elif restaurant == "korean":
			return redirect(url_for('korean'))
		elif restaurant == "french":
			return redirect(url_for('french'))
		elif restaurant == "italian":
			return redirect(url_for('italian'))
		elif restaurant == "mediterranean":
			return redirect(url_for('mediterranean'))
		elif restaurant == "indian":
			return redirect(url_for('indian'))
		elif restaurant == "thai":
			return redirect(url_for('thai'))
		elif restaurant == "middleeastern":
			return redirect(url_for('middleeastern'))
		elif restaurant == "vietnamese":
			return redirect(url_for('vietnamese'))
		elif restaurant == "greek":
			return redirect(url_for('greek'))
	return render_template("index.html")

@app.route('/mexican', methods=['GET','POST'])
def mexican():
	#get_median_income()
	return render_template("mexican-map.html")

@app.route('/korean', methods=['GET','POST'])
def korean():
	return render_template("korean-map.html")

@app.route('/chinese', methods=['GET','POST'])
def chinese():
	return render_template("chinese-map.html")

@app.route('/japanese', methods=['GET','POST'])
def japanese():
	return render_template("japanese-map.html")

@app.route('/french', methods=['GET','POST'])
def french():
	return render_template("french-map.html")

@app.route('/italian', methods=['GET','POST'])
def italian():
	return render_template("italian-map.html")

@app.route('/mediterranean', methods=['GET','POST'])
def mediterranean():
	return render_template("mediterranean-map.html")

@app.route('/indian', methods=['GET','POST'])
def indian():
	return render_template("indian-map.html")

@app.route('/thai', methods=['GET','POST'])
def thai():
	return render_template("thai-map.html")

@app.route('/middleeastern', methods=['GET','POST'])
def middleeastern():
	return render_template("middle-eastern-map.html")

@app.route('/vietnamese', methods=['GET','POST'])
def vietnamese():
	return render_template("vietnamese-map.html")

@app.route('/greek', methods=['GET','POST'])
def greek():
	return render_template("greek-map.html")


if __name__ == "__main__":
	app.run(debug=True)