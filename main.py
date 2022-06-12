#string = '(((([{}]))))'
# string = '    [([])((([[[]]])))]{()}'
# string = '    {{[()]}}'
string = '}{}'
# string = '{{[(])]}}'
# string = '[[{())}]'


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.size()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def is_pair(bracketleft, bracketright) -> bool:
    if (bracketleft == '(') and (bracketright == ')'):
        return True
    elif (bracketleft == '{') and (bracketright == '}'):
        return True
    elif (bracketleft == '[') and (bracketright == ']'):
       return True
    else:
       return False

def is_string_balance(string = '') -> bool:
    stack = Stack()
    left_symbols = ['(', '[', '{']
    right_symbols = [')', ']', '}']

    for symbol in string:
        if symbol in left_symbols:
            stack.push(symbol)
        if symbol in right_symbols:
            if stack.isEmpty():
                return False
            elif not(is_pair(stack.pop(), symbol)):
                return False

    if stack.isEmpty():
        return True
    else:
        return False



if __name__ == '__main__':

    print(f'Строка {string} сбалансирована? {is_string_balance(string)}')