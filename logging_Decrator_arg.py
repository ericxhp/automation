# coding=utf-8
#logging module
#argparse module
#decrator
import argparse
import time
from functools import wraps
from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler

parser = argparse.ArgumentParser()

parser.add_argument('--Name',dest='TestName',default="my test")
parser.add_argument('--Author',dest='Author',default="eric")
parser.add_argument('--slope',dest='PLSlope',type=float,default=.2)

args=parser.parse_args()

# print "Test case Name is {}".format(args.TestName)
# print "Test case Owner is {}".format(args.Author)
# print "Slope is {}".format(args.PLSlope)

#Sample code for decorator

def timethis(func):
	@wraps(func)
	def  wrapper(*args,**kwargs):
		start = time.time()
		r = func(*args, **kwargs)
		end = time.time()
		print "Func Name :{}, ExecutionTime:{}".format(func.__name__,end - start)
		return r
	return wrapper


@timethis
def delay(nDelayNum):
	time.sleep(nDelayNum)

def logconfig():
	# 第一步，创建一个logger  
	logger = logging.getLogger()  
	logger.setLevel(logging.INFO)    # Log等级总开关  
  
	# 第二步，创建一个handler，用于写入日志文件  
	logfile = 'myapp.log'  
	# fh = logging.FileHandler(logfile, mode='w')  
	# fh.setLevel(logging.INFO)   # 输出到file的log等级的开关 

	Rthandler = RotatingFileHandler(logfile, maxBytes=10*1024*1024,backupCount=5)
	Rthandler.setLevel(logging.INFO)
	formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
	Rthandler.setFormatter(formatter)
	logging.getLogger('').addHandler(Rthandler) 
  
	# 第三步，再创建一个handler，用于输出到控制台  
	ch = logging.StreamHandler()  
	ch.setLevel(logging.INFO)   # 输出到console的log等级的开关  
  
	# 第四步，定义handler的输出格式  
	#formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
	# formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")  
	# fh.setFormatter(formatter)  
	ch.setFormatter(formatter)  
  
	# 第五步，将logger添加到handler里面  
	#logger.addHandler(fh)  
	logger.addHandler(ch)

def main():

 	logconfig()	
	logging.info('Delay 4 second')
	delay(4)
	logging.info('Test finished')


if __name__ == '__main__':
	main()
