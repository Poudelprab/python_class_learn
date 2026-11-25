#name="prabhat"
#print(f"hello,{name}!") #f string is a way to insert variables or expressions directly into a string

input1= int(input("enter any number: "))
input2= int(input("enter another number: "))

sum= input1+input2  #sum of user inputs
product= input1*input2 # product of user inputs
print(f"the total sum  of two input numbers is: {sum} \n The product of two user inputs is {product}") #displaying sum of user inputs and products
#print(f"the product  of two input numbers is: {product}") #displaying product of user inputs
print(f"The sum is :{sum: ,d}")


def calculate(a,b):
    sum=(a+b)
    product=(a*b)
    print(sum)
    print(product)
calculate(2,2)
    