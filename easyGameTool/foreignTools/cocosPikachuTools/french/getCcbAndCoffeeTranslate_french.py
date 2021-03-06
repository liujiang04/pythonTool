# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 下午8:14


'''
    从mysql 里面 直接提取 数据  复制到两个 translate 文件夹里面


'''

import os
import json
import pymysql
import shutil

projectFile = "/Users/admin/Documents/ljworkspace/local/cocos/project/pikachu_french/pikachu_english/app/static/"

def createJsonFile(jsonObj,fileName):

    with open(fileName + ".json", 'w') as f:
        json.dump(jsonObj, f, sort_keys=True, indent=4, separators=(',', ':'))

def makeCcbTranslate():
    print("begin makeCcbTranslate")
    # 打开数据库连接
    # db = pymysql.connect("192.168.1.207", "root", "", "CHARACTER_SETS")
    db = pymysql.connect(host='192.168.1.207', port=3306, user='root', passwd='', db='foreign-project')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT Id,French from ccbTranslate WHERE Id IS NOT NULL and Id != 0 and French is not NULL"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        obj = {}
        obj["RECORDS"] = []

        for row in results:
            itme = {}
            itme["Id"] = str(row[0])
            itme["text"] = str(row[1])
            obj["RECORDS"].append(itme)
        createJsonFile(obj,"ccbTranslate")

    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    print("begin makeCcbTranslate success")

def makeCoffeeTranslate():
    print("begin makeCoffeeTranslate")
    # 打开数据库连接
    # db = pymysql.connect("192.168.1.207", "root", "", "CHARACTER_SETS")
    db = pymysql.connect(host='192.168.1.207', port=3306, user='root', passwd='', db='foreign-project')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT Id,French from coffeeTranslate6 WHERE Id IS NOT NULL and Id != 0 and French is not NULL"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        obj = {}
        obj["RECORDS"] = []

        for row in results:
            itme = {}
            itme["Id"]= str(row[0])
            itme["text"] = str(row[1])
            obj["RECORDS"].append(itme)
        createJsonFile(obj,"coffeeTranslate")

    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    print("begin makeCoffeeTranslate success")


def copyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            '''创建路径'''
            mkdir(fpath)
        '''复制文件'''
        "".replace("png","txt").replace("jpg","txt")
        shutil.copyfile(srcfile, dstfile)
        print("copy %s -> %s" % (srcfile, dstfile))


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False


if __name__ == '__main__':
    makeCcbTranslate()
    makeCoffeeTranslate()
    copyfile("coffeeTranslate.json",projectFile+ "res/coffeeTranslate.json")
    copyfile("ccbTranslate.json",projectFile+ "res/ccbTranslate.json")


