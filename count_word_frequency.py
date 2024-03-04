def count_word_frequency(word_list): #tạo một hàm tìm tần số lặp lại của từ trong list
    word_freq ={} #tạo biến lưu trữ số lần xuất hiện
    for word in word_list: #vòng lặp biến word trong ds các biến
        if word in word_freq:#neesi biến đó đã có trong biến lưu trữ
            word_freq[word] += 1#tăng giá trị của biến lưu trữ lên 1
        else:
            word_freq[word] = 1#nếu không thì tần suất của biến đó vẫn giữ là 1
    return word_freq#trả về giá trị của biến lưu trư số lần xhien
word_list = ['apple', 'orrange', 'apple', 'apple' , 'banana', 'banana']#ví dụ 
f = count_word_frequency(word_list)
print(f) #in ra màn hình