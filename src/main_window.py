from config_dialog import ConfigDialog
import constants as c
import json_manager as manager
from qt_gui.main_window_qt import Ui_main_window, QtWidgets
from sim_window import SimWindow


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Construye la interfaz diseñada con qt

        self.channels = {
            'channel_1': {
                'id': 1,
                'frequency': self.label_channel_1.text(),
            },
            'channel_2': {
                'id': 2,
                'frequency': self.label_channel_2.text(),
            },
            'channel_3': {
                'id': 3,
                'frequency': self.label_channel_3.text(),
            },
            'channel_4': {
                'id': 4,
                'frequency': self.label_channel_4.text(),
            },
            'channel_5': {
                'id': 5,
                'frequency': self.label_channel_5.text(),
            },
            'channel_6': {
                'id': 6,
                'frequency': self.label_channel_6.text(),
            },
            'channel_7': {
                'id': 7,
                'frequency': self.label_channel_7.text(),
            },
            'channel_8': {
                'id': 8,
                'frequency': self.label_channel_8.text(),
            },
            'channel_9': {
                'id': 9,
                'frequency': self.label_channel_9.text(),
            },
        }
        self.generators = list()
        manager.SETTINGS[c.CHANNELS] = self.channels.copy()

        # Conexión de las señales de los menús
        self.new_action_menu.triggered.connect(self.__new_sim)
        self.exit_action_menu.triggered.connect(self.close)
        self.about_action_menu.triggered.connect(self.__about)
        self.help_action_menu.triggered.connect(self.__help)

        # Conexión de las señales de los botones
        self.btn_simulator.clicked.connect(self.__start_simulation)
        self.btn_clean.clicked.connect(self.__reset_fields)
        self.btn_save_file.clicked.connect(self.__save_config_file_as_json)
        self.btn_load_file.clicked.connect(self.__load_config_file)

        # Conexión de los ComboBox al modal de parametrización
        for box in self.boxes:
            box.activated.connect(self.__raise_modal)

    def __about(self):
        pass

    def closeEvent(self, event):
        """
            Sobre-escritura del método closeEvent para el cierre de la ventana.
        """
        # close = QtWidgets.QMessageBox.information(
        #     self,
        #     'Salir',
        #     c.EXIT_MESSAGE,
        #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #     QtWidgets.QMessageBox.No
        # )
        # if close == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        event.accept()

    def __help(self):
        pass

    def __load_config(self, channels, parameters):
        self.channels = channels.copy()
        self.parameters = parameters.copy()
        for channel, content in self.channels.items():
            index = content.get('id')
            distribution = content.get('distribution')
            box = self.boxes[index - 1]
            if distribution:
                box.setCurrentText(
                    distribution.get('name', c.BOX_DEFAULT_ITEM)
                )
                self.generators.insert(
                    index - 1,
                    c.GENERATORS.get(box.currentText())
                )
            else:
                box.setCurrentText(c.BOX_DEFAULT_ITEM)
        self.__check_boxes()
        self.energy_flag.setChecked(self.parameters.get(c.ENERGY))
        self.sample_time.setValue(self.parameters.get(c.SAMPLING))
        self.threshold.setValue(self.parameters.get(c.THRESHOLD))
        self.usage_flag.setChecked(self.parameters.get(c.USAGE))

    def __new_sim(self):
        self.__reset_fields()

    def __pick_settings_values(self):
        self.parameters = {
            c.SAMPLING: self.sample_time.value(),
            c.THRESHOLD: self.threshold.value(),
            c.ENERGY: self.energy_flag.isChecked(),
            c.USAGE: self.usage_flag.isChecked(),
        }

    def __raise_modal(self):
        for box in self.boxes:
            if self.sender() == box:
                box_selected = box

        modal = ConfigDialog(self, distribution=box_selected.currentText())
        modal.exec()
        if modal.result() == 1:
            channel_id = self.boxes.index(box_selected) + 1
            for channel, content in self.channels.items():
                if channel_id == content['id']:
                    content['distribution'] = {
                        'name': box_selected.currentText(),
                        c.PARAMETERS: modal.parameters_values.copy()
                    }
                    self.generators.insert(
                        channel_id - 1,
                        c.GENERATORS.get(box_selected.currentText())
                    )
                    manager.SETTINGS[c.CHANNELS][channel] = content.copy()
            del modal.parameters_values[:]
        else:
            self.sender().setCurrentIndex(-1)
        self.__check_boxes()

    def __reset_fields(self):
        self.sample_time.setValue(c.DEFAULT_SAMPLE_TIME)
        self.threshold.setValue(c.DEFAULT_THRESHOLD)
        for box in self.boxes:
            box.setCurrentIndex(-1)
        self.__check_boxes()

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
            c.SAVE_CONFIG,
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            self.__pick_settings_values()
            manager.SETTINGS['parameters'] = self.parameters.copy()
            manager.save_as_json(filepath)
            QtWidgets.QMessageBox.information(
                    self,
                    'Información',
                    f'{c.FILE_SAVED} en {filepath}',
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )

    def __load_config_file(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            c.LOAD_CONFIG,
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            success = manager.load_json(filepath)
            if success:
                self.__load_config(
                    manager.SETTINGS.get(c.CHANNELS),
                    manager.SETTINGS.get(c.PARAMETERS),
                )
                QtWidgets.QMessageBox.information(
                    self,
                    'Información',
                    c.FILE_LOADED,
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )

    def __check_boxes(self):
        for box in self.boxes:
            if box.currentIndex() == -1:  # -1 es el index del placeholder
                self.btn_simulator.setEnabled(False)
                self.btn_save_file.setEnabled(False)
                return
        self.btn_simulator.setEnabled(True)
        self.btn_save_file.setEnabled(True)


# Arranque de la aplicación
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
