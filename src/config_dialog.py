from PyQt5 import QtWidgets
from qt_gui.config_dialog_qt import Ui_config_dialog


DEFAULT = 0.5

class ConfigDialog(Ui_config_dialog, QtWidgets.QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ConfigDialog, self).__init__(*args, **kwargs)
        
        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        # Diccionario de opciones para configuración del diálogo
        self.options = {
            1: self.bernoulli,
            2: self.beta,
            3: self.gamma,
            4: self.gumbel,
            5: self.laplace,
            6: self.lognormal,
            7: self.normal,
            8: self.rayleigh,
            9: self.uniform,
            10: self.weibull,
        }

        # Lista para almacenar los valores de los parámetros
        self.parameters = list()

        # Conexión de las señales de los botones
        self.submit_button.clicked.connect(self.pick_values)
        self.reject_button.clicked.connect(self.close)
        self.rb_1.toggled.connect(self.rb_action)
        self.rb_2.toggled.connect(self.rb_action)
        self.rb_3.toggled.connect(self.rb_action)

    # Sobre-escritura del método closeEvent para el cierre del cuadro de diálogo
    def closeEvent(self, event):        
        self.default_values()
        self.reject()
        event.accept()

    def default_values(self):
        self.param_1.setValue(DEFAULT)
        self.param_2.setValue(DEFAULT)
        self.param_3.setValue(DEFAULT)
        self.param_4.setValue(DEFAULT)

    def pick_values(self):
        params = [self.param_1, self.param_2, self.param_3, self.param_4]
        for param in params:
            if param.isVisible():
                self.parameters.append(param.value())
        
        self.accept()

    def enable_radio_buttons(self, f1, f2, f3):
        self.rb_1.setEnabled(f1)
        self.rb_2.setEnabled(f2)
        self.rb_3.setEnabled(f3)

    def set_visible_params(self, f1, f2, f3, f4):
        self.param_1.setVisible(f1)
        self.param_1_label.setVisible(f1)
        self.param_2.setVisible(f2)
        self.param_2_label.setVisible(f2)
        self.param_3.setVisible(f3)
        self.param_3_label.setVisible(f3)
        self.param_4.setVisible(f4)
        self.param_4_label.setVisible(f4)

    def rb_action(self):
        btn = self.sender()
        if btn.isChecked() and btn.text() == "1P":
            self.set_visible_params(True, False, False, False)
            
        elif btn.isChecked() and btn.text() == "2P":
            self.set_visible_params(True, True, False, False)

        elif btn.isChecked() and btn.text() == "3P":
            self.set_visible_params(True, True, True, False)

    def bernoulli(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, False, False, False)
        self.param_1_label.setText("Probabilidad\nde exito:")
        

    def beta(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, True, True)
        self.param_1_label.setText("Parámetro de\nforma alpha:")
        self.param_2_label.setText("Parámetro de\nforma beta:")
        self.param_3_label.setText("Parámetro de\nubicación:")
        self.param_4_label.setText("Parámetro de\nescala:")

    def gamma(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nforma:")
        self.param_2_label.setText("Parámetro de\nescala:")

    def gumbel(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nubicación:")
        self.param_2_label.setText("Parámetro de\nescala:")

    def laplace(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nubicación:")
        self.param_2_label.setText("Parámetro de\nescala:")

    def lognormal(self):
        self.enable_radio_buttons(False, True, True)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nubicación:")
        self.param_2_label.setText("Parámetro de\nforma:")
        self.param_3_label.setText("Parámetro de\nescala:")

    def normal(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nubicación:")
        self.param_2_label.setText("Parámetro de\nforma:")

    def rayleigh(self):
        self.enable_radio_buttons(True, True, False)
        self.set_visible_params(True, False, False, False)
        self.param_1_label.setText("Parámetro de\nforma:")
        self.param_2_label.setText("Parámetro de\nescala:")

    def uniform(self):
        self.enable_radio_buttons(False, False, False)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\ncota inferior:")
        self.param_2_label.setText("Parámetro de\ncota superior:")

    def weibull(self):
        self.enable_radio_buttons(False, True, True)
        self.set_visible_params(True, True, False, False)
        self.param_1_label.setText("Parámetro de\nforma:")
        self.param_2_label.setText("Parámetro de\nescala:")
        self.param_3_label.setText("Parámetro de\nubicación:")