my_set = {1,1,2,2,4}
print(my_set)

first_url = 'www.google.com/first_url'
second_url = 'www.google.com/first_url'

my_urls = {first_url, second_url}

print(my_urls)

first_list = [1,2,3,3]
a_tuple = (4,2,7,7)

print(7 in a_tuple)
first_set_from_list = set(first_list)
second_set_from_list = set(a_tuple)
print(first_set_from_list)
print(second_set_from_list)
print(first_set_from_list.intersection(second_set_from_list))
print(first_set_from_list.union(second_set_from_list))
print(first_set_from_list.difference(second_set_from_list))
print(first_set_from_list.issubset(second_set_from_list))
print(first_set_from_list - second_set_from_list)
# my_lists = {first_list, second_list}
# print(my_lists)