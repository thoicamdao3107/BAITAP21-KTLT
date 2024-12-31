import sys
from PyQt6.QtWidgets import QApplication
from CombinationPermutationExt import MainApp  # Import MainApp từ CombinationPermutationExt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
