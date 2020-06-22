from PyQt5 import QtWidgets
from qt_gui.sim_window_qt import Ui_sim_window


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)

        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        # Conexión de señales de los botones
        

    # Sobre-escritura del método closeEvent para el cierre de la app
    def closeEvent(self, event):
        """close = QtWidgets.QMessageBox.information(self, 'Salir', "Estás seguro que cerrar la ventana/nde simulación?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        
        else:
            event.ignore()"""
        event.accept()    

    def receive_data(self, data):
        self.data = data.copy()
        for k, v in self.data.get("channels").items():
            print("{} --> {}".format(k, v))


# Arranque de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SimWindow()
    window.show()
    sys.exit(app.exec_())