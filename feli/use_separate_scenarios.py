def user_input(prompt):
    arr = {}
    for i in range(2):
        str = input(prompt)
        arr.append(str)
    return arr[0], arr[1]