import os

print os.getcwd()

os.chdir("/Users/harry/python_head_first/head_first_dry_run/chapter3")

print os.getcwd()

try:

	stream1 = open('sketch.txt')

	for each_line in stream1:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print role,
			print "said:",
			print line_spoken
		except ValueError:
			pass
except IOError:
	print "the file is missing!"
