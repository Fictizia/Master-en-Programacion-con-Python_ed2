def delete_from(origin_list, *args):
    group_result = set(origin_list) - set(args)
    return list(group_result)

# print(delete_from([1,3,3,3, 4,5,6,8], 1, 3, 5))

def complicated_deleted(origin_list, *args):
    for number in args:
        repeated = origin_list.count(number)
        for _ in range(0,repeated):
            origin_list.remove(number)
    
    return origin_list

print(complicated_deleted([1,3,3,3,4,5,6,8], 1, 3, 5))