def filter_dictionary(input_dict, condition):#tạo hàm tìm 
    filtered_dict = {}#tạo biến đếm
    
    for key, value in input_dict.items():#vòng lặp qua tất cả các cặp khóa-giá trị trong từ điển đầu vào.
        if condition(key, value):#Kiểm tra xem kết quả của việc gọi hàm điều kiện (condition) với đối số là khóa và giá trị hiện tại có là True hay không.
            filtered_dict[key] = value
    
    return filtered_dict#Trả về từ điển sau khi đã lọc.

def is_even_key_value(key, value):
    return key % 2 == 0 and value % 2 == 0#trả về giá trị biến key và giá trị khi cả hai đều chia hết cho 2

input_dict = {1: 10, 2: 20, 3: 15, 4: 24, 5: 30}#ví dụ
result = filter_dictionary(input_dict, is_even_key_value)
print(result)#in ra màn hình
