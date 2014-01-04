import string
import random
import getpass
import sys
import urllib
import hashlib
import os
import time
import pyperclip

from zenlib import *

# supported algorithms

MD5 = "MD5"
SHA1 = "SHA-1"
SHA256 = "SHA-256"
SHA512 = "SHA-512"

def getTerminalSize():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])

screen_width, screen_height = getTerminalSize()
center_width = screen_width

def main():

	isDictionarySet = False

	DICT_FILE = None
	ATK_MET = "DHS"

	try:
		f_config = open(os.path.dirname(os.path.realpath(__file__)) + "\\config\\config.dat", 'r')
		readall = f_config.read()

		settings = readall.split('\n')

		for z in range(len(settings)):
			if "method" in settings[z]:
				if settings[z].split('=')[1] == "DHS":
					print "[Zen@STARTUP]: Using DHS as cracking method."
					ATK_MET = "DHS"
				elif settings[z].split('=')[1] == "PLHS":
					print "[Zen@STARTUP]: PLHS is still not available. Using DHS for cracking."
					ATK_MET = "DHS"
				else:
					print "[Zen@STARTUP]: Unrecognized cracking method in config file. Using DHS as default."
					ATK_MET = "DHS"
			elif "dict" in settings[z]:
				try:
					f = open(settings[z].split('=')[1], 'r')
					f.close()
					DICT_FILE = settings[z].split('=')[1]

					isDictionarySet = True

					print "[Zen@STARTUP]: Dictionary file found! Using for cracking."
				except:
					print "[Zen@STARTUP]: Dictionary file not found! Will be asked later."
					DICT_FILE = None

					isDictionarySet = False
			elif "chunk_size" in settings[z]:
				CHUNK_SIZE = settings[z].split('=')[1]
				print "[Zen@STARTUP]: Using extract chunk size of: " + CHUNK_SIZE


		try:
			CHUNK_SIZE
		except NameError:
			CHUNK_SIZE = 1024

	except IOError:
		ATK_MET = "DHS"
		DICT_FILE = None
		isDictionarySet = False
		CHUNK_SIZE = 1024
		print "[!] Config file not found, all set to default."

	print
	print string.center("## ZenCracker ##", center_width)
	print string.center("-=[ v. 1.1 - follow me on twitter: @jndok ]=-", center_width)
	print string.center("lib v. 0.4 | algorithm v. 0.4", center_width)

	print
	print

	print "[Zen@STARTUP]: Type \'help\' to get help.\n"

	while 1:
		ans = raw_input(">>> ")

		if ans.lower() == "help":
			print "## HELP MENU ##\n"

			print "\'open\': Loads up a dictionary for the cracking attempt. This is the first command to be issued."
			print "\'hash\': Takes the hash to crack as input. This is the second command to be issued."
			print "\'quit\': Quits the program."
		elif ans.lower() == "open":

			if DICT_FILE == None:
				pass
			else:
				print "[Zen@EXECUTION]: Dictionary already set!"
				continue

			file1 = raw_input("[Zen@EXECUTION]: File to open (drag&drop supported): ")
			try:
				f = open(file1, 'r')
				#print f.read()
				f.close()

				isDictionarySet = True
				DICT_FILE = file1

			except IOError:
				print "[!] Error: File not found!"
				pass
		elif ans.lower() == "hash":
			hash1 = raw_input("[Zen@EXECUTION]: Insert hash to crack: ")

			hash_alg = detectAlgorithm(hash1)
			if hash_alg == None:
				print "[!] Error: Hash algorithm is not supported. Aborting."
				sys.exit(0)

			if isDictionarySet == True:
				print "\n\n[Zen@EXECUTION]: Dictionary and hash have been set. Cracking is ready to begin."
				print "[Zen@EXECUTION]: Hash algorithm may be " + hash_alg + "."
				print "[Zen@EXECUTION]: Attacking method is set to DHS. Press ENTER to begin the attack...\n"

				os.system("PAUSE")

				for i in range(4):
					sys.stdout.write("\rAttempting to crack the hash, please wait{0}".format("."*i))
					sys.stdout.flush()
					time.sleep(0.5)

				print

				DHS(hash1, DICT_FILE, hash_alg)

				print Fore.RED + "\n[Zen@CRACKING]: Hash NOT found! The password cannot be found in the specified dictionary. Try with a new one." + Fore.RESET

			else:
				print "[Zen@EXECUTION]: Dictionary for cracking is not set. Please set dictionary first."
				pass
		elif ans.lower() == "quit":
			sys.exit(0)
		elif ans.lower() == '':
			pass
		else:
			print "[Zen@EXECUTION]: Unrecognized command. \'help\' to get help."

	#with open("C:\\dict.txt") as FileObj:
		#for lines in FileObj:
			#print lines


if __name__ == '__main__':
	main()