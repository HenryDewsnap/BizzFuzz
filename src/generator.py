def return_fb(num:int):
    return_type = ""
    if num%3 == 0: return_type += "Fizz"
    if num%5 == 0: return_type += "Buzz"
    return return_type

file = open("fizz_buzz.py", "w")

end = 1000000
current_num = 0
while current_num < end:
    
    num_type = return_fb(current_num)
    if num_type != "":
        file.write(f"print(f'{current_num}: {num_type}')\n")

    current_num += 1
file.close()
