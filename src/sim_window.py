from chart_manager import BarChart, LineChart, SplineChart
import constants as c
from datetime import datetime
from qt_gui.sim_window_qt import Ui_sim_window, QtWidgets
from PyQt5.QtGui import QPixmap
from thread import FileThread, SimulationThread
from uuid import uuid4


class SimWindow(QtWidgets.QMainWindow, Ui_sim_window):
    def __init__(self, *args, obj=None, **kwargs):
        super(SimWindow, self).__init__(*args)
        self.setupUi(self)

        self.channels = kwargs.get(c.CHANNELS, None)
        self.parameters = kwargs.get(c.PARAMETERS, None)
        self.generators = kwargs.get('generators', None)
        self.simulation_filepath = f'{c.SIMULATIONS_PATH}Simulation-{datetime.now().strftime(c.DATE_FORMAT)}.csv'
        self.speed = 1

        # Conexión de las señales de los botones
        self.btn_start.clicked.connect(self.__start)
        self.btn_play.clicked.connect(self.__resume)
        self.btn_pause.clicked.connect(self.__pause)
        self.btn_stop.clicked.connect(self.__stop)
        self.btn_increase_speed.clicked.connect(self.increase_speed)
        self.btn_decrease_speed.clicked.connect(self.decrease_speed)
        self.btn_max_speed.clicked.connect(self.__max_speed)
        self.btn_reset_speed.clicked.connect(self.__default_speed)
        self.btn_save_chart.clicked.connect(self.save_chart)
        self.btn_open_csvfile.clicked.connect(self.show_outfile)

        self.__prepare_simulation()

    def closeEvent(self, event):
        """
            Sobre-escritura del método closeEvent para el cierre de la ventana.
        """
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

    def __plots_init(self):
        """Construye e inicializa los gráficos de la simulación."""
        index = 0
        for channel in self.channels.values():
            if channel["distribution"].get('name') == c.BERNOULLI:
                chart = LineChart(title="Canal {}".format(channel.get("id")))
                self.series.append(
                    chart.dynamic_line()
                )
                self.chartviews[index].setChart(chart)
            else:
                chart = SplineChart(title="Canal {}".format(channel.get("id")))
                self.series.append(
                    chart.dynamic_spline()
                )
                self.chartviews[index].setChart(chart)
            index += 1

        self.percent_chart = BarChart(
            title="%  Ocupación de los canales",
            parameters=self.channels.copy()
        )
        self.series.append(self.percent_chart.plot_bar_chart())
        self.chartviews[9].setChart(self.percent_chart)

    def __prepare_simulation(self):
        """Prepara el escenario de simulación"""
        self.__simulation_btn_mannager(True, False, False, False)
        self.__speed_btn_mannager(False, False, False, False)
        self.series = list()
        self.__plots_init()

    def save_chart(self):
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            c.SAVE_CHART,
            'bars',
            "JPG (*.jpg);;PNG (*.png)",
            options=QtWidgets.QFileDialog.Options()
        )

        if filepath:
            outfile = QPixmap(self.chart_bars_view.grab())
            outfile.save(filepath, quality=100)
            if outfile:
                QtWidgets.QMessageBox.information(
                    self,
                    c.SAVE_CHART,
                    c.SAVE_CHART_MSG,
                    QtWidgets.QMessageBox.Ok
                )
            else:
                QtWidgets.QMessageBox.critical(
                    self,
                    c.SAVE_CHART,
                    c.CHART_SAVE_ERROR,
                    QtWidgets.QMessageBox.Ok
                )

    def show_outfile(self):
        self.__file_thread = FileThread(
            name=f'File-{self.simulation_filepath}',
            kwargs={
                'filepath': self.simulation_filepath
            }
        )
        self.__file_thread.setDaemon(True)
        self.__file_thread.start()

    def __start(self):
        self.__thread = SimulationThread(
            name=f'Simulation-{uuid4()}',
            target=self.speed_value,
            kwargs={
                'callback': self.__finish_sim,
                'channels': self.channels.copy(),
                'filepath': self.simulation_filepath,
                'generators': self.generators.copy(),
                'parameters': self.parameters.copy(),
                'series': self.series.copy()
            }
        )
        self.__thread.setDaemon(True)
        self.__thread.start()
        self.__simulation_btn_mannager(False, False, True, True)
        self.__speed_btn_mannager(True, True, True, True)
        self.btn_start.setText("REINICIAR")

    def __resume(self):
        self.__thread.resume()
        self.__simulation_btn_mannager(False, False, True, True)

    def __pause(self):
        self.__thread.pause()
        self.__simulation_btn_mannager(False, True, False, True)

    def __stop(self):
        if self.__thread.is_alive:
            if self.__thread.paused:
                self.__thread.resume()
                self.__thread.stop()
            else:
                self.__thread.stop()
            self.__speed_btn_mannager(False, False, False, False)
            self.__simulation_btn_mannager(True, False, False, False)
        self.__prepare_simulation()

    def speed_value(self):
        return self.speed

    def increase_speed(self):
        self.speed *= 2
        self.__speed_btn_mannager(True, True, True, True)
        if self.speed < 1:
            self.label_speed.setText("X{}".format(self.speed))
        else:
            self.label_speed.setText("X{}".format(int(self.speed)))
        if self.speed == c.MAX_SPEED:
            self.__speed_btn_mannager(False, True, False, True)

    def decrease_speed(self):
        self.speed /= 2
        self.__speed_btn_mannager(True, True, True, True)
        if self.speed < 1:
            self.label_speed.setText("X{}".format(self.speed))
        else:
            self.label_speed.setText("X{}".format(int(self.speed)))
        if self.speed == c.MIN_SPEED:
            self.__speed_btn_mannager(True, False, True, True)

    def __default_speed(self):
        self.speed = 1
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.__speed_btn_mannager(True, True, True, True)

    def __max_speed(self):
        self.speed = c.MAX_SPEED
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.__speed_btn_mannager(False, True, False, True)

    def __simulation_btn_mannager(self, f1, f2, f3, f4):
        self.btn_start.setEnabled(f1)
        self.btn_play.setEnabled(f2)
        self.btn_pause.setEnabled(f3)
        self.btn_stop.setEnabled(f4)

    def __speed_btn_mannager(self, f1, f2, f3, f4):
        self.btn_increase_speed.setEnabled(f1)
        self.btn_decrease_speed.setEnabled(f2)
        self.btn_max_speed.setEnabled(f3)
        self.btn_reset_speed.setEnabled(f4)

    def __finish_sim(self, interrupted):
        self.__simulation_btn_mannager(True, False, False, False)
        self.__speed_btn_mannager(False, False, False, False)
        self.speed = 1
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.btn_open_csvfile.setEnabled(interrupted)
        self.btn_save_chart.setEnabled(interrupted)
