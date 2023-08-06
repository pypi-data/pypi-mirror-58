import pyking.docs.tutext as tut
import pyking.docs.matext as matext


def creat():
    with open('1TuJson.py', 'wt', encoding='utf-8') as f:
        f.write(tut.text1)
    with open('1TuSdk.py', 'wt', encoding='utf-8') as f:
        f.write(tut.text2)
    with open('1Tu普通接口.py', 'wt', encoding='utf-8') as f:
        f.write(tut.text3)
    with open('Tu常用接口文档.md', 'wt', encoding='utf-8') as f:
        f.write(tut.text4)

    with open('matdoc.md', 'wt', encoding='utf-8') as f:
        f.write(matext.text1)
    with open('1paint.py', 'wt', encoding='utf-8') as f:
        f.write(matext.text2)
    with open('2paint.py', 'wt', encoding='utf-8') as f:
        f.write(matext.text3)
    with open('3paint.py', 'wt', encoding='utf-8') as f:
        f.write(matext.text4)
    with open('4paint-zhexian.py', 'wt', encoding='utf-8') as f:
        f.write(matext.text5)

    return
