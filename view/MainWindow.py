import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLayout, QLabel, QPushButton, QComboBox
from PyQt6.QtCore import Qt

class mainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Calculadora principio de Arquimedes.")
        self.setGeometry(100, 100, 1200, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Calculadora principio de Arquimedes")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center; color: #e7ecef;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setMargin(20)
        main_layout.addWidget(title_label)
        central_widget.setStyleSheet("background-color: #274c77;")

        methods_widget = QWidget()
        methods_widget.setStyleSheet("background-color: #a3cef1 border-radius: 20px; padding: 20px;")

        container_layout = QVBoxLayout()
        container_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout.setSpacing(40)

        main_label = QLabel("¿Que formula desea usar?")
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_label.setStyleSheet("font-size: 18px; font-weight: bold;, color: #274c77;")
       
        container_layout.addWidget(main_label)

        test_layout = QVBoxLayout()
        test_label = QLabel("Metodo de prueba")
        test_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        test_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        test_label_description = QLabel("Seleccione una prueba para evaluar la calidad de los numeros generados.")
        test_label_description.setStyleSheet("font-size: 14px;")
        self.test_combo = QComboBox()
        self.test_combo.addItems(["Seleccione... ","Chi Cuadrado", "Varianza", "Kolmogorov Smirnov", "Medias"])
        test_layout.addWidget(test_label)
        test_layout.addWidget(test_label_description)
        test_layout.addWidget(self.test_combo)
    
        #methods_layout.addLayout(gen_layout)
        #methods_layout.addLayout(test_layout)

        calculate_button = QPushButton("Calcular")
        calculate_button.setStyleSheet("background-color: #5C8BE1; font-weight:bold; color: white; font-size: 16px; padding: 10px; border-radius: 10px;")
        calculate_button.setFixedSize(150, 40)
        calculate_button.setCursor(Qt.CursorShape.PointingHandCursor)

        #container_layout.addLayout(methods_layout)
        container_layout.addWidget(calculate_button, alignment=Qt.AlignmentFlag.AlignCenter)

        methods_widget.setLayout(container_layout)  

        main_layout.addWidget(methods_widget)

        central_widget.setLayout(main_layout)

app = QApplication(sys.argv)
window = mainWindow()
window.show()
sys.exit(app.exec())        
