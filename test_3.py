amount_of_box = int(input("Nhập số thùng hợp lệ: "))
result = ""
total_product = 0
for box in range(amount_of_box):
    product_quantity = int(input("Nhập số lượng hàng hóa: "))
    if product_quantity < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue
    elif product_quantity == 0:
        print("Chương trình hiểu là đã kiểm đếm xong và kết thúc quá trình nhập")
        break
    else: 
        total_product += product_quantity
        result += f"\nThùng {box+1} có: {product_quantity} sản phẩm"    
    
        
print(result)   
print(f"\nTổng số lượng hàng hóa: {total_product}")