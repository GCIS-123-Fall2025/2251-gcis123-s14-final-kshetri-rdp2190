
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    open_count = 0
    closed_count = 0
    last_open = 0
    a_stack = Stack()
    for i in range(len(a_string)):
        a_stack.push(a_string[i])
    index = len(a_stack) -1
    while a_stack.is_empty() == False:
        if a_stack.peek() == "(":
            open_count +=1
            a_stack.pop()
            last_open = index
        elif a_stack.peek() == ")":
            closed_count +=1
            a_stack.pop()
        else:
            a_stack.pop()
        index -=1
    if open_count == closed_count:
        return 0
    elif closed_count > open_count:
        return -1
    else:
        return last_open

    


def main():
    string1 = "--(---(------)--"
    print(balance_parenthesis(string1))
    string2 = "()----)"
    print(balance_parenthesis(string2))
    string3 = "-----() -- ( () )"
    print(balance_parenthesis(string3))


if __name__ == "__main__":    main()