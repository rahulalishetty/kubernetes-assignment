from flask import Flask,render_template, request
app = Flask(__name__)
 
@app.route('/')
def user():
   return render_template('userinput.html')

@app.route('/messageSent',  methods=['POST'])
def success():
	if request.method == 'POST':
		message = request.form.get('message')
		with open("/data/messages.txt",'a') as myfile:
			myfile.write(message+'\n')
	else:
		pass
	return render_template('userinput.html')
 
if __name__ == '__main__':
   app.run(host="0.0.0.0")
