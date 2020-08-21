from flask import Flask, render_template, request  
import os
app = Flask(__name__)  
 
wsgi_app=app.wsgi_app

@app.route('/', methods = ['GET','POST'])  
def success(): 
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join("uploads", f.filename))
		#return render_template("file_upload_form.html", message="successful")
    return render_template("file_upload_form.html", message="Upload")
  
if __name__ == '__main__':  
	
    app.run(debug = True)