a = int(input("Enter the  number:"))
b = int(input("Enter the  number:"))

try:
    print("resource Open")
    print(a/b)

except Exception as e:
  #  print("Hey b should not be zero since anything divide by zero is infinite",e)
    print(e)

finally:
    print("resource closed")

