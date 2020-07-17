import threading
# from datetime import datetime, timedelta
# import time


class GeneratorThread(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(self, target=target, name=name)
        self.data = kwargs.copy()
        self.wait = target
        self.name = name
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Indicador de hilo pausado
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Indicador de hilo detenido

    def run(self):
        '''Generación de VA y actualización de gráficas'''
        limit = self.data["parameters"].get("sampling")*30
        print(
            "Hola estamos en {} Debo generar {} VA".format(
                self.name,
                limit
            )
        )

        for _ in range(limit):
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
