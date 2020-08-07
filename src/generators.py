import math as mt
import numpy as np
from scipy import stats
import time


# Tiempo del sistema en segundos (s), usado como
# semilla del primer generador
SEED_1 = time.time()

# Tiempo del sistema en milisegundos (ms) usado como
# semilla del segundo generador
SEED_2 = time.time()*1000


def cong_mixto_posix():
    '''Generador congruencial usado por JAVA y POSIX'''
    global SEED_1
    a = 25214903917
    m = (2**48) - 1
    SEED_1 = (a*SEED_1 + 11) % m
    return SEED_1/m


def cong_mixto_gcc():
    '''Generador congruencial usado por gcc'''
    global SEED_2
    a = 1103515245
    m = (2**31) - 1
    SEED_2 = (a*SEED_2 + 12345) % m
    return SEED_2/m


def __var_checker(var):
    '''Verifica que la variable aleatoria generada esté dentro del rango
    establecido de valores.'''
    if var < 0:
        return 0
        return var if var < 0.75 else 0.75


def bernoulli(args):
    '''Genera una variable aleatoria que sigue una distribución
    de Bernoulli con una probabilidad de éxito p'''
    U = cong_mixto_posix()
    return 1 if U < args[0] else 0


def beta(args):
    '''Genera una variable aleatoria que sigue una distribución
    Beta de acuerdo a los parámetros enviados'''
    r_v = stats.beta.rvs(args[0], args[1], loc=args[2], scale=args[3])
    return __var_checker(r_v)


def gamma(args):
    '''Genera una variable aleatoria que sigue una distribución
    Gamma de acuerdo a los parámetros enviados'''
    r_v = stats.gamma.rvs(args[0], loc=0, scale=args[1])
    return r_v


def gumbel_inverse_transformation(u, B):
    U = cong_mixto_posix()
    X = u-(B*mt.log(-1*mt.log(1-U)))
    return X


def gumbel(args):
    '''Genera una variable aleatoria que sigue una distribución
    Gumbel (extremos) de acuerdo a los parámetros enviados'''
    r_v = np.random.gumbel(loc=args[0], scale=args[1])
    return r_v


def laplace(args):
    '''Genera una variable aleatoria que sigue una distribución
    de Laplace de acuerdo a los parámetros enviados'''
    r_v = stats.laplace.rvs(loc=args[0], scale=args[1])
    return r_v


def lognormal(args):
    '''Genera una variable aleatoria que sigue una distribución
    Lognormal de acuerdo a los parámetros enviados'''
    r_v = stats.lognorm.rvs(args[1], loc=args[2], scale=mt.exp(args[0]))
    return r_v


def normal(args):
    '''Genera una variable aleatoria que sigue una distribución
    Normal de acuerdo a los parámetros enviados'''
    r_v = stats.norm.rvs(loc=args[0], scale=args[1])
    return __var_checker(r_v)


def rayleigh(args):
    '''Genera una variable aleatoria que sigue una distribución
    Rayleigh de acuerdo a los parámetros enviados'''
    r_v = stats.rayleigh.rvs(loc=args[1], scale=args[0])
    return r_v


def uniform(args):
    '''Genera una variable aleatoria que sigue una distribución
    Uniforme continua de acuerdo a los parámetros enviados,
    usando el algoritmo de la transformación inversa'''
    U = cong_mixto_posix()
    X = args[0] + (args[1]-args[0])*U
    return X


def weibull_inverse_transformation(a, b, y):
    '''Genera una variable aleatoria que sigue una distribución
    Weibull continua de acuerdo a los parámetros enviados,
    usando el algoritmo de la transformación inversa'''
    U = cong_mixto_posix()
    X = b*(mt.pow(-1*mt.log(1-U), 1/a)) + y
    return X


def weibull(args):
    '''Genera una variable aleatoria que sigue una distribución
    Weibull de acuerdo a los parámetros enviados'''
    r_v = stats.weibull_min.rvs(c=args[0], loc=args[2], scale=args[1], size=1)
    return r_v
