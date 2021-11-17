import os
from flask import Flask, render_template, request

# import our OCR function
from ocr import ocr_core

# a folder to store images
upload_folder = '/static/uploads/'

#to allow only specific type of files
allowed_ext = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder="template")

#create a function for allowed files

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_ext

@app.route("/")
def home_page():
    return render_template('index.html')

#Fun to handle uploded image
@app.route('/upload', methods=['GET','POST'])
def upload_img():
    if request.method == "POST":
        #to check if file is in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg="no file selected")
        file = request.files['file']
        #if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg="No file selected")
        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)

            #display
            return render_template('upload.html', msg='success!', extracted_text=extracted_text, img_src=upload_folder + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
