# Jonas York 
# U4 L4
#Balancing brackets with ArrayStack

from StackClass import ArrayStack

def bracketOrder(bracketList):
  bracketStatus = "Balanced"
  myStack = ArrayStack()
  for item in bracketList:
    if item == "(" or item == "[" or item == "{":
      myStack.push(item)
    else: #
      if len(myStack) == 0:
        bracketStatus = "Unbalanced"
        break
      else:
        top = myStack.top()
        if top == "(" and item == ")":
          myStack.pop()
        elif top == "[" and item == "]":
          myStack.pop()
        elif top == "{" and item == "}":
          myStack.pop()
        else:
          bracketStatus = "Unbalanced"
          break
  if len(myStack) >=1:
    bracketStatus = "Unbalanced"
  return bracketStatus


def main():
  myStack = ArrayStack()
  test1 = "()(()){([()])}"
  test2 = "((()(()){([()])}))"
  test3 = ")(()){([()])]"
  test4 = "({[])}"
  test5 = "("

  for test in [test1, test2, test3, test4, test5]:
      # Function call for tests here
      print(f"{test} - {bracketOrder(test)}\n")
  

if __name__ == "__main__":
    main()

