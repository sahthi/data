
from VTAT_TOOL.models import Repository

def run(*args):
	print args
	if args:
		with open(args[0]) as fp:
			data = fp.readlines()
		print data
	names = Repository.objects.values_list('repository_name', flat=True)
	print names
