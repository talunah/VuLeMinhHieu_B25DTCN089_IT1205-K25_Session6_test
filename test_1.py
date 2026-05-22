product_price = float(input("Nhập đơn giá của sản phẩm: "))
product_quantity = int(input("Nhập số lượng sản phẩm: "))
total_price = product_price * product_quantity 
discount_price = total_price*0.1 if total_price >= 1000000 else 0
final_price = total_price - discount_price
print(f"Số tiền phải thanh toán: {final_price} VNĐ")