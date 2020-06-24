from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis, QBarSeries, QBarSet, QValueAxis, QAbstractBarSeries, QLegend
from PyQt5.QtGui import QFont, QIcon, QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt, QMargins
from qt_gui.sim_window_qt import Ui_sim_window, QtWidgets
from chart_manager import ChartDesign


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)

        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        self.build_simulation()

        # Conexión de señales de los botones
        #self.save_chart_button.clicked.connect(self.chart.save_chart)

    # Sobre-escritura del método closeEvent para el cierre de la app
    def closeEvent(self, event):
        """close = QtWidgets.QMessageBox.information(self, 'Salir', "Estás seguro que cerrar la ventana/nde simulación?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        
        else:
            event.ignore()"""
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

        # Construimos el gráfico de barras con los porcentajes de ocupación en los canales
        self.chart = ChartDesign(
            title="%  Ocupación de los canales TDT",
            parameters=self.data,
            font_size=10
        )

        self.chart.plot_bars()
        self.chart_bars.setChart(self.chart)
