def isValid(x):
	"Tests if the input is proper"
	if(x.isdigit()):
		if((int(x)>=1)and(int(x)<=4)):
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

def invAddItem(x):
	#check if the item is already in inventory
	if(x in inventory):
		inventory[x] = inventory[x] + 1;
	else:
		inventory[x] = 1;
		
		
def invRemoveItem(x):
	if(x in inventory):
		if(inventory[x]>1):
			inventory[x] = inventory[x] - 1;
		else:
			inventory.pop(x);
	else:
		print("item doesn't exist");

def checkInventory():
	print(inventory);

menu = "1) Check inventory\n2) Add item to inventory\n3) Remove item from inventory\n4) Quit"

inventory = {}
finished = False;

def runner(x):
	global finished
	if(x==1):
		checkInventory();
	elif(x==2):
		invAddItem(input("What will you add?: "));
	elif(x==3):
		invRemoveItem(input("What will you remove?: "));
	elif(x==4):
		finished = True;
		print("Goodbye");
	else:
		print("We didn't plan for this");

while(finished!=True):
	print(menu);
	given = giveValid();
	runner(int(given));