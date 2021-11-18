from PyQt5 import uic, QtWidgets

def funcao_calcular():
    imc = 0

    dado_altura = float(formulario.lineEdit.text().replace(",", "."))
    dado_peso = float(formulario.lineEdit_2.text())
    imc = dado_peso/(dado_altura*dado_altura)

    formulario.label_5.setText(str(imc))


app = QtWidgets.QApplication([])
formulario = uic.loadUi("janelaimc.ui")
formulario.botao_calcular.clicked.connect(funcao_calcular)

formulario.show()
app.exec()
