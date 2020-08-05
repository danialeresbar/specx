import threading
# from datetime import datetime, timedelta
import time


class SimulationThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.channels = [channel for channel in kwargs.get("channels").values()]
        self.series = [serie for serie in kwargs.get("series")]
        self.parameters = kwargs.get("parameters")
        self.wait = target
        self.name = name
        self.finish_callback = kwargs.get("callback")
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Indicador de hilo pausado
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Indicador de hilo detenido

    def run(self):
        '''Generación de VA y actualización de gráficas'''
        # limit = self.parameters.get("sampling")*30
        # threshold = self.parameters.get("threshold")
        self.series[0].append(6, 0.69)

        for channel in self.channels:
            with self.stop_cond:
                if self.stopped:
                    break
                # Generar VA
                time.sleep(self.wait())
                # print("Waiting")
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()

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


class FileThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)

    def run(self):
        '''Abre una instancia de un archivo'''
        pass
