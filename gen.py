#coding=utf-8
import re
import os
import time
import sys

reload(sys) 
sys.setdefaultencoding('utf8')
thedate = '2017-06-22'

inpath = 'D:/iphone/微信消息记录-李雄峰的 iPhone/201706221700-李雄峰/表格格式/支付产品技术交流群.xls'
unpath = unicode(inpath, "utf8")
source=open(unpath)
target = open('D:/github/payment-wechat/chat/_posts/'+thedate+'-chat.markdown', 'w')
target.write('---\n')              
target.write('layout:     post \n')                        
target.write('title:      "'+thedate+'-WeChat\n')
target.write('date:       '+ thedate+' 12:00:00\n')
target.write('author:     "PaymentGroup"\n')   
target.write('tag:		  [chat]\n')   
target.write('header-img: "img/post-bg-wechat.jpg"\n')                           
target.write('---\n')              


try:
	for line in source:
		if len(line)>690 and line[63:67] == 'xl24':
			datetime=line[233:252]
			date = line[233:243]
			time = line[244:252]
			
			pos_end = line.find('</td>', 335)
			name = line[335: pos_end]
			

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			wechat_no = line[pos_start:pos_end]
			
			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			action = line[pos_start:pos_end]

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			msgtype = line[pos_start:pos_end]

			pos_start = line.find('x:str>', pos_end+5) + 6
			pos_end = line.find('</td>', pos_start)
			msg = line[pos_start:pos_end]

			if date == thedate:
				target.write('> '+ time +'  ' + name + '   '+ wechat_no+ '  '+action + '   '+ msgtype + '  \n')
				target.write(msg + '  \n')
finally:
     source.close()

target.flush()
target.close()