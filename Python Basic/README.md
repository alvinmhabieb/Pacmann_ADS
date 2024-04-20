# Python Project Pacmann – Super Cashier

## Background
As programmers, we are asked to program a self-service cashier in a supermarket so that the payment system can run smoothly. The cashier system consists of features where customers can write down their identity and enter the items they buy directly.

## Workmanship Procedure
1. Create an object from class: trnsct_123 = Transaction()
2. Create a 'add_item' function to enter the item you want to buy;
3. Create 'update_item_name', 'update_item_qty', and 'update_item_price' functions to change the item, number of items and price of the purchased item;
4. Create a 'delete_item' function to remove items from the shopping list and a 'reset_transaction' function to delete all items in the shopping list;
5. Create a 'check_order' function to be able to view and check the shopping list that has been inputted;
6. Create a 'total_price' function to calculate total spending.

## Program Flow
- Create a process of solving self-service cashier problems to help merchants sell.
- Create a process to 'add items' to groceries.
- Create a process to 'remove items' of groceries.
- Create a process to 'edit the name' of a grocery item.
- Create a process to 'edit the amount' of grocery items. 
- Create a process to 'edit the price' of groceries.
- Create a process to 'calculate the total price' of groceries.
- Create a process for 'calculating discounts' of grocery items.
- Create a process for 'emptying things' groceries.
- Check groceries by 'displaying all groceries'.

## Function Explained
All of the following functions are contained in a class named 'Transaction' in the file 'script.py'
https://github.com/alvinmhabieb/super-cashier/blob/main/script.py :

#### Method
- 'add_item'. Add items with the format 'add_item([item_name, quantity, price_per_item])' into the variable 'items' in the class. Example: 'add_item(['Chicken', 12, 15_000])'
- 'delete_item'. Remove items by name inside 'items' if available with the format 'delete_item(item_name)'. Example: 'delete_item('Chicken')'
- 'update_item_name'. Rename the current item with a new item name if the item mentioned is available with the format 'update_item_name(old_name, new_name)'. Example: 'update_item_name('chicken', 'fried chicken')'
- 'update_item_qty'. Replace the order quantity of the goods if the item mentioned is available with the format 'update_item_name(item_name, new_qty)'. Example: 'update_item_qty('Chicken', 20)'.
- 'update_item_price'. Replace the price per item item if the item mentioned is available with the format 'update_item_price(item_name, new_price)'. Example 'update_item_price('Chicken', 30_000)'
- 'calculate_total_price'. Calculates the total price of all goods.
- 'check_order'. Displays all the items that have been added along with the total overall price.
- 'reset_transaction'. Empty all items at once that have been added.
- 'total_price_print'. Displays all items along with the total price of each item, discounts, and total after discounts.

#### Generic Function
- '__init__'. Initiating the main variable in a class. In this case it is the variable 'items' that are assimilated.
- 'calculate_discount'. Calculates if the total overall price of the item qualifies for a discount. The terms of the discount are as follows:
	1. If above IDR 200,000 discount of 5%
	2. If above IDR 300,000 discount of 8%
	3. If above IDR 500,000 discount of 10%

#### Modules
- 'validate_add_item'. Validate before the item is added. Covering the writing format and the price of the goods / qty should not be negative.
- 'validate_update_item_name'. Validate before the item is renamed. Includes the format of writing new item names and old item names.
- 'validate_update_item_qty'. Validate before qty items are updated. Covering the writing format and qty should not be negative.
- 'validate_update_item_price'. Validate before the item's price is updated. Covering the writing format and price should not be negative.

## Test Case
Create a transaction function from a script with code 'trnsct_123 = Transaction()'
![image](https://user-images.githubusercontent.com/47166304/215318266-b9280c5a-4977-4ac8-8f77-8e8a776658b1.png)

### Test 1: add_item()
The customer wants to add two new items using the 'add_item()' method. The added items are as follows:
- Item Name: Fried Chicken, Qty: 2, Price: 20000
- Item Name: Toothpaste, Qty: 3, Price: 15000

**Output:**
![image](https://user-images.githubusercontent.com/47166304/215318274-445884a3-fe1d-4823-b771-67da591ca764.png)


### Test 2: delete_item()
When a customer incorrectly purchases one of the items from the added purchase, the customer uses the 'delete_item()' method to delete the item. The item you want to remove is **Toothpaste**.

**Output:**
![image](https://user-images.githubusercontent.com/47166304/215318282-9bd3a1d6-b661-4215-bc65-dab798e34fbb.png)


### Test 3: reset_transaction()
The customer entered the wrong item that they wanted to spend. Because they want to repeat from the input item from the beginning, the customer simply uses the 'reset_transaction()' method to delete all items that have been added.

**Output:**
![image](https://user-images.githubusercontent.com/47166304/215318289-30812256-6312-49be-bf03-297ad56a3365.png)


### Test 4: total_price()
After the customer finishes shopping, they will calculate the total expenditure that must be paid using the 'total_price()' method. Before issuing the output of the total shopping will display the items purchased. The added items are as follows:
- Item Name: Fried Chicken, Qty: 2, Price: 20000
- Item Name: Toothpaste, Qty: 3, Price: 15000
- Item Name: Toy Car, Qty: 2, Price: 200000
- Item Name: Instant Noodles, Qty: 5, Price: 3000

**Output:**
![image](https://user-images.githubusercontent.com/47166304/215318296-5826dba5-506f-4019-bca8-0c0d409297de.png)


## Conclusion
- Super cashier is a simple program consisting of features where customers can write down their identity and enter the items they buy directly.
- There are features of adding items, editing items (name, quantity, price per item), deleting items, and summing up the entire price of the item and its discounts quickly and precisely.
- All of these features can make it easier and faster for buyers to buy their goods independently.
