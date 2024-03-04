def sum_and_product(tuple_of_numbers):#Định nghĩa hàm sum_and_product_of_tuple_elements 
   
    total_sum = 0# Khởi tạo biến để lưu tổng và tích
    total_product = 1
    
    
    for number in tuple_of_numbers:
        total_sum += number## Cộng phần tử vào tổng
        total_product *= number# Nhân phần tử vào tích
    
    return total_sum, total_product # Trả về tổng và tích


numbers_tuple = (1, 2, 3, 4)#ví dụ
sum_result, product_result = sum_and_product(numbers_tuple)
print("Sum:", sum_result)#in ra màn hình
print("Product:", product_result)
