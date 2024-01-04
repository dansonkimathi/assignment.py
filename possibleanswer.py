def original_item_price():
	original_price = 0.0
	original_price = float(input("What is the original price of the item?"))
	

	return original_price
	

	

	

	

def Discount():
	store_discount_choice = 0.0
	original_price = 0.0
	store_discount_percentage = 0.0
	

orig_price = original_item_price()
	

store_discount_choice = int(input("Is there an in-store discount? Enter 1 for Yes, 2 for No."))
	
def calculate_store_discount():
    original_price = 0.0
Discount = 0.0
discount_amount = 0.0
final_store_discount = 0.0 

if store_discount_choice == 1:
    calculate_store_discount()
	

elif store_discount_choice == 2:
	original_item_price()
	

	

	

	


	

original_price = int(input("Re-Enter the original price."))
	

in_store_discount = int(input("What is the in_store discount? (ex. .20)"))
	

discount_amount = original_price * in_store_discount
final_store_discount = original_price - discount_amount
	

print ("The in_store savings amount is ", discount_amount)
print ("Your new price is ", final_store_discount)
	
