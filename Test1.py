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
    
# Ignore empty string if cart already has items  
    if product_input == "":
        print("Product name cannot be empty. Try again.")
        continue

# Exit condition
    if product_input == 'q':
        break

# Add valid product name
    product.append(product_input)

# Print the final list of products from the cart
print("All products are successfully added to the cart.")
print("Products list is:")
print(product)

##=======================##
