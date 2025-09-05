#python week 3 assignment
def calculate_discount(price, discount_percent):
    if discount_percent == 20:
        discount_amount = price * (discount_percent/100)
        return price - discount_amount
    else:
        return price
#To prompt the user for input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount)
print(f"final price after discount:{final_price:2f}")
ValueError
print("please enter valid numeric values.")



