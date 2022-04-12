import random

from fitz import fitz
import datetime


def pdf_text(f_path, username):
    doc = fitz.open(f_path)
    page = doc[0]

    page.draw_rect((100, 100, 200, 200), color=(1, 1, 1), fill=(1, 1, 1), width=0)  # 方法1绘制白色无框矩形覆盖地址
    ff = page.insert_font(fontname="HT", fontfile=r"Arial Unicode.ttf", fontbuffer=None,
                          set_simple=False)  # 定义黑体
    fs = 16
    if len(list(username.encode('gbk'))) > 10:
        fs = 16 - (len(list(username.encode('gbk'))) - 10) * 1.2
        print("fs:", fs)
    page.insert_text((185, 465), username, fontname="HT", fontsize=fs, color=(0, 0, 0, 1), fill=None, render_mode=0,
                     border_width=1, rotate=0, morph=None, overlay=True)
    number = authorized_code_generate()
    page.insert_text((210, 615), number, fontname="HT", fontsize=16, color=(0, 0, 0, 1), fill=None, render_mode=0,
                     border_width=1, rotate=0, morph=None, overlay=True)
    now = datetime.datetime.today()
    year = now.year
    month = now.month
    if month < 10:
        month = '0' + str(month)
    today = now.day
    if today < 10:
        today = '0' + str(today)
    page.insert_text((348, 710), str(year), fontname="HT", fontsize=14, color=(0, 0, 0, 1), fill=None, render_mode=0,
                     border_width=1, rotate=0, morph=None, overlay=True)
    page.insert_text((393, 710), str(month), fontname="HT", fontsize=14, color=(0, 0, 0, 1), fill=None, render_mode=0,
                     border_width=1, rotate=0, morph=None, overlay=True)
    page.insert_text((422, 710), str(today), fontname="HT", fontsize=14, color=(0, 0, 0, 1), fill=None, render_mode=0,
                     border_width=1, rotate=0, morph=None, overlay=True)
    doc.save(r"a.pdf", garbage=4, deflate=True)


def authorized_code_generate():
    prefix = "MITEC 2022 "
    r = random.randint(1, 9999)
    r_str = str(r)
    r_code = '0' * (4 - len(r_str)) + str(r_str)
    code = prefix + r_code
    return code


pdf_text("certificate.pdf", "啤酒beerpig")
# authorized_code_generate()
