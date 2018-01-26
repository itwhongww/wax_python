# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import StreamingHttpResponse
# Create your views here.
from django.http import HttpResponse
import time
import random
import logging
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger("django") 
logger.debug("初始化....")
filepath = "/home/sftp_root/shared/weiax/upfiles/wax_file/"
def hello(request):
	logger.debug("初始化hello")
	return HttpResponse('hello')

def tourist(request):
	randomNum = '游客'+time.strftime("%y%m%d%H%M%S", time.localtime()) + str(random.randrange(100,999))
	return HttpResponse(randomNum)

@csrf_exempt
def upload(request):
	try:
		if request.method == "POST":
			file = request.FILES.get("file",None)
			if not file:
				return HttpResponse("没有文件上传")
			
			destination = open(filepath+file.name,'wb+')
			for chunk in file.chunks():
				destination.write(chunk)
			destination.close()
			returnData = {}
			returnData["code"] = 0
			fileName = file.name
			fileName = fileName.encode('unicode-escape').decode('string_escape')
			# fielName = fielName.encode('utf-8').decode('utf-8')
			
			returnData["fileName"] = fileName
			return HttpResponse(str(returnData))
	except Excption as e:
		logger.error(e)

def download(request):
	if request.method == "GET":
		paramName = request.GET.get("fileName")
		the_file_name = filepath + paramName
		# response = StreamingHttpResponse(file_iterator(the_file_name))
		# response['Content-Type']='application/octet-stream'
		# response['Content-Disposition']='attachment;filename="{0}"'.format(paramName)
		logger.debug(0)
		f =open(the_file_name)
		logger.debug(1)
		data = f.read()
		logger.debug(2)
		f.close()
		logger.debug(2.5)
		#以下设置项是为了下载任意类型文件
		response = HttpResponse(data,content_type='APPLICATION/OCTET-STREAM')  
		logger.debug(3)
		response['Content-Disposition'] = 'attachment; filename=%s' %paramName
		logger.debug(34)
		return response

def file_iterator(file_name, chunk_size=512):
		logger.debug(10)
		with open(file_name) as f:
			logger.debug(11)
			while True:
				logger.debug(12)
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break

# the_file_name = filepath + "计数器.txt"
# f =open(the_file_name)
# logger.debug(1)
# data = f.read()
# logger.debug(2)
# f.close()
# logger.debug(2.5)
# #以下设置项是为了下载任意类型文件
# response = HttpResponse(data,content_type='APPLICATION/OCTET-STREAM') 