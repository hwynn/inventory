import sys
inventory = {}
def giveValid():
	while(True):
		str1 = input("Enter your input: ");
		if(str1.isdigit() == False):
			print("Input must a number");
			continue
		if((int(str1)>=1)and(int(str1)<=4) == False):
			print("Input must be between 1 and 4");
			continue
		break
	return(int(str1));

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

while(True):
	print("1) Check inventory\n2) Add item to inventory\n3) Remove item from inventory\n4) Quit");
	given = giveValid();
	if(given==1):
		print(inventory);
	elif(given==2):
		invAddItem(input("What will you add?: "));
	elif(given==3):
		invRemoveItem(input("What will you remove?: "));
	elif(given==4):
		print("Goodbye");
		sys.exit()
	else:
		print("We didn't plan for this");