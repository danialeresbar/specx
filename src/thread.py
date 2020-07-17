import threading
# from datetime import datetime, timedelta
# import time


class GeneratorThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.data = kwargs.copy()
        self.settings = self.data.get("parameters")
        self.wait = target
        self.name = name
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Indicador de hilo pausado
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Indicador de hilo detenido

    def run(self):
        '''Generación de VA y actualización de gráficas'''
        # limit = self.settings.get("sampling")*30
        # threshold = self.settings.get("threshold")
        channels = [channel for channel in self.data.values()]
        # for k, v in self.data.items():
        #     print("{} --> {}".format(k, v))

        for channel in channels:
            print(channel)
            with self.stop_cond:
                if self.stopped:
                    break

                # Generar VA

                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()

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
