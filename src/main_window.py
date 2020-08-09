from config_dialog import ConfigDialog
import generators as gen
import json_manager as manager
from qt_gui.main_window_qt import Ui_main_window, QtWidgets
from sim_window import SimWindow


GENERATORS = {
            "Bernoulli": gen.bernoulli,
            "Beta": gen.beta,
            "Gamma": gen.gamma,
            "Gumbel max": gen.gumbel,
            "Laplace": gen.laplace,
            "Lognormal": gen.lognormal,
            "Normal": gen.normal,
            "Rayleigh": gen.rayleigh,
            "Uniforme": gen.uniform,
            "Weibull": gen.weibull,
        }


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Construye la interfaz diseñada con qt

        self.__boxes = [
            self.pdf_1,
            self.pdf_2,
            self.pdf_3,
            self.pdf_4,
            self.pdf_5,
            self.pdf_6,
            self.pdf_7,
            self.pdf_8,
            self.pdf_9
        ]
        self.channels = {
            'channel_1': {
                'id': 1,
                'frequency': self.channel_1_label.text(),
            },
            'channel_2': {
                'id': 2,
                'frequency': self.channel_2_label.text(),
            },
            'channel_3': {
                'id': 3,
                'frequency': self.channel_3_label.text(),
            },
            'channel_4': {
                'id': 4,
                'frequency': self.channel_4_label.text(),
            },
            'channel_5': {
                'id': 5,
                'frequency': self.channel_5_label.text(),
            },
            'channel_6': {
                'id': 6,
                'frequency': self.channel_6_label.text(),
            },
            'channel_7': {
                'id': 7,
                'frequency': self.channel_7_label.text(),
            },
            'channel_8': {
                'id': 8,
                'frequency': self.channel_8_label.text(),
            },
            'channel_9': {
                'id': 9,
                'frequency': self.channel_9_label.text(),
            },
        }
        self.generators = list()

        manager.CONFIG['channels'] = self.channels.copy()

        # Conexión de las señales de los menús
        self.new_action_menu.triggered.connect(self.__new_sim)
        self.exit_action_menu.triggered.connect(self.close)
        self.about_action_menu.triggered.connect(self.__about)
        # self.help_action_menu.triggered.connect()

        # Conexión de las señales de los botones
        self.run_button.clicked.connect(self.__start_simulation)
        self.clean_button.clicked.connect(self.__reset_fields)
        self.save_file_button.clicked.connect(self.__save_config_file_as_json)
        self.load_file_button.clicked.connect(self.__load_config_file)

        # Conexión de los ComboBox al modal de parametrización
        for box in self.__boxes:
            box.activated.connect(self.__raise_modal)

    def __about(self):
        self.run_button.setEnabled(True)

    def closeEvent(self, event):
        """
            Sobre-escritura del método closeEvent para el cierre de la ventana.
        """
        # close = QtWidgets.QMessageBox.information(
        #     self,
        #     "Salir",
        #     "Estás seguro que deseas salir?",
        #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #     QtWidgets.QMessageBox.No
        # )
        # if close == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        event.accept()

    def __load_config(self, channels, parameters):
        self.channels = channels.copy()
        for key, value in self.channels.items():
            index = value.get("id")
            distribution = value.get("distribution")
            box = self.__boxes[index - 1]
            if distribution:
                box.setCurrentText(distribution.get("name", "Selecciona"))
                self.generators.insert(
                    index - 1,
                    GENERATORS.get(box.currentText())
                )
            else:
                box.setCurrentText("Selecciona")
        self.__verify_boxes()

        self.parameters = parameters.copy()
        self.threshold.setValue(self.parameters.get("threshold"))
        self.sample_time.setValue(self.parameters.get("sampling"))
        self.energy_flag.setChecked(self.parameters.get("energy"))
        self.usage_flag.setChecked(self.parameters.get("usage"))

    def __new_sim(self):
        self.__reset_fields()

    def __pick_settings_values(self):
        self.parameters = {
            "sampling": self.sample_time.value(),
            "threshold": self.threshold.value(),
            "energy": self.energy_flag.isChecked(),
            "usage": self.usage_flag.isChecked(),
        }

    def __raise_modal(self):
        for box in self.__boxes:
            if self.sender() == box:
                box_selected = box

        modal = ConfigDialog(self, distribution=box_selected.currentText())
        modal.exec()
        if modal.result() == 1:
            channel_id = self.__boxes.index(box_selected) + 1
            for key, value in self.channels.items():
                if channel_id == value["id"]:
                    value["distribution"] = {
                        "name": box_selected.currentText(),
                        "parameters": modal.parameters_values.copy()
                    }
                    self.generators.insert(
                        channel_id - 1,
                        GENERATORS.get(box_selected.currentText())
                    )
                    manager.CONFIG["channels"][key] = value.copy()
            del modal.parameters_values[:]
        else:
            self.sender().setCurrentIndex(0)
        self.__verify_boxes()

    def __reset_fields(self):
        self.sample_time.setValue(5)
        self.threshold.setValue(0.33)
        for box in self.__boxes:
            box.setCurrentIndex(0)
        self.__verify_boxes()

    def __start_simulation(self):
        self.__pick_settings_values()
        sim_window = SimWindow(
            self,
            channels=self.channels.copy(),
            parameters=self.parameters.copy(),
            generators=self.generators.copy()
        )
        sim_window.show()

    def __save_config_file_as_json(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Guardar configuración',
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            self.__pick_settings_values()
            manager.CONFIG["parameters"] = self.parameters.copy()
            manager.save_as_json(filepath)
            QtWidgets.QMessageBox.information(
                    self,
                    "Información",
                    "Archivo de configuración guardado en {}".format(filepath),
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )

    def __load_config_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Cargar configuración',
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            success = manager.load_json(filepath)
            if success:
                self.__load_config(
                    manager.CONFIG.get("channels"),
                    manager.CONFIG.get("parameters"),
                )
                QtWidgets.QMessageBox.information(
                    self,
                    "Información",
                    "Archivo de configuración cargado",
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )

    def __verify_boxes(self):
        for box in self.__boxes:
            if box.currentIndex() == 0:
                return self.run_button.setEnabled(False)
        self.run_button.setEnabled(True)


# Arranque de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
