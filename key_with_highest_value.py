def key_with_highest_value(input_dict):#tạo hàm tìm giá trị key lớn nhất
    if not input_dict:  #nếu giá trị cần tìm ko có trong dict
        return None#trả về none
    
    max_value = max(input_dict.values())  #tìm giá trị lớn nhất
    for key, value in input_dict.items():#cho biến key và value chạy lần lượt trong các phần tử của dict
        if value == max_value:#so sánh và nêu bằng giá trị lớn nhất thì trả về giá trị của key
            return key


input_dict = {'a': 10, 'b': 20, 'c': 15}#ví dụ
result = key_with_highest_value(input_dict)
print(result)#in ra màn hình
