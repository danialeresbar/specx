from PyQt5 import QtWidgets
from qt_gui.main_window_qt import Ui_main_window
from config_dialog import ConfigDialog
from sim_window import SimWindow


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        # Diccionario con la configuración de la simulación
        self.data = {
            "simulation_params": {
                "sampling": self.sample_time.value(),
                "threshold": self.threshold.value(),
                "energy": self.energy_flag.isChecked(),
                "usage": self.usage_flag.isChecked(),
            },
            "channels": {
                "channel_1": {
                    "freq": self.channel_1_label.text(),
                    "box": self.pdf_1,
                },
                "channel_2": {
                    "freq": self.channel_2_label.text(),
                    "box": self.pdf_2,
                },
                "channel_3": {
                    "freq": self.channel_3_label.text(),
                    "box": self.pdf_3,
                },
                "channel_4": {
                    "freq": self.channel_4_label.text(),
                    "box": self.pdf_4,
                },
                "channel_5": {
                    "freq": self.channel_5_label.text(),
                    "box": self.pdf_5,
                },
                "channel_6": {
                    "freq": self.channel_6_label.text(),
                    "box": self.pdf_6,
                },
                "channel_7": {
                    "freq": self.channel_7_label.text(),
                    "box": self.pdf_7,
                },
                "channel_8": {
                    "freq": self.channel_8_label.text(),
                    "box": self.pdf_8,
                },
                "channel_9": {
                    "freq": self.channel_9_label.text(),
                    "box": self.pdf_9,
                },
            },
        }

        # Conexión de las señales de los menús
        self.new_action_menu.triggered.connect(self.new_sim)
        self.exit_action_menu.triggered.connect(self.close)
        self.about_action_menu.triggered.connect(self.about)
        #self.help_action_menu.triggered.connect()

        # Conexión de señales de los botones
        self.run_button.clicked.connect(self.run_sim)
        self.clean_button.clicked.connect(self.reset_fields)

        # Conexión de los ComboBox al modal de parametrización
        self.pdf_1.activated.connect(self.raise_modal)
        self.pdf_2.activated.connect(self.raise_modal)
        self.pdf_3.activated.connect(self.raise_modal)
        self.pdf_4.activated.connect(self.raise_modal)
        self.pdf_5.activated.connect(self.raise_modal)
        self.pdf_6.activated.connect(self.raise_modal)
        self.pdf_7.activated.connect(self.raise_modal)
        self.pdf_8.activated.connect(self.raise_modal)
        self.pdf_9.activated.connect(self.raise_modal)

    def run_sim(self):
        # Ventana de ejecución para el proceso de simulación
        sim_window = SimWindow(self)
        sim_window.receive_data(self.data)
        sim_window.show()
        #self.run_button.setEnabled(self.run_condition())

    def raise_modal(self, index):
        modal = ConfigDialog()
        config = modal.options.get(self.sender().currentIndex())

        if config:
            config()
            modal.exec()

            if modal.result() == 1:
                for k,v in self.data.get("channels").items():
                    if self.sender() == v.get("box"):
                        v['parameters'] = modal.parameters.copy()

                del modal.parameters[:]
                self.run_button.setEnabled(self.run_condition())

            else:
                self.sender().setCurrentIndex(0)

        else:
            return

    # Sobre-escritura del método closeEvent para el cierre de la app
    def closeEvent(self, event):
        """close = QtWidgets.QMessageBox.information(self, 'Salir', "Estás seguro que deseas salir?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        
        else:
            event.ignore()"""
        event.accept()

    def reset_fields(self):
        self.sample_time.setValue(5)
        self.threshold.setValue(0.33)
        self.run_button.setEnabled(False)
        boxes = [self.pdf_1, self.pdf_2, self.pdf_3, self.pdf_4, self.pdf_5, self.pdf_6, self.pdf_7, self.pdf_8, self.pdf_9]
        for box in boxes:
            box.setCurrentIndex(0)

    def new_sim(self):
        self.reset_fields()

    def about(self):
        self.run_button.setEnabled(True)

    def run_condition(self):
        boxes = [self.pdf_1, self.pdf_2, self.pdf_3, self.pdf_4, self.pdf_5, self.pdf_6, self.pdf_7, self.pdf_8, self.pdf_9]
        for box in boxes:
            if box.currentIndex() == 0:
                return False

        return True

# Arranque de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())