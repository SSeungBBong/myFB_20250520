from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
import csv
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap

Form, Window = uic.loadUiType("myProject05/res/Dialog.ui")
filename = "" # Initialize filename as an empty string

def on_picture_button_clicked():
    global filename  # Use the global filename variable
    # Open a file dialog to select an image
    options = QFileDialog.Option.ReadOnly
    file_filter = "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"

    filename, _ = QFileDialog.getOpenFileName(window, "Select an Image", "", file_filter, options=options)
    if filename:
        QMessageBox.information(window, "File Selected", f"Selected file: {filename}")
        # Display the selected image in lbl_picture
        pixmap = QPixmap(filename)
        form.lbl_picture.setPixmap(pixmap)
        form.lbl_picture.setScaledContents(True)
    else:
        QMessageBox.warning(window, "No File Selected", "No file was selected.")



def on_save_button_clicked():
    # Retrieve input values from the form
    global filename  # Use the global filename variable
    name = form.lineEdit_name.text()
    phone = form.lineEdit_phone.text()
    try:
        memo = form.textEdit_memo.toPlainText()
    except AttributeError:
        QMessageBox.critical(window, "Error", "The 'textEdit_Memo' widget is not defined. Please check the UI file.")
        return
    # Retrieve the selected radio button value
    if form.radioButton_1.isChecked():
        selected_option = "Option 1"
    elif form.radioButton_2.isChecked():
        selected_option = "Option 2"
    else:
        selected_option = None

    # Check if all fields are filled
    if not name or not phone :
        QMessageBox.warning(window, "Input Error", "Please fill in all fields.")
        return

    # Save the input values to addbook.csv
    try:
        with open("/myProject05/data/addbook.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, memo, selected_option, filename])
        QMessageBox.information(window, "Success", "Contact information saved successfully!")
        
    except Exception as e:
        QMessageBox.critical(window, "Error", f"Failed to save book information: {e}")
        return

    # Clear the input fields
    form.lineEdit_name.clear()
    form.lineEdit_phone.clear()
    form.textEdit_memo.clear()

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

# Connect the btn_Save clicked signal to the on_save_button_clicked function
form.btn_Save.clicked.connect(on_save_button_clicked)
form.btn_picture.clicked.connect(on_picture_button_clicked)

window.show()
app.exec()