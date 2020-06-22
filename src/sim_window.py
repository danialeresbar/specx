from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis, QBarSeries, QBarSet, QValueAxis, QAbstractBarSeries
from PyQt5.QtGui import QFont, QIcon, QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt, QMargins
from qt_gui.sim_window_qt import Ui_sim_window


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)

        # Construye la interfaz diseñada con qt
        self.setupUi(self)

        self.build_simulation()

        # Conexión de señales de los botones
        self.save_chart_button.clicked.connect(self.save_chart)

    # Sobre-escritura del método closeEvent para el cierre de la app
    def closeEvent(self, event):
        """close = QtWidgets.QMessageBox.information(self, 'Salir', "Estás seguro que cerrar la ventana/nde simulación?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        
        else:
            event.ignore()"""
        event.accept()

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
        self.chart_view = QChartView(self.bar_chart())
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_layout.addWidget(self.chart_view)

    def bar_chart(self):
        # Etiquetas para eje x
        font = QFont()
        font.setPointSize(10)
        freqs = list()
        for k, v in self.data.items():
            freqs.append(v.get("freq"))

        chart = QChart()
        chart.setMargins(QMargins(5, 5, 5, 5))
        chart.setTitleFont(font)
        chart.setTitle("%  Ocupación de los canales TDT")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeQt)
        
        # Valores de prueba eje Y
        values = [24.32, 14.85, 8.91, 12.54, 7.85, 31.53, 66.84, 14.68, 95.32]
        for index in range(len(values)):
            series = QBarSeries()
            
            bar_set = QBarSet(freqs[index])
            #bar_set.setColor(colores[index])
            bar_set.setLabelColor(Qt.black)
            bar_set.setLabelFont(font)
            bar_set.append(values[index])
            
            series.append(bar_set)
            series.setLabelsVisible(True)
            #series.setLabelsAngle(-90)
            series.setLabelsFormat("@value %")
            if values[index] < 20:
                series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

            else:
                series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            
            chart.addSeries(series)


        axis_x = QBarCategoryAxis()
        axis_x.append(freqs)
        axis_x.setLabelsFont(font)

        axis_y = QValueAxis()
        axis_y.setRange(0, 100)
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.2f %")
        axis_y.setLabelsFont(font)

        chart.createDefaultAxes()
        chart.setAxisX(axis_x, None)
        chart.setAxisY(axis_y, None)

        chart.legend().setVisible(True)
        chart.legend().setFont(font)
        chart.legend().setAlignment(Qt.AlignBottom)

        return chart

    def save_chart(self):
        name, ext = QtWidgets.QFileDialog.getSaveFileName(
            self, "Guardar como",
            "Gráfico de barras",
            "JPG (*.jpg);;PNG (*.png);;SVG (*.svg)",
            options=QtWidgets.QFileDialog.Options()
            )
                
        if name:
            file = QPixmap(self.chart_view.grab())
            file.save(name, quality = 100)

            if file:
                QtWidgets.QMessageBox.information(self, "Guardar gráfico", "Gráfico guardado con éxito.",
                                        QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(self, "Guardar gráfico", "Error al guardar el gráfico.", QtWidgets.QMessageBox.Ok)
