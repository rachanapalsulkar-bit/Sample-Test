a="rachana"
b="palsulkar"
c= a + " " + b
print(c)

##================##

a=1
b=5
c=3
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("Some values are equal")

##=======================##
product = []
print("\nEnter the product name (type 'q' to stop):")
while True:
    product_input = input()
    if product_input == 'q':
        break
    if product_input == '0' and not product:
        print("Cart is empty")
        break
    print(product)
    
print("All products are successfully added to the cart.")
print("Products list is:")
print(product)
