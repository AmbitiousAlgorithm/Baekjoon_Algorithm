def solution(s):
    answer = True

    stack = []
    bracket = {')':'(', '}':'{', ']':'['}


    for letter in s:
        stack.append(letter)

        if len(stack) >= 2:
            top = stack[-1]

            if top =='}' and bracket[top] == stack[-2]:
                stack.pop()
                stack.pop()
            if top ==')' and bracket[top] == stack[-2]:
                stack.pop()
                stack.pop()
            if top ==']' and bracket[top] == stack[-2]:
                stack.pop()
                stack.pop()


    if stack:
        answer = False

    return answer