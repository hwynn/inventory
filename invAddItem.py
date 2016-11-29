inventory = {}

def invAddItem(x):
	#check if the item is already in inventory
	if(x in inventory):
		inventory[x] = inventory[x] + 1;
	else:
		inventory[x] = 1;

invAddItem(input("What will you add?: "));
print(inventory);
invAddItem("ball");
print('ball' in inventory);
print(1 in inventory);
invAddItem("ball");
print(inventory);