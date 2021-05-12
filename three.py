try:
	f = open('simple.txt','w')
	f.write("Test write to simple test!")
except IOError:asprint("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
	print("SUCCESS!")
	f.close()

