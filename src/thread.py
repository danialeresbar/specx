from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
import threading
import time


class SimulationThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.channels = [
            channel for channel in kwargs.get("channels").values()
        ]
        self.series = [serie for serie in kwargs.get("series")]
        # self.bars = kwargs.get("bars")
        self.parameters = kwargs.get("parameters")
        self.generators = kwargs.get("generators")
        self.wait = target
        self.finish_callback = kwargs.get("callback")
        self.file_content = list()

        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Indicador de hilo pausado
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Indicador de hilo detenido

    def run(self):
        '''Generación de Variables aleatorias y actualización de gráficas'''
        index = 0
        limit = self.parameters.get("sampling")*30
        point = datetime.now()
        bars = self.series[-1]

        for channel in self.channels:
            counter = 0
            random_vars = list()
            generator = self.generators[index]
            serie = self.series[index]

            while(counter < limit and not self.stopped):
                var = generator(channel["distribution"].get("parameters"))
                self.__update_chart(serie, counter*2, var)
                self.__update_file_content(
                    point, channel.get("frequency"),
                    channel["distribution"].get("name"),
                    var
                )
                time.sleep(2/self.wait())
                counter += 1
                point += timedelta(seconds=2)
                random_vars.append(var)
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()

            with self.stop_cond:
                if self.stopped:
                    break

            self.__update_bars(bars[index], random_vars)
            index += 1

        self.finish_callback()
        print("Termina mi ejecución")

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
            dx = serie.chart().plotArea().width() / serie.chart().axes(Qt.Horizontal, serie)[0].tickCount()
            serie.chart().scroll(dx, 0)

    def __update_bars(self, bar, values):
        counter = 0
        for value in values:
            if value > self.parameters.get("threshold"):
                counter += 1
        bar.barSets()[0].replace(0, (counter/len(values))*100)
        if (counter/len(values))*100 < 20:
            bar.setLabelsPosition(3)

    def __update_file_content(self, point, frequency, distribution, var):
        line = point.strftime("%m-%d-%Y-%H:%M:%S") + ';' + frequency + ';' + distribution + ';' + str(var)
        self.file_content.append(line)


class FileThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)

    def run(self):
        '''Abre una instancia de un archivo'''
        pass
