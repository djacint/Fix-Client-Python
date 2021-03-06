import quickfix
import sys

def main(fileName):
	if len(sys.argv) < 2: 
		return
	fileName = sys.argv[1]

	try:
			settings = quickfix.SessionSettings(fileName)
			application = quickfix.MyApplication()
			storeFactory = quickfix.FileStoreFactory(settings)
			logFactory = quickfix.FileLogFactory(settings)
			acceptor = quickfix.SocketAcceptor(application, storeFactory, settings, logFactory)
			acceptor.start()
			# while condition == true: do something
			acceptor.stop()
	except quickfix.ConfigError, e:
			print e
