def find_max(a_list):
    flag = True
    none_list = []
    if a_list == none_list:
        return 0
    else:
        max_value = a_list[0]
        for i in a_list:
            if i > max_value:
                max_value = i
            else:
                pass
        return(f"最大值為{max_value}")

        
print(find_max([0, 1, 3, 5, 4, 9, 16, 58, 3, 5, 11, 16]))