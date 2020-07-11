from qt_gui.sim_window_qt import Ui_sim_window, QtWidgets
from chart_manager import ChartDesign
# from key import DynamicSpline


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)

        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        self.build_simulation()

        # Conexión de señales de los botones
        # self.save_chart_button.clicked.connect(self.chart.save_chart)

    # Sobre-escritura del método closeEvent para el cierre de la app
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.information(
            self,
            'Salir',
            "Seguro que desea cerrar la ventana de simulación?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()
        event.accept()

    # Prepara el escenario de simulación
    def build_simulation(self):
        self.data = self.parent().data.copy()
        """for k, v in self.data.items():
            print("{} --> {}".format(k, v))"""

        self.sim_parameters = {
            "sampling": self.parent().sample_time.value(),
            "threshold": self.parent().threshold.value(),
            "energy": self.parent().energy_flag.isChecked(),
            "usage": self.parent().usage_flag.isChecked(),
        }

        # Gráfico de barras con los porcentajes de ocupación de los canales
        self.chart = ChartDesign(
            title="%  Ocupación de los canales TDT",
            parameters=self.data,
            font_size=10
        )

        self.chart.plot_bar_chart()
        self.chart_bars.setChart(self.chart)

        """chart_1 = DynamicSpline()
        #chart_1.setTitle("Gráfico de prueba")
        chart_1.legend().hide()
        chart_1.layout().setContentsMargins(0, 0, 0, 0)
        chart_1.setBackgroundRoundness(0)
        chart_1.setMargins(QMargins(0, 0, 0, 0))
        chart_1.setAnimationOptions(QChart.SeriesAnimations)

        chart_2 = DynamicSpline()
        #chart_2.setTitle("Gráfico de prueba")
        chart_2.legend().hide()
        chart_2.layout().setContentsMargins(0, 0, 0, 0)
        chart_2.setBackgroundRoundness(0)
        chart_2.setMargins(QMargins(0, 0, 0, 0))
        chart_2.setAnimationOptions(QChart.SeriesAnimations)

        chart_3 = DynamicSpline()
        #chart_3.setTitle("Gráfico de prueba")
        chart_3.legend().hide()
        chart_3.layout().setContentsMargins(0, 0, 0, 0)
        chart_3.setBackgroundRoundness(0)
        chart_3.setMargins(QMargins(0, 0, 0, 0))
        chart_3.setAnimationOptions(QChart.SeriesAnimations)

        chart_4 = DynamicSpline()
        #chart_4.setTitle("Gráfico de prueba")
        chart_4.legend().hide()
        chart_4.layout().setContentsMargins(0, 0, 0, 0)
        chart_4.setBackgroundRoundness(0)
        chart_4.setMargins(QMargins(0, 0, 0, 0))
        chart_4.setAnimationOptions(QChart.SeriesAnimations)

        chart_5 = DynamicSpline()
        #chart_5.setTitle("Gráfico de prueba")
        chart_5.legend().hide()
        chart_5.layout().setContentsMargins(0, 0, 0, 0)
        chart_5.setBackgroundRoundness(0)
        chart_5.setMargins(QMargins(0, 0, 0, 0))
        chart_5.setAnimationOptions(QChart.SeriesAnimations)

        self.chart_test_1.setChart(chart_1)
        self.chart_test_2.setChart(chart_2)
        self.chart_test_3.setChart(chart_3)
        self.chart_test_4.setChart(chart_4)
        self.chart_test_5.setChart(chart_5)"""
