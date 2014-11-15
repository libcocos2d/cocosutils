import sys
import getopt

VERSION = "1.0"

def usage():
	print "Usage: " +  sys.argv[0] + " [OPTIONS]"
	#todo: get usage from all the plugins
	sys.exit(1)


def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "version"])
	except getopt.GetoptError, err:
		# print help information and exit:
		print(err) # will print something like "option -a not recognized"
		sys.exit(-1)

	for o, a in opts:
		if o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-V", "--version"):
			print VERSION
			sys.exit(0)
		else:
			assert False, "unhandled option"
			sys.exit(-1)

	argc = len(sys.argv)
	if argc == 0:
		usage()
