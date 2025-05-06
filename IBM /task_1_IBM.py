"""
A purchasing manager must buy a specific number of units of an item to replenish the warehouse. 
The primary supplier has a list of containers, each with a number of units. 
The manager must buy contiguous containers, starting at container 0 and continuing until 
at least the desired number has been purchased. If there are not enough units available, they must be purchased from another supplier.
If any excess items must be purchased, 
they must be resold. Determine the remaining number of items to be purchased or sold after purchasing from the primary supplier.

Example n=5
itemCount = [10, 20, 30, 40, 15]
target = 80

The manager starts buying at index 0 and continues until 
all available units are purchased or until at least 80 units have been purchased.
The manager will buy containers with itemCounts
= 10 + 20 + 30 + 40 = 100. Since too many items
were purchased, the number sold is purchased -
target = 100 - 80 = 20

If the target = 130, the manager will purchase all
of the units from the primary supplier for a total
of purchases = 115. Then another target -
purchases = 130 - 115 = 15 additional units must be purchased

"""

"""
Approach : 

While loop can be run until any of the two conditions are met :

if index > len(itemCount)
if target is achieved (total_units_purchased > target)
"""

def restock(itemCount, target):
    index = 0
    total_items_purchased = 0

    while index < len(itemCount) and total_items_purchased < target:
        total_items_purchased += itemCount[index]
        index += 1
    
    if total_items_purchased < target:
        return target - total_items_purchased
    else:
        return total_items_purchased - target
    
if __name__ == "__main__":
    itemCount = [10, 20, 30, 40, 15]
    result = restock(itemCount, 80)
    print(result) 