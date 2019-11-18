
import base64
import json
import sys
import os


def translation():
    str = input('please input Data(value) : ')
    data_json = ""
    file = open('decoding.json', 'w')

    try:
        newStr = str.replace("_", "/").replace("-", "+")
        decodeStr = base64.standard_b64decode(newStr)
        #data_json = decodeStr.decode() #translate the code(string) to unicode
        #json_object = json.load(data_json) #condition, and also a progress
    except:
        print("Error: your data isn't json")


    #return json.dump(decodeStr, file, indent=4, ensure_ascii=False)
    return json.dump(decodeStr, file)


def open_json():
    os.system('/Users/zhengshi/PycharmProjects/TestTools_Python/TeatData/decoding.json')

def main():
    translation()
    open_json()

if __name__ == '__main__':
    main()





