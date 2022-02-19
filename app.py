from flask import Flask, render_template
from flask import request
import zipfile
import time
import os
from flask_cors import CORS

app = Flask(__name__,
            template_folder="/Users/beerpig/Downloads/GradingSystem/frontend/dist",
            static_folder="/Users/beerpig/Downloads/GradingSystem/frontend/dist/static"
            )

CORS(app)


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/handler', methods=["POST"])
def handler():
    file_obj = request.files.get('file', None)
    print("file_obj.name:", file_obj.filename)
    timestamp = str(time.time())
    cur_timestamp = timestamp.replace('.', '')
    print(cur_timestamp)
    upload_folder = 'upload/'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        print()
    if file_obj.filename != '':
        cur_name = cur_timestamp + '.' + file_obj.filename.split('.')[-1]
        print('cur_name:', cur_name)
        file_obj.save(os.path.join('upload/', cur_name))
    extracted_files = unzip(cur_name)
    print('extracted_files:', extracted_files)
    return "successfully"


def unzip(zip_name):
    dir = 'upload'
    zip_path = os.path.join(dir, zip_name)
    print(zip_path)
    zip_file = zipfile.ZipFile(zip_path)
    print(zip_file.namelist())
    extract_files = [file for file in zip_file.namelist() if
                     file.split('.')[-1] == 'docx' or file.split('.')[-1] == 'pdf']
    folder_path = 'upload/' + zip_name.split('.')[0]
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print('makedir successfully')
    for file in zip_file.namelist():
        zip_file.extract(file, folder_path)
    zip_file.close()
    extracted_files = [os.path.join(folder_path, f) for f in extract_files]
    return extracted_files


if __name__ == '__main__':
    app.run()
