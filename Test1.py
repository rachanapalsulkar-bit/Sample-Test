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

##=======================##
product = []
product_input = input("\n Enter the product name: ")
product.append(product_input)



while True:
    product_input = input("Enter the product name: ")
    if product_input == 'q':
        break
    product.append(product_input)
    print(product) ; print("Type 'q' to stop.\n")

print("All products are successfully added to the cart.")
print("Products list is:") ; print(product)
