from chart_manager import PDFChart
import constants as c
from qt_gui.config_dialog_qt import Ui_config_dialog, QtWidgets


class ConfigDialog(Ui_config_dialog, QtWidgets.QDialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(ConfigDialog, self).__init__(*args)
        self.setupUi(self)

        self.distributions = {
            c.BERNOULLI: self.bernoulli,
            c.BETA: self.beta,
            c.GAMMA: self.gamma,
            c.GUMBEL: self.gumbel,
            c.LAPLACE: self.laplace,
            c.LOGNORM: self.lognormal,
            c.NORM: self.norm,
            c.RAYLEIGH: self.rayleigh,
            c.UNIFORM: self.uniform,
            c.WEIBULL: self.weibull,
        }
        self.distribution_callback = None
        self.parameters_values = list()
        # self.pdf_chart = PDFChart()

        # Conexión de las señales de los botones
        self.btn_submit .clicked.connect(self.__pick_values)
        self.btn_reject.clicked.connect(self.close)
        self.radiobtn_1.toggled.connect(self.__radiobtn_checked)
        self.radiobtn_2.toggled.connect(self.__radiobtn_checked)
        self.radiobtn_3.toggled.connect(self.__radiobtn_checked)

        # Conexión de las señales de los spin
        self.parameter_spbox_1.valueChanged.connect(self.__update_preview)
        self.parameter_spbox_2.valueChanged.connect(self.__update_preview)
        self.parameter_spbox_3.valueChanged.connect(self.__update_preview)
        self.parameter_spbox_4.valueChanged.connect(self.__update_preview)

        self.__load_distribution(kwargs.get('distribution', 'Bernoulli'))
        self.setWindowTitle(f'Distribución-{kwargs.get("distribution")}')

    def closeEvent(self, event):
        """Sobre-escritura del método closeEvent para el cierre
            de la ventana."""
        self.reject()
        event.accept()

    def __load_distribution(self, distribution):
        if distribution in self.distributions:
            self.distribution_callback = self.distributions.get(distribution)
            self.distribution_callback(update=False)

    def __pick_values(self):
        for parameter_spbox in self.parameter_spboxes:
            if parameter_spbox.isVisible():
                self.parameters_values.append(parameter_spbox.value())
            else:
                self.parameters_values.append(float(0))
        print(self.parameters_values)
        self.accept()

    def __show_radio_buttons(self, f1, f2, f3):
        self.radiobtn_1.setVisible(f1)
        self.radiobtn_2.setVisible(f2)
        self.radiobtn_3.setVisible(f3)

    def __show_params(self, f1, f2, f3, f4):
        self.parameter_spbox_1.setVisible(f1)
        self.parameter_label_1.setVisible(f1)
        self.parameter_spbox_2.setVisible(f2)
        self.parameter_label_2.setVisible(f2)
        self.parameter_spbox_3.setVisible(f3)
        self.parameter_label_3.setVisible(f3)
        self.parameter_spbox_4.setVisible(f4)
        self.parameter_label_4.setVisible(f4)

    def __radiobtn_checked(self):
        btn = self.sender()
        if btn.isChecked() and btn.text() == '1P':
            self.__show_params(True, False, False, False)

        elif btn.isChecked() and btn.text() == '2P':
            self.__show_params(True, True, False, False)

        elif btn.isChecked() and btn.text() == '3P':
            self.__show_params(True, True, True, False)

    def __update_preview(self):
        self.distribution_callback(update=True)

    def bernoulli(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, False, False, False)
            self.parameter_label_1.setText(c.SUCCESS_PROB_LABEL)
            self.parameter_spbox_1.setMinimum(0.0)
            self.parameter_spbox_1.setMaximum(1.0)
            self.parameter_spbox_1.setValue(c.SUCCESS_PROB)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Bernoulli</small></center>
            ''',
            parameters={
                "success": self.parameter_spbox_1.value(),
                "fail": 1 - self.parameter_spbox_1.value(),
            }
        )
        self.pdf_chart.plot_bernoulli()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.BERNOULLI)

    def beta(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, True, True)
            self.parameter_label_1.setText(c.BETA_SHAPE_1_LABEL)
            self.parameter_spbox_1.setMinimum(0.01)
            self.parameter_spbox_1.setValue(c.BETA_SHAPE_1)
            self.parameter_label_2.setText(c.BETA_SHAPE_2_LABEL)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.BETA_SHAPE_2)
            self.parameter_label_3.setText(c.SHAPE)
            self.parameter_spbox_3.setMinimum(-1000)
            self.parameter_spbox_3.setValue(c.BETA_LOC)
            self.parameter_label_4.setText(c.LOCATION)
            self.parameter_spbox_4.setMinimum(0.01)
            self.parameter_spbox_4.setValue(c.BETA_SCALE)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución Beta</small></center>
            ''',
            parameters={
                "alpha": self.parameter_spbox_1.value(),
                "beta": self.parameter_spbox_2.value(),
                "a": self.parameter_spbox_3.value(),
                "b": self.parameter_spbox_4.value(),
            }
        )
        self.pdf_chart.plot_beta()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.BETA)

    def gamma(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.SHAPE)
            self.parameter_spbox_1.setMinimum(1)
            self.parameter_spbox_1.setValue(c.GAMMA_SHAPE)
            self.parameter_label_2.setText(c.SCALE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.GAMMA_SCALE)
            self.parameter_label_3.setText(c.LOCATION)
            self.parameter_spbox_3.setMinimum(-10)
            self.parameter_spbox_3.setValue(c.GAMMA_LOC)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Gamma</small></center>
            ''',
            parameters={
                "alpha": self.parameter_spbox_1.value(),
                "lmbda": self.parameter_spbox_2.value(),
                "gamma": self.parameter_spbox_3.value(),
            }
        )
        self.pdf_chart.plot_gamma()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.GAMMA)

    def gumbel(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.LOCATION)
            self.parameter_spbox_1.setMinimum(0)
            self.parameter_spbox_2.setValue(c.GUMBEL_LOC)
            self.parameter_label_2.setText(c.SCALE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.GUMBEL_SCALE)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Gumbel</small></center>
            ''',
            parameters={
                "mu": self.parameter_spbox_1.value(),
                "sigma": self.parameter_spbox_2.value(),
            }
        )
        self.pdf_chart.plot_gumbel()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.GUMBEL)

    def laplace(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.LOCATION)
            self.parameter_spbox_1.setMinimum(0)
            self.parameter_spbox_1.setValue(c.LAPLACE_LOC)
            self.parameter_label_2.setText(c.SCALE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.LAPLACE_SCALE)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Laplace</small></center>
            ''',
            parameters={
                "mu": self.parameter_spbox_1.value(),
                "b": self.parameter_spbox_2.value(),
            }
        )
        self.pdf_chart.plot_laplace()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.LAPLACE)

    def lognormal(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.LOCATION)
            self.parameter_spbox_1.setMinimum(-10)
            self.parameter_spbox_1.setValue(c.LOGNORM_LOC)
            self.parameter_label_2.setText(c.SHAPE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.LOGNORM_SHAPE)
            self.parameter_label_3.setText(c.SCALE)
            self.parameter_spbox_3.setMinimum(-10)
            self.parameter_spbox_3.setValue(c.LOGNORM_SCALE)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución Lognormal</small></center>
            ''',
            parameters={
                "mu": self.parameter_spbox_1.value(),
                "sigma": self.parameter_spbox_2.value(),
                "gamma": self.parameter_spbox_3.value(),
            }
        )
        self.pdf_chart.plot_lognorm()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.LOGNORM)

    def norm(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.LOCATION)
            self.parameter_spbox_1.setMinimum(0)
            self.parameter_spbox_1.setValue(c.NORM_LOC)
            self.parameter_label_2.setText(c.SCALE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.NORM_SCALE)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución Normal</small></center>
            ''',
            parameters={
                "mu": self.parameter_spbox_1.value(),
                "sigma": self.parameter_spbox_2.value(),
            }
        )
        self.pdf_chart.plot_norm()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.NORM)

    def rayleigh(self, update):
        if not update:
            self.__show_radio_buttons(True, True, False)
            self.__show_params(True, False, False, False)
            self.parameter_label_1.setText(c.SCALE)
            self.parameter_spbox_1.setMinimum(0.01)
            self.parameter_spbox_1.setValue(c.RAYLEIGH_SCALE)
            self.parameter_label_2.setText(c.LOCATION)
            self.parameter_spbox_2.setMinimum(0)
            self.parameter_spbox_2.setValue(c.RAYLEIGH_LOC)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Rayleigh</small></center>
            ''',
            parameters={
                "sigma": self.parameter_spbox_1.value(),
                "lmbda": self.parameter_spbox_2.value(),
            }
        )
        self.pdf_chart.plot_rayleigh()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.RAYLEIGH)

    def uniform(self, update):
        if not update:
            self.__show_radio_buttons(False, False, False)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.UNIFORM_INF_LABEL)
            self.parameter_spbox_1.setValue(c.UNIFORM_INF)
            self.parameter_label_2.setText(c.UNIFORM_SUP_LABEL)
            self.parameter_spbox_2.setValue(c.UNIFORM_SUP)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución Uniforme</small></center>
            ''',
            parameters={
                "inf": self.parameter_spbox_1.value(),
                "sup": self.parameter_spbox_2.value(),
            }
        )
        self.pdf_chart.plot_uniform()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.UNIFORM)

    def weibull(self, update):
        if not update:
            self.__show_radio_buttons(False, True, True)
            self.__show_params(True, True, False, False)
            self.parameter_label_1.setText(c.SHAPE)
            self.parameter_spbox_1.setMinimum(0.1)
            self.parameter_spbox_1.setValue(c.WEIBULL_SHAPE)
            self.parameter_label_2.setText(c.SCALE)
            self.parameter_spbox_2.setMinimum(0.01)
            self.parameter_spbox_2.setValue(c.WEIBULL_SCALE)
            self.parameter_label_3.setText(c.LOCATION)
            self.parameter_spbox_3.setMinimum(0)
            self.parameter_spbox_3.setValue(c.WEIBULL_LOC)

        self.pdf_chart = PDFChart(
            title='''
                Función de densidad de probabilidad
                <center><small>Distribución de Weibull</small></center>
            ''',
            parameters={
                "alpha": self.parameter_spbox_1.value(),
                "beta": self.parameter_spbox_2.value(),
                "gamma": self.parameter_spbox_3.value(),
            }
        )
        self.pdf_chart.plot_weibull()
        self.pdf_chartview.setChart(self.pdf_chart)

        self.distribution_callback = self.distributions.get(c.WEIBULL)
