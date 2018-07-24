from flask import Flask,render_template, request
app = Flask(__name__)
 
@app.route('/')
def write():
	lines=[]
	with open("/data/messages.txt",'r') as myfile:
		lines=[line.rstrip('\n') for line in myfile]
	return render_template('view_file.html',lines=lines)

if __name__ == '__main__':
   app.run(host="0.0.0.0")
