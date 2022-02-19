from flask import Flask, render_template, request
import zipfile

app = Flask(__name__)

from test import *


@app.route('/')
def index():
    return 'hello!'


dic = {
    "SCORE": {
        "AI": 86.0,
        "TRUES": 78,
        "BIAS": 8.0
    },
    "FILES": [
        {
            "NAME": "互联网+商业计划书 初赛",
            "LABELS": {
                "__label__ACADEMIC": {
                    "items": [
                        "研究员",
                        "教授",
                        "知名人士",
                        "研究生",
                        "副教授",
                        "专业人士",
                        "副校长",
                        "学院",
                        "大学",
                        "博士",
                        "讲师"
                    ],
                    "score": 1
                },
                "__label__INDUSTRIAL": {
                    "items": [
                        "业界"
                    ],
                    "score": 1
                },
                "__label__BUSINESS": {
                    "items": [
                        "预测",
                        "现状",
                        "前景",
                        "市场潜力",
                        "工业",
                        "营业额",
                        "市场前景",
                        "分析",
                        "营收",
                        "产业",
                        "前瞻性",
                        "销售额",
                        "发展潜力",
                        "规模",
                        "净利润"
                    ],
                    "score": 1
                },
                "__label__INVESTMENT": {
                    "items": [
                        "资源整合",
                        "资金",
                        "投资",
                        "融资",
                        "合作意向",
                        "投融资"
                    ],
                    "score": 1
                },
                "__label__PATENTS": {
                    "items": [
                        "知识产权",
                        "专利",
                        "专利申请",
                        "一等奖",
                        "发明人"
                    ],
                    "score": 1
                }
            },
            "ENTITYS": [
                {
                    "name": "南京航空航天大学",
                    "score": 1.25
                },
                {
                    "name": "董事长",
                    "score": 2
                },
                {
                    "name": "上海大学",
                    "score": 1.25
                },
                {
                    "name": "校长",
                    "score": 2
                },
                {
                    "name": "上海外国语大学",
                    "score": 1.25
                },
                {
                    "name": "教授",
                    "score": 1.5
                },
                {
                    "name": "北京航空航天大学",
                    "score": 1.5
                },
                {
                    "name": "副教授",
                    "score": 1.25
                },
                {
                    "name": "西北工业大学",
                    "score": 1.5
                },
                {
                    "name": "专利",
                    "score": 1.5
                },
                {
                    "name": "一等奖",
                    "score": 2
                }
            ]
        },
        {
            "NAME": "备赛报名表Application form 青空计划",
            "LABELS": {
                "__label__ACADEMIC": {
                    "items": [],
                    "score": 0
                },
                "__label__INDUSTRIAL": {
                    "items": [],
                    "score": 0
                },
                "__label__BUSINESS": {
                    "items": [
                        "产业"
                    ],
                    "score": 1
                },
                "__label__INVESTMENT": {
                    "items": [],
                    "score": 0
                },
                "__label__PATENTS": {
                    "items": [
                        "一等奖"
                    ],
                    "score": 1
                }
            },
            "ENTITYS": [
                {
                    "name": "一等奖",
                    "score": 2
                }
            ]
        }
    ]
}


@app.route('/file/upload/', methods=['POST'])
def upload_file():
    json = {}
    print(request.args)
    f = request.files.get('filename')
    fname = f.filename
    type = judge_file(fname)
    if (type):
        # f.save('../data/var/www/uploads/' + (f.filename))
        # upzip(f,type)
        # json = judge_folder('../data/var/www/uploads/')
        json = dic
    else:
        return {
            'code': 500,
            'msg': '文件类型错误',
            'data': json
        }
    return {
        'code': 200,
        'msg': '打分成功',
        'data': json
    }


def upzip(f, type):
    l = ['docx', 'pdf']

    if (type == 'zip'):
        zip_file = zipfile.ZipFile(f)
        zip_list = zip_file.namelist()  # 得到压缩包里所有文件

        for f in zip_list:
            newname = ''
            try:
                newname = f.encode('cp437').decode('gbk')
            except:
                try:  # 此处多进行了一次判断
                    newname = f.encode('cp437').decode('utf-8')
                except:
                    newname = f
            t_l = newname.split('.')
            if (len(t_l) > 0 and type[-1] in l):
                zip_file.extract(f, '../data/var/www/uploads/' + newname)  # 循环解压文件到指定目录
        # with zipfile.ZipFile(f, 'r') as zf:
        #     for info in zf.infolist():
        #         try:
        #             newname=info.filename.encode('cp437').decode('gbk');
        #         except:
        #             try:#此处多进行了一次判断
        #                 newname=info.filename.encode('cp437').decode('utf-8');
        #             except:
        #                 newname=info.filename
        #         outname=newname.split('/')
        #         l=len(outname)
        #     if outname[l-1]!='':#判断解压出来的是否文件夹


def judge_file(fname):
    l = ['docx', 'pdf', 'zip', 'rar']
    type = fname.split('.')[-1].lower()
    if (type not in l):
        return False
    else:
        return type


@app.route('/f/', methods=['POST'])
def search():
    print(request.args)
    f = request.files.get('filename')
    f.save('../data/var/www/uploads/' + (f.filename))
    return 'search'


if __name__ == '__main__':
    app.run()
