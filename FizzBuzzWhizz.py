#-*- coding: UTF-8 -*-
#平台 windows mac linux均可，使用Python 2.7
#
import sys

def verify_input(input_numbers):
	#判断输入是否合法
	if len(input_numbers) == 3:
		#判断是否为三个字符
		for i in xrange(0,len(input_numbers),1):
			try:
				input_numbers[i] = int(input_numbers[i])
				#判断是否为数字
			except ValueError:
				return False
			if input_numbers[i] < 1 or input_numbers[i] > 9:
				#判断是否为一位非零正整数
				return False
	else: 
		return False
	return True

def output_result(num_x,input_s):
	#输出函数
	num_str = []
	num_str.append(num_x/100)
	num_str.append(num_x/10 - num_str[0]*10)
	num_str.append(num_x - num_str[0]*100 -num_str[1]*10)
	if num_str[0] == input_s[0] or num_str[1] == input_s[0] or num_str[2] == input_s[0]:
		#条件5
		print u"Fizz"
		return
	else:
		#条件3,4同时完成
		if num_x%input_s[0] == 0:
			sys.stdout.softspace= 0
			print u"Fizz",
		if num_x%input_s[1] == 0:
			sys.stdout.softspace= 0
			print u"Buzz",
		if num_x%input_s[2] == 0:
			sys.stdout.softspace= 0
			print u"Whizz",
		if num_x%input_s[0] != 0 and num_x%input_s[1] != 0 and num_x%input_s[2] != 0 :
			#不满足条件3,4,5的输出原数
			print num_x
		if num_x%input_s[0] == 0 or num_x%input_s[1] == 0 or num_x%input_s[2] == 0 :
			#为满足条件3,的输出补一个回车
			print ""
		return

while (1):
	input_nums = raw_input(u"Please input 3 special numbers(','for split):")
	input_list = input_nums.split(",")
	#输入并分割为三个独立的特殊数
	if verify_input(input_list):
		#调用判断函数，满足即跳出输入循环
		break
	else:
		print(u"Input error! Please input again!")
		continue
for i in xrange(100):
	#调用输出函数
	x = i+1
	output_result(x,input_list)
#程序完成，暂停
raw_input('Press any key and Enter to continue ~!')