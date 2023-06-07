num = int(input("Provide a number to give you it's multiplication table: "))
counter = 0
for i in range (1, 13, 1):
  table = num * i
  print()
  print("How much is",num,"x",i,"?")
  print()
  answer = int(input(""))
  # question = input("How much is", num,"x", i,"?")
  if answer == table:
    counter +=1
    print()
    print("You have won a point!")
    print("Subtotal points:",counter)
    print()
  else:
    print()
    print("Wrong!")
    print("The right answer is",num,"x",i,"=",table)
    print("No points this time")
    print()
if counter == 12:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", counter, "out of 10 correct.")
