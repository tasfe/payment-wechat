#coding=utf-8
import re
import os
import time
import sys
import cgi

reload(sys) 
sys.setdefaultencoding('utf8')

import codecs

if len(sys.argv) < 2 :
  print('python gen.py 2017-06-21')
  sys.exit()

thedate = sys.argv[1] 

## 导出路径
root_path = u'D:/iphone/微信消息记录-李雄峰的 iPhone/'

## 最新的文件路径
last_folder = u' '

## 文件相对路径的位置
sub_path = u'/表格格式/支付产品技术交流群.xls'

## 寻找最近日期的xls文件

for cur_folder in os.listdir(root_path):
	if cmp(cur_folder, last_folder)>0 and  os.path.exists(root_path + cur_folder + sub_path):
		last_folder = cur_folder
	
unpath = root_path + last_folder + sub_path

print('使用最新文件: '+ unpath +'\n')

## unpath = unicode(inpath, "utf8")

source=open(unpath)
target = codecs.open(r'D:/github/payment-wechat/wechat/_posts/'+thedate+'-chat.markdown', 'w', encoding = 'utf-8', errors='ignore')
target.write(u'---\n')              
target.write(u'layout:     post \n')                        
target.write(u'title:      "'+thedate+'-WeChat"\n')
target.write(u'date:       '+ thedate+' 12:00:00\n')
target.write(u'author:     "PaymentGroup"\n')   
target.write(u'tag:		  [chat]\n')   
target.write(u'header-img: "img/post-bg-wechat.jpg"\n')                           
target.write(u'---\n')              


try:
	for line in source:
		if len(line)>690 and line[63:67] == 'xl24':
			datetime=line[233:252]
			date = line[233:243]
			time = line[244:252]
			
			pos_end = line.find('</td>', 335)
			name = line[335: pos_end].decode('gbk', errors='ignore').encode('utf-8')
			

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			wechat_no = line[pos_start:pos_end]
			
			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			action = line[pos_start:pos_end].decode('gbk', errors='ignore').encode('utf-8')

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			msgtype = line[pos_start:pos_end].decode('gbk', errors='ignore').encode('utf-8')

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			msg = cgi.escape(line[pos_start:pos_end]).decode('gbk', errors='ignore').encode('utf-8')

			if date == thedate and msgtype == u'文本':
				target.write(u'> ')
				target.write(time)
				target.write(u'  ')
				target.write(name)
				# target.write(u'   ')
				# target.write(wechat_no.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('  ')				
				# target.write(action.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('   ')
				# target.write(msgtype.decode('gbk', errors='ignore').encode('utf-8'))
				target.write(u'  \n   \n')				
				target.write(msg + u'  \n   \n')
			if date == thedate and msgtype == u'网页':
				target.write(u'> ')
				target.write(time)
				target.write(u'  ')
				target.write(name)
				# target.write(u'   ')
				# target.write(wechat_no.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('  ')				
				# target.write(action.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('   ')
				# target.write(msgtype.decode('gbk', errors='ignore').encode('utf-8'))
				target.write(u'  \n   \n')				
				target.write(msg + u'  \n   \n')
			if date == thedate and msgtype == unicode('照片壁纸','utf8'):
				target.write(u'> ')
				target.write(time)
				target.write(u'  ')
				target.write(name)
				# target.write(u'   ')
				# target.write(wechat_no.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('  ')				
				# target.write(action.decode('gbk', errors='ignore').encode('utf-8'))
				# target.write('   ')
				# target.write(msgtype.decode('gbk', errors='ignore').encode('utf-8'))
				target.write(u'  \n   \n')
				
				target.write('!['+ datetime + '](http://wechat.lixf.cn/img/'+ date.replace('-', '')+'_'+ time.replace(':','') + '.png' + ') \n   \n')

finally:
     source.close()

target.flush()
target.close()

print('完成导出：'+ unpath +'\n')