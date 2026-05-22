password = 123456
count = 0
while True:
    password_input = int(input("Nhập mật khẩu: "))
    if password_input == password:
        print("Đăng nhập thành công!")
        break
    else:
        if count < 3:
            print("Mật khẩu sai, vui lòng nhập lại!\n"
                  f"Bạn còn {2-count} lần thử\n")
            count += 1
        else:
            print("Tài khoản đã bị khóa!")
            break
            