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

        self.__plot_views = [
            self.chart_test_1,
            self.chart_test_2,
            self.chart_test_3,
            self.chart_test_4,
            self.chart_test_5,
            self.chart_test_6,
            self.chart_test_7,
            self.chart_test_8,
            self.chart_test_9,
        ]

        # Conexión de las señales de los botones
        self.start_button.clicked.connect(self.__start)
        self.play_button.clicked.connect(self.__resume)
        self.pause_button.clicked.connect(self.__pause)
        self.stop_button.clicked.connect(self.__stop)
        self.increase_time_speed_button.clicked.connect(self.increase_speed)
        self.decrease_time_speed_button.clicked.connect(self.decrease_speed)
        self.max_time_speed_button.clicked.connect(self.__max_speed)
        self.defaultt_time_speed_button.clicked.connect(self.__default_speed)
        self.save_chart_button.clicked.connect(self.save_chart)
        self.show_file_button.clicked.connect(self.show_outfile)

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
        for key, value in self.channels.items():
            if value["distribution"].get('name') == c.BERNOULLI:
                chart = LineChart(title="Canal {}".format(value.get("id")))
                self.series.append(
                    chart.dynamic_line()
                )
                self.__plot_views[index].setChart(chart)
            else:
                chart = SplineChart(title="Canal {}".format(value.get("id")))
                self.series.append(
                    chart.dynamic_spline()
                )
                self.__plot_views[index].setChart(chart)
            index += 1

        self.bars_usage = BarChart(
            title="%  Ocupación de los canales",
            parameters=self.channels.copy()
        )
        self.series.append(self.bars_usage.plot_bar_chart())
        self.chart_bars_view.setChart(self.bars_usage)

    def __prepare_simulation(self):
        """Prepara el escenario de simulación"""
        self.__sim_button_mannager(True, False, False, False)
        self.__speed_button_mannager(False, False, False, False)
        self.series = list()
        self.__plots_init()

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
        self.__sim_button_mannager(False, False, True, True)
        self.__speed_button_mannager(True, True, True, True)
        self.start_button.setText("REINICIAR")

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
            self.__speed_button_mannager(False, False, False, False)
            self.__sim_button_mannager(True, False, False, False)
        self.__prepare_simulation()

    def speed_value(self):
        return self.speed

    def increase_speed(self):
        self.speed *= 2
        self.__speed_button_mannager(True, True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == c.MAX_SPEED:
            self.__speed_button_mannager(False, True, False, True)

    def decrease_speed(self):
        self.speed /= 2
        self.__speed_button_mannager(True, True, True, True)
        if self.speed < 1:
            self.time_speed_label.setText("X{}".format(self.speed))
        else:
            self.time_speed_label.setText("X{}".format(int(self.speed)))
        if self.speed == c.MIN_SPEED:
            self.__speed_button_mannager(True, False, True, True)

    def __default_speed(self):
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(True, True, True, True)

    def __max_speed(self):
        self.speed = c.MAX_SPEED
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.__speed_button_mannager(False, True, False, True)

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

    def __finish_sim(self, interrupted):
        self.__sim_button_mannager(True, False, False, False)
        self.__speed_button_mannager(False, False, False, False)
        self.speed = 1
        self.time_speed_label.setText("X{}".format(int(self.speed)))
        self.show_file_button.setEnabled(interrupted)
        self.save_chart_button.setEnabled(interrupted)
