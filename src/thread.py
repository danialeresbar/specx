import constants as c
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
import threading
import time


class SimulationThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.channels = [
            channel for channel in kwargs.get(c.CHANNELS).values()
        ]
        self.series = [serie for serie in kwargs.get(c.SERIES)]
        self.parameters = kwargs.get(c.PARAMETERS)
        self.generators = kwargs.get("generators")
        self.wait = target
        self.callback_exit = kwargs.get("callback")
        self.filepath = kwargs.get("filepath")

        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Indicador de hilo pausado
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Indicador de hilo detenido
        self.finish_flag = True

    def run(self):
        """Generación de Variables aleatorias y actualización de gráficas"""
        bars = self.series[-1]
        delta = datetime.now()
        index = 0
        limit = self.parameters.get(c.SAMPLING)*30

        for channel in self.channels:
            generator = self.generators[index]
            serie = self.series[index]
            usage_percent = 0
            var_count = 0

            while(var_count < limit and not self.stopped):
                var = generator(channel['distribution'].get(c.PARAMETERS))
                var_count += 1
                self.__update_chart(serie, var_count*2, var)
                self.__update_outfile(
                    delta,
                    channel.get('frequency'),
                    channel['distribution'].get('name'),
                    var
                )
                time.sleep(2/self.wait())  # Delta entre la generación de VAs
                delta += timedelta(seconds=2)
                if var >= self.parameters.get(c.THRESHOLD):
                    usage_percent += 1
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()
            with self.stop_cond:
                if self.stopped:
                    self.finish_flag = False
                    break
            self.__update_bars(bars[index], (usage_percent/var_count)*100)
            index += 1

        self.callback_exit(self.finish_flag)

    def pause(self):
        '''Pausa la ejecución del hilo estableciendo el estado del lock de
        la condición pausado en cerrado (locked)'''
        self.paused = True
        self.pause_cond.acquire()  # Adquiere el lock

    def resume(self):
        '''Reanuda la ejecución del hilo estableciendo el estado del lock de
        la condición pausado en abierto (unlocked)'''
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()  # Libera el lock

    def stop(self):
        '''Detiene la ejecución del hilo estableciendo el estado del lock de
        la condición detenido en cerrado (locked)'''
        self.stopped = True
        self.stop_cond.acquire  # Establece el indicador interno a True

    def __update_chart(self, serie, x, y):
        serie.append(x, y)
        if x >= 12:
            dx = serie.chart().plotArea().width() / \
                serie.chart().axes(Qt.Horizontal, serie)[0].tickCount()
            serie.chart().scroll(dx, 0)

    def __update_bars(self, bar, usage_percent):
        bar.barSets()[0].replace(0, usage_percent)
        if usage_percent > 20:
            bar.setLabelsPosition(0)

    def __update_outfile(self, delta, frequency, distribution, var):
        line = "{};{};{};{}".format(
            delta.strftime("%m-%d-%Y-%H:%M:%S"),
            frequency,
            distribution,
            var
        )
        with open(self.filepath, 'a') as outfile:
            outfile.write(line + '\n')


class FileThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.filepath = kwargs.get('filepath')

    def run(self):
        """Abre una instancia de un archivo"""
        import os
        import subprocess
        path = f'{os.getcwd()}{os.path.sep}{self.filepath}'
        try:
            subprocess.call(path, shell=True)
        except Exception:
            print(c.FILE_OPEN_ERROR)
