#!/usr/python
# coding=utf-8
import os, json, codecs

# 需要检查的格式
FileExt = ['png', 'jpg']
# 不需要抽查的文件夹
DirExt = []

rmap = []

KEY_PATH = '/Users/chaohuawu/Documents/SVN/com/fytx2/code/trunk/project/res/'
Save_PATH = '/Users/chaohuawu/Documents/SVN/com/fytx2/code/trunk/project/res/1.json'

# 遍历文件夹
def getFile(path):
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                # find dir todo ..
                if item in DirExt:
                    # not in DirExt
                    continue

                getFile(full_path)

            file_ext = item.split(".")[-1]
            if file_ext not in FileExt:
                # not in FileExt
                continue

            print(full_path)
            key = os.path.relpath(full_path, KEY_PATH)
            rmap.append(key)
    except Exception, ex:
        print ex  

getFile('/Users/chaohuawu/Documents/SVN/com/fytx2/code/trunk/project/res/ccbResources/guozhan/guozhan_bg')
getFile('/Users/chaohuawu/Documents/SVN/com/fytx2/code/trunk/project/res/ccbResources/guozhan/guozhan_bg2')
getFile('/Users/chaohuawu/Documents/SVN/com/fytx2/code/trunk/project/res/ccbResources/zhucheng/zhucheng_cj')
print rmap
json.dump(obj=rmap,fp=codecs.open(Save_PATH , "w", encoding="utf-8"), indent=2, sort_keys=True, ensure_ascii=False, encoding='utf-8')