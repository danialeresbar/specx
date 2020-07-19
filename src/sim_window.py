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
        super(SimWindow, self).__init__(*args)
        self.setupUi(self)  # Construye la interfaz diseñada con qt

        self.__sim_button_mannager(False, True, True)
        self._build_simulation(
            kwargs.get("channels", None),
            kwargs.get("parameters", None)
        )

        # Conexión de señales de los botones
        self.play_button.clicked.connect(self.__resume)
        self.pause_button.clicked.connect(self.__pause)
        self.stop_button.clicked.connect(self.__stop)
        self.increase_time_speed_button.clicked.connect(self.increase_speed)
        self.decrease_time_speed_button.clicked.connect(self.decrease_speed)
        self.max_time_speed_button.clicked.connect(self.__max_speed)
        self.defaultt_time_speed_button.clicked.connect(self.__default_speed)
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
    def _build_simulation(self, channels, parameters):
        self.speed = 1
        self.chart = ChartDesign(
            title="%  Ocupación de los canales TDT",
            parameters=channels,
            font_size=10
        )

        self.chart.plot_bar_chart()
        self.chart_bars.setChart(self.chart)

        self.__thread = GeneratorThread(
            target=self.get_speed_value,
            kwargs=channels,
            name="Simulation-{}".format(uuid4())
        )
        # self.__thread.setDaemon(True)
        # self.__thread.start()

        # chart_1 = DynamicSpline()
        # #chart_1.setTitle("Gráfico de prueba")
        # chart_1.legend().hide()
        # chart_1.layout().setContentsMargins(0, 0, 0, 0)
        # chart_1.setBackgroundRoundness(0)
        # chart_1.setMargins(QMargins(0, 0, 0, 0))
        # chart_1.setAnimationOptions(QChart.SeriesAnimations)

    def __resume(self):
        self.__thread.__resume()
        self.__sim_button_mannager(False, True, True)

    def __pause(self):
        self.__thread.__pause()
        self.__sim_button_mannager(True, False, True)

    def __stop(self):
        if self.__thread.paused:
            self.__thread.__resume()
            self.__thread.__stop()
        else:
            self.__thread.__stop()
        self.__sim_button_mannager(True, False, False)
        self.__default_speed()

    def get_speed_value(self):
        return self.speed

    def increase_speed(self):
        global MAX_SPEED
        self.speed *= 2
        self.__speed_button_mannager(True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MAX_SPEED:
            self.__speed_button_mannager(False, True, True)

    def decrease_speed(self):
        global MIN_SPEED
        self.speed /= 2
        self.__speed_button_mannager(True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MIN_SPEED:
            self.__speed_button_mannager(True, False, True)

    def __default_speed(self):
        global DEFAULT_SPEED
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(True, True, True)

    def __max_speed(self):
        global MAX_SPEED
        self.speed = MAX_SPEED
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(False, True, True)

    def __sim_button_mannager(self, f1, f2, f3):
        self.play_button.setEnabled(f1)
        self.pause_button.setEnabled(f2)
        self.stop_button.setEnabled(f3)

    def __speed_button_mannager(self, f1, f2, f3):
        self.increase_time_speed_button.setEnabled(f1)
        self.decrease_time_speed_button.setEnabled(f2)
        self.max_time_speed_button.setEnabled(f3)
        pass
