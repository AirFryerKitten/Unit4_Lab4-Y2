# # Implementation & testing of the ArrayStack class

from StackClass import ArrayStack


def main():
    original = "Sphinx of black quartz, judge my vow"
    new = ""

    MyStack = ArrayStack()

    for letter in original:
        MyStack.push(letter)
    
    for item in range(len(MyStack)):
        new += MyStack.pop()

    print(f"Original: {original}")
    print(f"Reversed: {new}")

if __name__ == "__main__":
    main()

