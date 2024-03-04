def merge_sum(dict1, dict2):#tạo một hàm tính tổng các khóa của biến
    merge_dict={}#tạo biến lưu trữ 
    for key,value in dict1.items():#cho biến key và value chạy trong ds các biến trong dict1
        merge_dict[key]=value#lấy giá trị của key gắn vào value

    for key,value in dict2.items():#tương tự dict 1
            if key in merge_dict:#nếu key trong dict2 tồn tại trong biến lưu trữ mergedict th
                merge_dict[key]+=value#key = key +value
            else:
                merge_dict[key] = value#nếu không thì key = value
    return merge_dict#trả về biến lưu trữ
dict1 = { 'a': 1, 'b' : 2, 'c' : 3}#ví dụ
dict2 = { 'b': 3, 'c' : 4, 'd' : 5}
result = merge_sum(dict1, dict2)
print(result)#in ra màn hình