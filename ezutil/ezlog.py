import logging
from datetime import datetime
import traceback,sys
import pdb

def TRACE(timed, verbose=False):
	#print ("timed is {0}, verbose is {1}".format(timed, verbose))
	def decorator(fun):
		def wrapped(*args, **kargs):
			if verbose: print("in {0}".format(fun.__name__))
			if timed:
				o = fun(*args,**kargs)
			else:
				o = fun(*args,**kargs)
			return o
		return wrapped
	return decorator

def dump_args(func):
    "This decorator dumps out the arguments passed to a function before calling it"
    argnames = func.func_code.co_varnames[:func.func_code.co_argcount]
    fname = func.func_name

    def echo_func(*args,**kwargs):
        print fname, ":", ', '.join(
            '%s=%r' % entry
            for entry in zip(argnames,args) + kwargs.items())
        return func(*args, **kwargs)

    return echo_func

class TimeFormatter(logging.Formatter):
	def formatTime(self,record, datefmt=None):
		dt = datetime.now()
		return "[{0}]".format(dt.strftime("%y%m%d-%H%M%S-%f"))

def getstack(msg=None):
	ret = "{0}\n>>>>>\n".format(msg)
	stacks = traceback.extract_stack()
	for s in stacks[:-1]:
		i = "{0:<16}{2:<8}{1:>5}|{3}\n".format(*s)
		ret += i
	return ret+"<<<<<<\n"


def logger(name="xeven"):
	_ezlog = logging.getLogger(name)
	_ezlog.setLevel(logging.DEBUG)
	fh = logging.FileHandler('xeven.log')
	fh.setLevel(logging.DEBUG)
	formatter = TimeFormatter('%(name)s %(asctime)s %(filename)s - %(funcName)s : %(lineno)s\n==> %(message)s')
	fh.setFormatter(formatter)
	_ezlog.addHandler(fh)
	pdb.set_trace()
	return _ezlog

def tracelogger(name="xeven"):
	_ezlog = logging.getLogger(name)
	_ezlog.setLevel(logging.DEBUG)
	fh = logging.FileHandler('xeven_trace.log')
	fh.setLevel(logging.DEBUG)
	formatter = TimeFormatter('FROM %(name)s %(asctime)s %(filename)s %(message)s')
	fh.setFormatter(formatter)
	_ezlog.addHandler(fh)

	return _ezlog

@TRACE(True)
def helloworld(a,b):
	print a, b

@dump_args
def f1(a,b,c):
    print a + b + c

def main():
	#a = logger()
	#a.debug("hello")
	#b = tracelogger()
	#b.debug(getstack())
	#a.warn("this is warning")
	#a.error("this is error")
	#a.critical("ciritical error")
	helloworld("1","sdf")
	f1(1,2,4)

if __name__ == '__main__':
	main()

