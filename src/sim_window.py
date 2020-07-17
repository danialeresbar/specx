from qt_gui.sim_window_qt import Ui_sim_window, QtWidgets
from chart_manager import ChartDesign
from thread import GeneratorThread
from uuid import uuid4
# from key import DynamicSpline


DEFAULT_SPEED = 1
MAX_SPEED = 64
MIN_SPEED = 1/MAX_SPEED


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Construye la interfaz diseñada con qt

        self._sim_button_mannager(False, True, True)
        self._build_simulation()

        # Conexión de señales de los botones
        self.play_button.clicked.connect(self.resume)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)
        self.increase_time_speed_button.clicked.connect(self.increase_speed)
        self.decrease_time_speed_button.clicked.connect(self.decrease_speed)
        self.max_time_speed_button.clicked.connect(self.max_speed)
        self.defaultt_time_speed_button.clicked.connect(self.default_speed)
        # self.save_chart_button.clicked.connect(self.chart.save_chart)

    def closeEvent(self, event):
        '''Sobre-escritura del método closeEvent para el cierre de la app'''
        # close = QtWidgets.QMessageBox.information(
        #     self,
        #     'Salir',
        #     "Seguro que desea cerrar la ventana de simulación?",
        #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #     QtWidgets.QMessageBox.No
        # )
        # if close == QtWidgets.QMessageBox.Yes:
        #     event.accept()

        # else:
        #     event.ignore()
        event.accept()

    # Prepara el escenario de simulación
    def _build_simulation(self):
        self.speed = 1
        self.data = self.parent().data.copy()

        # Gráfico de barras con los porcentajes de ocupación de los canales
        self.chart = ChartDesign(
            title="%  Ocupación de los canales TDT",
            parameters=self.data,
            font_size=10
        )

        self.chart.plot_bar_chart()
        self.chart_bars.setChart(self.chart)

        self.thread = GeneratorThread(
            target=self.get_speed_value,
            kwargs=self.data,
            name="Simulation-{}".format(uuid4())
        )
        self.thread.setDaemon(True)
        self.thread.start()

        # chart_1 = DynamicSpline()
        # #chart_1.setTitle("Gráfico de prueba")
        # chart_1.legend().hide()
        # chart_1.layout().setContentsMargins(0, 0, 0, 0)
        # chart_1.setBackgroundRoundness(0)
        # chart_1.setMargins(QMargins(0, 0, 0, 0))
        # chart_1.setAnimationOptions(QChart.SeriesAnimations)

    def resume(self):
        self.thread.resume()
        self._sim_button_mannager(False, True, True)

    def pause(self):
        self.thread.pause()
        self._sim_button_mannager(True, False, True)

    def stop(self):
        if self.thread.paused:
            self.thread.resume()
            self.thread.stop()
        else:
            self.thread.stop()
        self._sim_button_mannager(True, False, False)

    def get_speed_value(self):
        return self.speed

    def increase_speed(self):
        global MAX_SPEED
        self.speed *= 2
        self._speed_button_mannager(True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MAX_SPEED:
            self._speed_button_mannager(False, True, True)

    def decrease_speed(self):
        global MIN_SPEED
        self.speed /= 2
        self._speed_button_mannager(True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MIN_SPEED:
            self._speed_button_mannager(True, False, True)

    def default_speed(self):
        global DEFAULT_SPEED
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self._speed_button_mannager(True, True, True)

    def max_speed(self):
        global MAX_SPEED
        self.speed = MAX_SPEED
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self._speed_button_mannager(False, True, True)

    def _sim_button_mannager(self, f1, f2, f3):
        self.play_button.setEnabled(f1)
        self.pause_button.setEnabled(f2)
        self.stop_button.setEnabled(f3)

    def _speed_button_mannager(self, f1, f2, f3):
        self.increase_time_speed_button.setEnabled(f1)
        self.decrease_time_speed_button.setEnabled(f2)
        self.max_time_speed_button.setEnabled(f3)
        pass
