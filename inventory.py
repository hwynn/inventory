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

menu = "1) Check inventory\n2) Add item to inventory\n3) Remove item from inventory"
print(menu);
inventory = {}

valid = False;
while(valid!=True):
	str1 = input("Select an option: ");
	valid = isValid(str1)
print ("Received input is : ", str1);