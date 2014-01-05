#####################################
#                      __ __ __     #
#  .-----.-----.-----.|  |__|  |--. #
#  |-- __|  -__|     ||  |  |  _  | #
#  |_____|_____|__|__||__|__|_____| #
#                                   #
#         -=[v. 0.4 BETA]=-         #
#                                   #
#    Follow me on Twitter: @jndok   #
#                                   #
# please, if you don not know what  #
# you are doing, DO NOT fuck any-   #
# thing up. Thanks.                 # 
#####################################

# WORKS ON OS X, JUST CHANGE THE FOLDERS

import os
import hashlib
import sys
import math
import time
import getpass

from timeit import default_timer
#from colorama import Fore, init

#init()

MD5 = "MD5"
SHA1 = "SHA-1"
SHA256 = "SHA-256"
SHA512 = "SHA-512"

usr = getpass.getuser()

__all__ = ['logToFile', 'DHS', 'detectAlgorithm', 'chunkRead'] # do not add PLHS and __PLHS_CRACK

def logToFile(msg):

	try:
		f = open(os.path.dirname(os.path.realpath(__file__)) + "\\log.txt", 'a+')
		f.write(msg)
		f.close()
	except IOError:
		f = open(os.path.dirname(os.path.realpath(__file__)) + "\\log.txt", 'w')
		f.write(msg)
		f.close()

def DHS(given_hash, dictionary, hash_type):

	if hash_type == MD5:
		# probably best option

		f = open(dictionary, 'r')

		start = default_timer()

		for piece in chunkRead(f):
			hash_list = piece.split('\n')

			#print hash_list

			for z in range(len(hash_list)):
				m = hashlib.md5()
				m.update(hash_list[z])

				#print "[+] Trying hash: " + m.hexdigest()

				if m.hexdigest() == given_hash:
					dur = default_timer() - start
					print "\n[Zen@CRACKING]: Hash found! The password has been cracked. Password: " + str(hash_list[z])
					print "[Zen@CRACKING]: Hash has been cracked in: " + str(math.ceil(dur*100)/100) + "s."
					sys.exit(0)
				else:
					pass
	elif hash_type == SHA1:
		f = open(dictionary, 'r')

		start = default_timer()

		for piece in chunkRead(f):
			hash_list = piece.split('\n')

			#print hash_list

			for z in range(len(hash_list)):
				s = hashlib.sha1()
				s.update(hash_list[z])

				#print "[+] Trying hash: " + m.hexdigest()

				if s.hexdigest() == given_hash:
					dur = default_timer() - start
					print "\n[Zen@CRACKING]: Hash found! The password has been cracked. Password: " + str(hash_list[z])
					print "[Zen@CRACKING]: Hash has been cracked in: " + str(math.ceil(dur*100)/100) + "s."
					sys.exit(0)
				else:
					pass
	elif hash_type == SHA256:
		f = open(dictionary, 'r')

		start = default_timer()

		for piece in chunkRead(f):
			hash_list = piece.split('\n')

			#print hash_list

			for z in range(len(hash_list)):
				s256 = hashlib.sha256()
				s256.update(hash_list[z])

				#print "[+] Trying hash: " + m.hexdigest()

				if s256.hexdigest() == given_hash:
					dur = default_timer() - start
					print "\n[Zen@CRACKING]: Hash found! The password has been cracked. Password: " + str(hash_list[z])
					print "[Zen@CRACKING]: Hash has been cracked in: " + str(math.ceil(dur*100)/100) + "s."
					sys.exit(0)
				else:
					pass
	elif hash_type == SHA512:
		f = open(dictionary, 'r')

		start = default_timer()

		for piece in chunkRead(f):
			hash_list = piece.split('\n')

			#print hash_list

			for z in range(len(hash_list)):
				s512 = hashlib.sha512()
				s512.update(hash_list[z])

				#print "[+] Trying hash: " + m.hexdigest()

				if s512.hexdigest() == given_hash:
					dur = default_timer() - start
					print "\n[Zen@CRACKING]: Hash found! The password has been cracked. Password: " + str(hash_list[z])
					print "[Zen@CRACKING]: Hash has been cracked in: " + str(math.ceil(dur*100)/100) + "s."
					sys.exit(0)
				else:
					pass

#def PLHS(given_hash, dictionary, hash_type, hasBeenWritten): # WARNING: THIS FUNCTION IS NOT COMPLETED YET, DO NOT USE IN CRACKING
#
#	if hasBeenWritten == True:
#		print "[Zen@CRACKING]: Hashtabs already written. Skipping to cracking."
#		#__PLHS_CRACK()
#	if hash_type == MD5:
#		j = 0
#		f = open(dictionary, 'r')
#
#		for piece in chunkRead(f):
#			hashtab = piece.split('\n')
#
#			f1 = open("C:\\Users\\" + usr + "\\Desktop\\plhs\\hashtab_" + str(j) + ".txt", 'w')
#			j += 1
#
#			for z in range(len(hashtab)):
#				m = hashlib.md5()
#				m.update(hashtab[z])
#				f1.write(m.hexdigest() + ':' + hashtab[z] + '\n')
#
#		__PLHS_CRACK("C:\\Users\\" + usr + "\\Desktop\\plhs\\", j)
#
#def __PLHS_CRACK(_dir, fnum): # WARNING: THIS FUNCTION IS NOT COMPLETED YET, DO NOT USE IN CRACKING
#
#	print fnum
#
#	for z in range(fnum): # bugs if number of hashtabs is 1
#		f = open(_dir + 'hashtab_' + str(z) + '.txt', 'r')
#		inp = f.read()
#		print inp

def detectAlgorithm(_hash):

	if len(_hash) == 32:
		return MD5
	elif len(_hash) == 40:
		return SHA1
	elif len(_hash) == 64:
		return SHA256
	elif len(_hash) == 128:
		return SHA512
	else:
		return None

def chunkRead(f_obj, chunk=1024):

	while 1:
		data = f_obj.read(chunk)
		if not data:
			break
		yield data
