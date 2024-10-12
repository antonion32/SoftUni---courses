
num_messages = int(input())

for message in range(num_messages):
    current_num = int(input())

    if current_num == 88:
        print(f"Hello")
    elif current_num == 86:
        print(f"How are you?")
    elif current_num < 88:
        print(f"GREAT!")
    else:
        print("Bye.")