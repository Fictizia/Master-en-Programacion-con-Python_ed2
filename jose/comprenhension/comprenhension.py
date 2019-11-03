# comprenhension list

numbers_to_ten = list()
for number in range(1,11):
    numbers_to_ten.append(number)



com_number_to_ten = [number for number in range(1,11) if number%2==0]
print(com_number_to_ten)