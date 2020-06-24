from qt_gui.config_dialog_qt import Ui_config_dialog, QtWidgets
from chart_manager import ChartDesign


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
            7: self.norm,
            8: self.rayleigh,
            9: self.uniform,
            10: self.weibull,
        }

        # Configura los valores iniciales de los parámetros
        self.default_param_values()

        # Lista para almacenar los valores de los parámetros
        self.parameters = list()

        self.chart = ChartDesign()

        # Conexión de las señales de los botones
        self.submit_button.clicked.connect(self.pick_values)
        self.reject_button.clicked.connect(self.close)
        self.rb_1.toggled.connect(self.rb_action)
        self.rb_2.toggled.connect(self.rb_action)
        self.rb_3.toggled.connect(self.rb_action)

        # Conexión de las señales de los spin
        self.param_1.valueChanged.connect(self.update_plot)
        self.param_2.valueChanged.connect(self.update_plot)
        self.param_3.valueChanged.connect(self.update_plot)
        self.param_4.valueChanged.connect(self.update_plot)

    # Sobre-escritura del método closeEvent para el cierre del cuadro de diálogo
    def closeEvent(self, event):        
        self.reject()
        event.accept()

    def default_param_values(self):
        self.param_1.setValue(0.5)
        self.param_2.setValue(0.5)
        self.param_3.setValue(0.5)
        self.param_4.setValue(0.5)

    def pick_values(self):
        params = [self.param_1, self.param_2, self.param_3, self.param_4]
        for param in params:
            if param.isVisible():
                self.parameters.append(param.value())
        
        self.accept()

    def show_radio_buttons(self, f1, f2, f3):
        self.rb_1.setVisible(f1)
        self.rb_2.setVisible(f2)
        self.rb_3.setVisible(f3)

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

    def update_plot(self):
        for k, v in self.options.items():
            if self.options.get("update") == k:
                v()
    
    def bernoulli(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, False, False, False)
            self.param_1_label.setText("Probabilidad\nde exito:")
            self.param_1.setMinimum(0.0)
            self.param_1.setMaximum(1.0)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "success": self.param_1.value(),
                "fail": 1 - self.param_1.value(),
            },
            font_size=10
        )

        # Vista preliminar
        self.chart.plot_bernoulli()
        self.chart_view.setChart(self.chart)

        self.options["update"] = 1

    def beta(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, True, True, True)
            self.param_1_label.setText("Parámetro de\nforma alpha:")
            self.param_1.setMinimum(0.01)
            self.param_2_label.setText("Parámetro de\nforma beta:")
            self.param_2.setMinimum(0.01)
            self.param_3_label.setText("Parámetro de\nubicación:")
            self.param_3.setMinimum(-1000000)
            self.param_4_label.setText("Parámetro de\nescala:")
            self.param_4.setMinimum(0.01)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "alpha": self.param_1.value(),
                "beta": self.param_2.value(),
                "a": self.param_3.value(),
                "b": self.param_4.value(),
            },
            font_size=10
        )

        # Vista preliminar
        self.chart.plot_beta()
        self.chart_view.setChart(self.chart)

        self.options["update"] = 2

    def gamma(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, True, True)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nforma:")
            self.param_1.setMinimum(1)
            self.param_2_label.setText("Parámetro de\nescala:")
            self.param_2.setMinimum(0.01)
            self.param_3_label.setText("Parámetro de\nubicación:")
            self.param_3.setMinimum(0)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "alpha": self.param_1.value(),
                "lmbda": self.param_2.value(),
                "gamma": self.param_3.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_gamma()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 3

    def gumbel(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nubicación:")
            self.param_1.setMinimum(0)
            self.param_2_label.setText("Parámetro de\nescala:")
            self.param_2.setMinimum(0.01)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "mu": self.param_1.value(),
                "sigma": self.param_2.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_gumbel()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 4

    def laplace(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nubicación:")
            self.param_1.setMinimum(0)
            self.param_2_label.setText("Parámetro de\nescala:")
            self.param_2.setMinimum(0.01)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "mu": self.param_1.value(),
                "b": self.param_2.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_laplace()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 5

    def lognormal(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, True, True)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nubicación:")
            self.param_1.setMinimum(0)
            self.param_2_label.setText("Parámetro de\nforma:")
            self.param_2.setMinimum(0.01)
            self.param_3_label.setText("Parámetro de\nescala:")
            self.param_3.setMinimum(0.01)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "mu": self.param_1.value(),
                "sigma": self.param_2.value(),
                "gamma": self.param_3.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_lognorm()
        self.chart_view.setChart(self.chart)
        
        
        self.options["update"] = 6

    def norm(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nubicación:")
            self.param_1.setMinimum(0)
            self.param_2_label.setText("Parámetro de\nforma:")
            self.param_2.setMinimum(0.01)
        
        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "mu": self.param_1.value(),
                "sigma": self.param_2.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_norm()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 7

    def rayleigh(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(True, True, False)
            self.set_visible_params(True, False, False, False)
            self.param_1_label.setText("Parámetro de\nescala:")
            self.param_1.setMinimum(0.01)
            self.param_2_label.setText("Parámetro de\nubicación:")
            self.param_2.setMinimum(0)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "sigma": self.param_1.value(),
                "lmbda": self.param_2.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_rayleigh()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 8

    def uniform(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, False, False)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\ncota inferior:")
            self.param_2_label.setText("Parámetro de\ncota superior:")

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "inf": self.param_1.value(),
                "sup": self.param_2.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_uniform()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 9

    def weibull(self):
        if not "update" in self.options.keys():
            self.show_radio_buttons(False, True, True)
            self.set_visible_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nforma:")
            self.param_1.setMinimum(0.01)
            self.param_2_label.setText("Parámetro de\nescala:")
            self.param_2.setMinimum(0.01)
            self.param_3_label.setText("Parámetro de\nubicación:")
            self.param_3.setMinimum(0)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "gamma": self.param_1.value(),
                "alpha": self.param_2.value(),
                "mu": self.param_3.value(),
            },
            font_size=10
        )
        
        # Vista preliminar
        self.chart.plot_weibull()
        self.chart_view.setChart(self.chart)
        
        self.options["update"] = 10        
