# Jonas York 
# U4 L3 
# Reversing  a file 

from StackClass import ArrayStack

def getFile(fileName):
  cleanContents = ""
  with open(fileName, "r") as openFile:
      contents = openFile.read()
      for letter in contents:
        if ord(letter) >= 65 and ord(letter) <= 90 or ord(letter) >= 97 and ord(letter) <= 122:
          cleanContents += letter
        elif letter == " " or "\n":
          cleanContents += letter
        
  return cleanContents

def writeFile(fileName, contents):
  with open(fileName, "w") as openFile:
    openFile.write(contents)


def main():
  myStack = ArrayStack()
  reverse = ""
  contents = getFile("earnest.txt")
  contentsList = contents.split(" ")

  for item in contentsList:
    myStack.push(item)
  for i in range(len(myStack)):
    reverse += myStack.pop() + " "
  writeFile("reverse.txt", reverse)
  

if __name__ == "__main__":
    main()

