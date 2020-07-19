from qt_gui.config_dialog_qt import Ui_config_dialog, QtWidgets
from chart_manager import ChartDesign


class ConfigDialog(Ui_config_dialog, QtWidgets.QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ConfigDialog, self).__init__(*args)
        self.setupUi(self)

        self.distributions = {
            "Bernoulli": self.bernoulli,
            "Beta": self.beta,
            "Gamma": self.gamma,
            "Gumbel max": self.gumbel,
            "Laplace": self.laplace,
            "Lognormal": self.lognormal,
            "Normal": self.norm,
            "Rayleigh": self.rayleigh,
            "Uniforme": self.uniform,
            "Weibull": self.weibull,
        }

        self.distribution_callback = None
        self.__load_default_values()
        self.parameters_values = list()
        self.chart = ChartDesign()

        # Conexión de las señales de los botones
        self.submit_button.clicked.connect(self.__pick_values)
        self.reject_button.clicked.connect(self.close)
        self.rb_1.toggled.connect(self.__button_checked)
        self.rb_2.toggled.connect(self.__button_checked)
        self.rb_3.toggled.connect(self.__button_checked)

        # Conexión de las señales de los spin
        self.param_1.valueChanged.connect(self.__update_plot)
        self.param_2.valueChanged.connect(self.__update_plot)
        self.param_3.valueChanged.connect(self.__update_plot)
        self.param_4.valueChanged.connect(self.__update_plot)

        self.__load_distribution(kwargs.get("distribution"))

    def closeEvent(self, event):
        self.reject()
        event.accept()

    def __load_distribution(self, distribution):
        if distribution in self.distributions:
            self.distribution_callback = self.distributions.get(distribution)
            self.distribution_callback(update=False)

    def __load_default_values(self):
        self.param_1.setValue(0.5)
        self.param_2.setValue(0.2)
        self.param_3.setValue(0.2)
        self.param_4.setValue(0.5)

    def __pick_values(self):
        params = [self.param_1, self.param_2, self.param_3, self.param_4]
        for param in params:
            if param.isVisible():
                self.parameters_values.append(param.value())
        self.accept()

    def __show_radio_buttons(self, f1, f2, f3):
        self.rb_1.setVisible(f1)
        self.rb_2.setVisible(f2)
        self.rb_3.setVisible(f3)

    def __show_params(self, f1, f2, f3, f4):
        self.param_1.setVisible(f1)
        self.param_1_label.setVisible(f1)
        self.param_2.setVisible(f2)
        self.param_2_label.setVisible(f2)
        self.param_3.setVisible(f3)
        self.param_3_label.setVisible(f3)
        self.param_4.setVisible(f4)
        self.param_4_label.setVisible(f4)

    def __button_checked(self):
        btn = self.sender()
        if btn.isChecked() and btn.text() == "1P":
            self.__show_params(True, False, False, False)

        elif btn.isChecked() and btn.text() == "2P":
            self.__show_params(True, True, False, False)

        elif btn.isChecked() and btn.text() == "3P":
            self.__show_params(True, True, True, False)

    def __update_plot(self):
        self.distribution_callback(update=True)

    def bernoulli(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, False, False, False)
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
        self.chart.plot_bernoulli()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Bernoulli")

    def beta(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, True, True)
            self.param_1_label.setText("Parámetro de\nforma alpha:")
            self.param_1.setMinimum(0.01)
            self.param_2_label.setText("Parámetro de\nforma beta:")
            self.param_2.setMinimum(0.01)
            self.param_3_label.setText("Parámetro de\nubicación:")
            self.param_3.setMinimum(-1000)
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
        self.chart.plot_beta()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Beta")

    def gamma(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_gamma()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Gamma")

    def gumbel(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_gumbel()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Gumbel max")

    def laplace(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_laplace()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Laplace")

    def lognormal(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_lognorm()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Lognormal")

    def norm(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_norm()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Normal")

    def rayleigh(self, update):
        if "update" not in self.distributions.keys():
            self.__show_radio_buttons(True, True, False)
            self.__show_params(True, False, False, False)
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
        self.chart.plot_rayleigh()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Rayleigh")

    def uniform(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
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
        self.chart.plot_uniform()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Uniforme")

    def weibull(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
            self.param_1_label.setText("Parámetro de\nforma:")
            self.param_1.setMinimum(0.15)
            self.param_2_label.setText("Parámetro de\nescala:")
            self.param_2.setMinimum(0.15)
            self.param_3_label.setText("Parámetro de\nubicación:")
            self.param_3.setMinimum(0.01)

        self.chart = ChartDesign(
            title="Función de densidad de probabilidad",
            parameters={
                "gamma": self.param_1.value(),
                "alpha": self.param_2.value(),
                "mu": self.param_3.value(),
            },
            font_size=10
        )
        self.chart.plot_weibull()
        self.chart_view.setChart(self.chart)

        self.distribution_callback = self.distributions.get("Weibull")
