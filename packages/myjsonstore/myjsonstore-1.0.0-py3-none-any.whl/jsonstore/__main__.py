# local imports
from jsonstore.storage import SingleKeyStorage as Client
from jsonstore import msg, util
# other imports
import argparse

def parse_args():
	p = argparse.ArgumentParser()
	p.add_argument(
		"-u","--upload",
		help=("Upload a file. Usage: -u path/to/file.txt"))
	p.add_argument(
		"-d","--download",
		help=("Download a file. Usage: -d token/count"))
	args = p.parse_args()
	if args.upload and args.download:
		p.error(msg.alert("Cannot upload and download at the same time"))
	if (not args.upload) and (not args.download):
		p.error(msg.alert("Nothing to do. Specify either -u/-d"))
	return args

def main(args):
	if args.upload:
		try:
			fd = open(args.upload,"rb").read()
			k, c = Client(verbose=False).store(fd)
			print(k+'/'+str(c))
			return 0
		except Exception as e:
			print(msg.alert("Cannot upload file [%s]" % args.upload))
			print(msg.star(str(e)))
			return 1
	elif args.download:
		try:
			k, c = args.download.split('/')
			c = int(c)
			res = Client(verbose=False).retrieve(k, c)
			util.printraw(res)
			return 0
		except Exception as e:
			print(msg.alert("Cannot download file with k/c: "+args.download))
			print(msg.star(str(e)))
			return 1

if __name__ == "__main__":
	exit(main(parse_args()))
