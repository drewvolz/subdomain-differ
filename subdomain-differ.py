#!/usr/bin/python3
import difflib, subprocess, sys, os

command = 'python3 ./ctfr.py -d ' + sys.argv[1]
command = command.split()
outfile_name = sys.argv[1] + '.txt'

def run_command(command):
	p = subprocess.Popen(command,
		stdout=subprocess.PIPE,
		stderr=subprocess.STDOUT
	)
	return iter(p.stdout.readline, b'')

def get_original_subdomains():
	original = ''
	if os.path.exists(outfile_name):
		old_data = open(outfile_name, 'r')
		for line in old_data:
			original += (line.strip() + '\n')
	return original.rstrip()

def get_current_subdomains():
	current_subdomains = ''
	for line in run_command(command):
		bytesLine = line.decode('ascii')
		cleanerLine = bytesLine.strip()
		current_subdomains += (cleanerLine + '\n')
	return current_subdomains.rstrip()

def write_current_to_file(current):
	with open(outfile_name, 'w') as text_file:
		print(current, file=text_file)

def unidiff_output(original, current):
	original = original.splitlines(1)
	current = current.splitlines(1)
	diff = difflib.unified_diff(original, current)
	finalDiff = ''.join(diff)
	if len(finalDiff) < 1:
		print('No changes.')
	else:
		print(finalDiff)

def run():
	original = get_original_subdomains()
	current = get_current_subdomains()
	write_current_to_file(current)
	unidiff_output(original, current)

if __name__ == '__main__':
	run()
