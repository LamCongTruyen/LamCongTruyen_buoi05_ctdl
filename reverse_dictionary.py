def reverse_dictionary(input_dict):#tạo hàm đảo ngược khóa
    reversed_dict = {}
    
    #cho biến key và value chạy trong ds các biến trong dict
    for key, value in input_dict.items():
        # Gán cặp khóa-giá trị trong thứ tự ngược lại vào từ điển mới
        reversed_dict[value] = key
    
    return reversed_dict#trả về giá trị của biến reversed_dict

# Ví dụ 
input_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_result = reverse_dictionary(input_dict)
print(reversed_result)#in ra màn hình
