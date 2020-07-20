from chart_manager import ChartDesign
from qt_gui.sim_window_qt import Ui_sim_window, QtWidgets
from PyQt5.QtGui import QPixmap
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

        self.channels = kwargs.get("channels", None)
        self.parameters = kwargs.get("parameters", None)
        self.speed = 1

        self.__sim_button_mannager(True, False, False, False)
        self.__speed_button_mannager(False, False, False, False)
        self._build_simulation()

        # Conexión de señales de los botones
        self.start_button.clicked.connect(self.__start)
        self.play_button.clicked.connect(self.__resume)
        self.pause_button.clicked.connect(self.__pause)
        self.stop_button.clicked.connect(self.__stop)
        self.increase_time_speed_button.clicked.connect(self.increase_speed)
        self.decrease_time_speed_button.clicked.connect(self.decrease_speed)
        self.max_time_speed_button.clicked.connect(self.__max_speed)
        self.defaultt_time_speed_button.clicked.connect(self.__default_speed)
        self.save_chart_button.clicked.connect(self.save_chart)

    def closeEvent(self, event):
        '''Sobre-escritura del método closeEvent para el cierre de la app'''
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

    def _build_simulation(self):
        self.chart_channels_usage = ChartDesign(
            title="%  Ocupación de los canales TDT",
            parameters=self.channels.copy()
        )
        self.chart_channels_usage.plot_bar_chart()
        self.chart_bars_view.setChart(self.chart_channels_usage)

        # chart_1 = DynamicSpline()
        # #chart_1.setTitle("Gráfico de prueba")
        # chart_1.legend().hide()
        # chart_1.layout().setContentsMargins(0, 0, 0, 0)
        # chart_1.setBackgroundRoundness(0)
        # chart_1.setMargins(QMargins(0, 0, 0, 0))
        # chart_1.setAnimationOptions(QChart.SeriesAnimations)

    def save_chart(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Guardar como",
            "chart",
            "JPG (*.jpg);;PNG (*.png)",
            options=QtWidgets.QFileDialog.Options()
            )

        if filepath:
            outfile = QPixmap(self.chart_bars_view.grab())
            outfile.save(filepath, quality=100)

            if outfile:
                QtWidgets.QMessageBox.information(
                    self,
                    "Guardar gráfico",
                    "Gráfico guardado con éxito.",
                    QtWidgets.QMessageBox.Ok
                )
            else:
                QtWidgets.QMessageBox.critical(
                    self,
                    "Guardar gráfico",
                    "Error al guardar el gráfico.",
                    QtWidgets.QMessageBox.Ok
                )

    def __start(self):
        self.__thread = GeneratorThread(
            target=self.get_speed_value,
            kwargs={
                "channels": self.channels.copy(),
                "parameters": self.parameters.copy(),
                "callback": self.__finish_sim
            },
            name="Simulation-{}".format(uuid4())
        )
        self.__thread.setDaemon(True)
        self.__thread.start()
        self.__sim_button_mannager(False, False, True, True)
        self.__speed_button_mannager(True, True, True, True)

    def __resume(self):
        self.__thread.resume()
        self.__sim_button_mannager(False, False, True, True)

    def __pause(self):
        self.__thread.pause()
        self.__sim_button_mannager(False, True, False, True)

    def __stop(self):
        if self.__thread.is_alive:
            if self.__thread.paused:
                self.__thread.resume()
                self.__thread.stop()
            else:
                self.__thread.stop()
            self.__speed_button_mannager(True, False, False, False)
            self.__sim_button_mannager(False, False, False, False)

    def get_speed_value(self):
        return self.speed

    def increase_speed(self):
        global MAX_SPEED
        self.speed *= 2
        self.__speed_button_mannager(True, True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MAX_SPEED:
            self.__speed_button_mannager(False, True, True, True)

    def decrease_speed(self):
        global MIN_SPEED
        self.speed /= 2
        self.__speed_button_mannager(True, True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == MIN_SPEED:
            self.__speed_button_mannager(True, False, True, True)

    def __default_speed(self):
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(True, True, True, True)

    def __max_speed(self):
        global MAX_SPEED
        self.speed = MAX_SPEED
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(False, True, True, True)

    def __sim_button_mannager(self, f1, f2, f3, f4):
        self.start_button.setEnabled(f1)
        self.play_button.setEnabled(f2)
        self.pause_button.setEnabled(f3)
        self.stop_button.setEnabled(f4)

    def __speed_button_mannager(self, f1, f2, f3, f4):
        self.increase_time_speed_button.setEnabled(f1)
        self.decrease_time_speed_button.setEnabled(f2)
        self.max_time_speed_button.setEnabled(f3)
        self.defaultt_time_speed_button.setEnabled(f4)
        pass

    def __finish_sim(self):
        self.__sim_button_mannager(True, False, False, False)
        self.__speed_button_mannager(False, False, False, False)
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
