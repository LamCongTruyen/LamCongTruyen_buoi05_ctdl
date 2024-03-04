def same_frequency(list1, list2):#tạo hàm same_frequency
    if len(list1) != len(list2):#Kiểm tra xem độ dài của hai danh sách có bằng nhau không
        return False
    
    freq_dict1 = {}#Tạo hai từ điển freq_dict1 và freq_dict2 để lưu trữ tần suất của các phần tử trong mỗi danh sách.
    freq_dict2 = {}
    
    for item in list1:#Đếm tần suất của các phần tử trong list1 và lưu vào freq_dict1.
        freq_dict1[item] = freq_dict1.get(item, 0) + 1  #Hàm get(item, 0) trả về giá trị tần suất hiện tại của item, hoặc 0 nếu item chưa có trong từ điển.

    for item in list2:
        freq_dict2[item] = freq_dict2.get(item, 0) + 1    

    return freq_dict1 == freq_dict2
    #So sánh hai từ điển freq_dict1 và freq_dict2 để kiểm tra xem chúng có cùng tần suất của các phần tử hay không.
    # Nếu cùng, trả về True; ngược lại, trả về False.
list1 = [1, 2, 3, 2, 1]#ví dụ
list2 = [3, 1, 2, 1, 3]
result = same_frequency(list1, list2)
print(result)#in ra màn hình
