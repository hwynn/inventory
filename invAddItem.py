inventory = {}


def invAddItem(x):
	#x must be a word
	#check if the item is already in inventory
	inventory[x] = 1;

print(inventory);
invAddItem("ball");
print(inventory);