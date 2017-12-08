#!/usr/bin/python
# 功能：创建一个新文件并写入文本
# 代码来源：网上随便找的
import os      # python的标准库中的os模块包含普遍的操作系统功能。如果希望程序能够在不同的平台上运行，os模块尤为重要。
ls=os.linesep  # 字符串给出当前平台使用的行终止符。例如，windows使用'\r\n',linux使用'\n'而mac使用'\r'
# get filename
while True:
	fname=input('Input an unused file name >') # 从键盘输入文件名
	if os.path.exists(fname):
		print("ERROR: '%s' already exists" %fname)
	else:
		break;

# get file content lines
all=[]
print("\nEnter lines('.'by itself to quit).\n")

# loop untill user terminates input
while True:
	entry=input('>')
	if entry=='.':
		break;
	else:
		all.append(entry)

# write lines to file with proper line-ending
fobj=open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all]) # 这个列表解析，把每行字符加上一个行结束符写入到文件里
fobj.close()
print('Done!')

