import json

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

num = 0


def helper(data, pid):
    global num
    if isinstance(data, dict):
        l = []
        for (k, v) in data.items():
            num += 1
            dict_tmp = {"pid": pid, "name": str(k), "id": num}
            if isinstance(v, (float, int, str)):
                dict_tmp['data'] = v
            elif isinstance(v, list) and is_list_all_string(v):
                dict_tmp['data'] = v
            else:
                dict_tmp['childlist'] = helper(v, num)
            l.append(dict_tmp)
        return l
    elif isinstance(data, list):
        l = []
        for d in data:
            l.append(helper(d, num))
        return l
            # if isinstance(d, dict):
            #     l = []
            #     for (k, v) in d.items():
            #         num += 1
            #         dict_tmp = {"pid": pid, "name": str(k), "id": num}
            #         if isinstance(v, (float, int, str)):
            #             dict_tmp['data'] = v
            #         elif isinstance(v, list) and is_list_all_string(v):
            #             dict_tmp['data'] = v
            #         else:
            #             dict_tmp['childlist'] = helper(v, num)
            #         l.append(dict_tmp)
            #     return l


def is_list_all_string(l):
    for ll in l:
        if not isinstance(ll, str):
            return False
    return True


# l = helper(dic, 0)
# print(l)
# # l = [{'pid': 0, 'name': 'SCORE', 'id': 1, 'childlist': [{'pid': 1, 'name': 'AI', 'id': 2, 'data': 86.0}, {'pid': 1, 'name': 'TRUES', 'id': 3, 'data': 78}, {'pid': 1, 'name': 'BIAS', 'id': 4, 'data': 8.0}]}, {'pid': 0, 'name': 'FILES', 'id': 5, 'childlist': [{'pid': 5, 'name': 'NAME', 'id': 6, 'data': '互联网+商业计划书 初赛'}, {'pid': 5, 'name': 'LABELS', 'id': 7, 'childlist': [{'pid': 7, 'name': '__label__ACADEMIC', 'id': 8, 'childlist': [{'pid': 8, 'name': 'items', 'id': 9, 'data': ['研究员', '教授', '知名人士', '研究生', '副教授', '专业人士', '副校长', '学院', '大学', '博士', '讲师']}, {'pid': 8, 'name': 'score', 'id': 10, 'data': 1}]}, {'pid': 7, 'name': '__label__INDUSTRIAL', 'id': 11, 'childlist': [{'pid': 11, 'name': 'items', 'id': 12, 'data': ['业界']}, {'pid': 11, 'name': 'score', 'id': 13, 'data': 1}]}, {'pid': 7, 'name': '__label__BUSINESS', 'id': 14, 'childlist': [{'pid': 14, 'name': 'items', 'id': 15, 'data': ['预测', '现状', '前景', '市场潜力', '工业', '营业额', '市场前景', '分析', '营收', '产业', '前瞻性', '销售额', '发展潜力', '规模', '净利润']}, {'pid': 14, 'name': 'score', 'id': 16, 'data': 1}]}, {'pid': 7, 'name': '__label__INVESTMENT', 'id': 17, 'childlist': [{'pid': 17, 'name': 'items', 'id': 18, 'data': ['资源整合', '资金', '投资', '融资', '合作意向', '投融资']}, {'pid': 17, 'name': 'score', 'id': 19, 'data': 1}]}, {'pid': 7, 'name': '__label__PATENTS', 'id': 20, 'childlist': [{'pid': 20, 'name': 'items', 'id': 21, 'data': ['知识产权', '专利', '专利申请', '一等奖', '发明人']}, {'pid': 20, 'name': 'score', 'id': 22, 'data': 1}]}]}, {'pid': 5, 'name': 'ENTITYS', 'id': 23, 'childlist': [{'pid': 23, 'name': 'name', 'id': 24, 'data': '南京航空航天大学'}, {'pid': 23, 'name': 'score', 'id': 25, 'data': 1.25}]}]}]
# for ll in l:
#     print(ll)

