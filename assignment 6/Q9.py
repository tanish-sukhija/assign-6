class Parentheseshcecker:
    def __init__(self):
        pass

    def check_validity(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        return not stack


p = Parentheseshcecker()
s = input("Enter a string of parentheses to check its validity: ")
print(p.check_validity(s))