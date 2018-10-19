from flask import Flask, render_template, request, json
app=Flask(__name__)

@app.route('/')
def main():
	return render_template('signup.html')


@app.route('/signup',methods=['POST'])
def signup():
	_name=request.form['inputName']
	_email=request.form['email']
	_password=request.form['inputPassword']

	if _name and _email and _password:
		return json.dumps({'html':'<span> all Fields are Good</span>'})
	else:
		return json.dumps({'html':'<span> Enter Missing Fields</span>'})

if __name__=="__main__":
	app.run(debug=True)

