BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


print(("""{0}
█▀▀ ▀▀█▀▀ █▀▀▄ █▀▀ █▀▀▄ ▀▀█▀▀   █░░ █▀▀█ █▀▀█ █░█ █░░█ █▀▀█   █▀▀█ █░█ ▀█░█▀
▀▀█ ░░█░░ █░░█ █▀▀ █░░█ ░░█░░   █░░ █░░█ █░░█ █▀▄ █░░█ █░░█   █▄▄▀ █▀▄ ░█▄█░
▀▀▀ ░░▀░░ ▀▀▀░ ▀▀▀ ▀░░▀ ░░▀░░   ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀░▀ ░▀▀▀ █▀▀▀   ▀░▀▀ ▀░▀ ░░▀░░
{1}""").format(RED,END))




while(True):
	try:
		fb=open('all.csv')
		print("\n")
		n=input(("{0}ENTER ID NUMBER :{1}").format(GREEN,END))
		n=n.upper()
		print("\n")
		status=0
		for i in fb:
			if(i.startswith(n)):
				status+=1
				data=i.split(',')
				# print(data)
				print("IDNO 			: ",data[0])
				print("Name 			: ",data[2])
				print("FatherName		: ",data[4])
				print("MotherName		: ",data[5])
				print("SSC HT No		: ",data[1])
				print("DOB 			: ",data[6])
				print("Branch 			: ",data[3])
				print("Mobile Number 		: ",data[7])
				print("Mobile Number		: ",data[8])
				st=''
				for i in range(11,len(data)-1):
					st+=data[i]+","
				print("Address			: ",st[:-1])
				print("UID 			: ",data[-1])

				break
		fb.close()
		if(status==0):
			print(("{0}DATA NOT FOUND").format(RED))
			print("\n")
		print(("{0}If U Wanna continue press{1} 'y'{2}, u dont want to then {3}'n'{4}").format(YELLOW,GREEN,YELLOW,RED,END))
		print("\n")
		ch=input(("{0}ENTER UR CHOICE :{1}").format(MAGENTA,END))
		ch=ch.lower()
		print("\n")
		if(ch=='y'):
			continue
		else:
			exit(0)
	except Exception as e:
		print(e)