from PyQt5 import QtWidgets, uic

#Iniciar la app
app = QtWidgets.QApplication([])

#Cargar archivos .iu
login = uic.loadUi("ventana1.ui")
entrar = uic.loadUi("ventana2.ui")

def gui_login():
    name = login.txtUser.text()
    password = login.txtContra.text()

    if len(name) == 0 or len(password) == 0:
        login.lblFalta.setText("Faltan datos")
    elif name == "Chris" and password == "123456":
        gui_entrar()

def gui_entrar():
    login.hide()
    entrar.show()


#Botones
login.btnIngresar.clicked.connect(gui_login)

#Ejecutable
login.show()
app.exec()


