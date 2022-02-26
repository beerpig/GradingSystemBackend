import json
import dict2json
import JWT_demo
import pymysql_demo
import response_result

from flask import Flask, render_template
from flask import request, jsonify
import zipfile
import time
import os
from flask_cors import CORS

app = Flask(__name__,
            template_folder="/Users/beerpig/Downloads/GradingSystem/frontend/dist",
            static_folder="/Users/beerpig/Downloads/GradingSystem/frontend/dist/static"
            )

CORS(app)


@app.before_request
def before():
    print(request.path)
    if request.path == '/login' or request.path == '/getUserName' or request.path.startswith(
            "/static") or request.path == '/register' or request.path == '/':
        return None
    token = request.headers.get('token')
    user = request.headers.get('user')
    select_token_sql = "select * from userToken where userName=%s"
    sql_token = pymysql_demo.select_token(select_token_sql, [user])
    if token != sql_token:
        result = response_result.TOKEN_NOPASS
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        return jsonify(result)


# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/tokenAvailable', methods=["POST"])
def token_available():
    req = request
    print(req)
    return {'state': 402}, 401


@app.route('/getUserName', methods=["GET"])
def get_username():
    # request.headers.get('token')
    username = request.args.get('user')
    print('username:', username)
    return {'success': 'true'}, 200


@app.route('/login', methods=["POST"])
def login():
    req = request
    str_req_data = req.data.decode('UTF-8')
    json_req_data = json.loads(str_req_data)
    username = json_req_data['name']
    password = json_req_data['pwd']
    token = JWT_demo.generate_access_token(username)
    sql_login = "select * from user where userName = %s and password = %s"
    res = pymysql_demo.select_user_login(sql_login, [username, password])
    if res:
        result = response_result.LOGIN_SUCCESS
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        return jsonify(result)
    return jsonify(response_result.LOGIN_FAILURE)


@app.route('/register', methods=["POST"])
def register():
    req = request
    str_req_data = req.data.decode('UTF-8')
    json_req_data = json.loads(str_req_data)
    username = json_req_data['name']
    password = json_req_data['pwd']
    phone = json_req_data['phone']
    # captcha = 1111
    password_md5 = pymysql_demo.encode_(password)
    sql_register = "insert into user (userName, password, phone, create_time) values (%s, %s, %s, now())"
    res = pymysql_demo.user_insert(sql_register, [username, password_md5, phone])
    if res:
        return jsonify(response_result.REGISTER_SUCCESS)
    return jsonify(response_result.REGISTER_FAILURE)


@app.route('/captchaLaunch', methods=["POST"])
def captcha_launch():
    req = request
    str_req_data = req.data.decode('UTF-8')
    json_req_data = json.loads(str_req_data)
    phone = json_req_data['phone']
    data = {"token": "sdafjsld", "success": "true"}
    response = json.dumps(data)
    return response, 200, {"ContentType": "application/json"}


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
    # 把 res 改成生成的数据
    res = dict2json.dic
    responses = res
    responses["msg"] = "successfully"
    data = json.dumps(responses)
    return data, 200, {"ContentType": "application/json"}


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
