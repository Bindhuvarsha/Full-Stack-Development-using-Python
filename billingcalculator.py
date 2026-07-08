product = input("Enter product name: ")
price = int(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
discount = int(input("Enter discount amount: "))
total = price * quantity
final_bill = total - discount
print("Product:",product)
print("Total amount:",total)
print("Final bill:",final_bill)