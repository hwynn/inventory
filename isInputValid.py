def isValid(x):
	"Tests if the input is proper"
	if(x.isdigit()):
		if((int(x)>=1)and(int(x)<=5)):
			return(True);
		else:
			print("Input must be between 1 and 5");
			return(False);
	else:
		print("Input must a number");
		return(False);

def giveValid():
	valid = False;
	while(valid!=True):
		str1 = input("Enter your input: ");
		valid = isValid(str1)
	return(str1);