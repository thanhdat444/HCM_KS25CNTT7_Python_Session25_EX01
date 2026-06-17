class BankAccount:
    # 1. Class Attributes:
    bank_name = "Vietcombank"
    transaction_fee = 2000 

    # 2. Instance Attributes & Initialization:
    def __init__(self, account_number, account_name: str):
        self.account_number = account_number
        self.__account_name = account_name.strip().upper()
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    
    @property
    def account_name(self):
        return self.__account_name
    
    @account_name.setter
    def account_name(self, new_account_name: str):
        new_account_name = new_account_name.upper()

        self.__account_name = new_account_name
        
    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10
    
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        total = amount + BankAccount.transaction_fee

        if (self.__balance >= total):
            self.__balance -= total
            return True
        else:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False

    def display_info(self):
        print(f"Tên ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")

def menu():
    print("""
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================""")
    
def main():
    current_account = None

    while True:
        menu()

        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                print("--- MỞ TÀI KHOẢN MỚI ---")
                while True:
                    account_number = input("Nhập số tài khoản 10 chữ số: ")

                    if (BankAccount.validate_account_number(account_number)):
                        break

                    print("Số tài khoản không hợp lệ!")
                    print("Số tài khoản phải gồm đúng 10 chữ số.")

                while True:
                    account_name = input("Nhập tên chủ tài khoản: ")

                    if (account_name):
                        break

                    print("Tên chủ tài khoản không được để trống!!")

                current_account = BankAccount(account_number, account_name)

                print("Mở tài khoản thành công!")
                print(f"Số tài khoản: {current_account.account_number}")
                print(f"Tên chủ tài khoản: {current_account.account_name}")

            case "2":
                if (not current_account):
                    print("Hệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue
                
                print("--- THÔNG TIN TÀI KHOẢN ---")
                BankAccount.display_info(current_account)
            case "3":
                if (not current_account):
                    print("Hệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue

                print("--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                choose = input("Chọn loại giao dịch (1-2): ").strip()

                match choose:
                    case "1":
                        try:
                            amount = int(input("Nhập số tiền giao dịch: "))

                            if (amount <= 0):
                                print("Số tiền giao dịch phải > 0")
                                continue

                        except ValueError:
                            print("Số tiền phải là số nguyên dương")
                            continue

                        current_account.deposit(amount)
                        print(f"Nạp tiền thành công: +{amount:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")
                    case "2":
                        try:
                            amount = int(input("Nhập số tiền giao dịch: "))

                            if (amount <= 0):
                                print("Số tiền giao dịch phải > 0")
                                continue

                        except ValueError:
                            print("Số tiền phải là số nguyên dương")
                            continue

                        if (current_account.withdraw(amount)):
                            print(f"Rút tiền thành công: -{amount:,} VND")
                            print(f"Phí giao dịch: {current_account.transaction_fee:,} VND")
                        
                        print(f"Số dư mới: {current_account.balance:,} VND")
                    case _:
                        print("Lỗi: lựa chọn không hợp lệ!!")
            case "4":
                if (not current_account):
                    print("Hệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue

                print("--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                while True:
                    new_name = input("Nhập tên mới: ").strip()

                    if (new_name):
                        break

                    print("Tên không được để trống!!")

                current_account.account_name = new_name

                print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")
            case "5":
                if (not current_account):
                    print("Hệ thống chưa có thông tin tài khoản")
                    print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                    continue

                print("--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
                print(f"Phí giao dịch hiện tại: {current_account.transaction_fee:,} VND")

                try:
                    new_transaction_fee = int(input("Nhập số tiền giao dịch: "))

                    current_account.update_transaction_fee(new_transaction_fee)

                    print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {current_account.transaction_fee:,} VND")
                    if (new_transaction_fee <= 0):
                        print("Phí giao dịch không được âm")
                        print(f"Phí giao dịch hiện tại vẫn là: {current_account.transaction_fee:,} VND")
                        continue

                except ValueError:
                    print("Số tiền phải là số nguyên dương")
                    continue

            case "6":
                print("Thoát chương trình!!")
                break
            case _:
                print("Lỗi: Lựa chọn không hợp lệ!!")

main()