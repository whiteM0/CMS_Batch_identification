import zlib
import json
from lxml import etree
import requests

def whatweb(url):
    response = requests.get(url,verify=False)
    whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
    whatweb_dict = json.dumps(whatweb_dict)
    whatweb_dict = whatweb_dict.encode()
    whatweb_dict = zlib.compress(whatweb_dict)
    data = {"info":whatweb_dict}
    return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

f=open("./target.txt","r")
f1=open("./out.txt","a")

for j in  f.readlines():
    try:
        j=j.replace("\t","")
        j=j.replace("\n","")
        if("http" not in j):
            j="http://"+j
        print(j+"\n")
        a=whatweb(j)
        print(a.content)
        f1.write(a.content+"\n\n")
    except:
        pass