def tuple_elementwise_sum(tuple1, tuple2):
    # Kiểm tra độ dài của hai tuple
    if len(tuple1) != len(tuple2):
        raise ValueError("The lengths of the input tuples must be equal")
    
    # Tính tổng các phần tử tương ứng và lưu vào một tuple mới
    result = tuple(x + y for x, y in zip(tuple1, tuple2))
    
    return result

# Ví dụ sử dụng:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple_elementwise_sum(tuple1, tuple2)
print(result)
