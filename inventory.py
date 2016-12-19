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

def invAddItem(x):
	#check if the item is already in inventory
	if(x in inventory):
		inventory[x] = inventory[x] + 1;
	else:
		inventory[x] = 1;
		
def checkInventory():
	print(inventory);

def invRemoveItem(x):
	print("sorry. this doesn't work yet.");

menu = "1) Check inventory\n2) Add item to inventory\n3) Remove item from inventory"
print(menu);
inventory = {}

def runner(x):
	if(x==1):
		checkInventory();
	elif(x==2):
		invAddItem(input("What will you add?: "));
	elif(x==3):
		invRemoveItem(input("What will you remove?: "));
	else:
		print("We didn't plan for this");

str1 = "";
valid = False;
while(valid!=True):
	str1 = input("Select an option: ");
	valid = isValid(str1)
runner(int(str1));
print ("Received input is : ", str1);

