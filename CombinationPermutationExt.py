from PyQt6.QtWidgets import QMainWindow
from CombinationPermutation import Ui_MainWindow  # Import lớp giao diện đã được chuyển đổi


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        # Nối các nút với các hàm xử lý
        self.ui.pushButton.clicked.connect(self.calculate_results)

    def calculate_results(self):
        try:
            n = int(self.ui.lineEdit.text())
            k = int(self.ui.lineEdit_2.text())
            # Tính toán tổ hợp (C) và hoán vị (A)
            A = self.factorial(n) // self.factorial(n - k)  # Hoán vị
            C = A // self.factorial(k)  # Tổ hợp
            self.ui.lineEdit_3.setText(str(A))
            self.ui.lineEdit_4.setText(str(C))
        except ValueError:
            self.ui.lineEdit_3.setText("Error")
            self.ui.lineEdit_4.setText("Error")

    @staticmethod
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
