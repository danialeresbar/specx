# from decimal import Decimal
import generators as gen


# ---- Distribución de Bernoulli ----
BERNOULLI = 'Bernoulli'
SUCCESS_PROB_LABEL = 'Probabilidad\nde exito:'
SUCCESS_PROB = 0.5

# ---- Distribución Beta ----
BETA = 'Beta'
BETA_SHAPE_1_LABEL = 'Parámetro de\nforma alpha:'
BETA_SHAPE_1 = 14.087
BETA_SHAPE_2_LABEL = 'Parámetro de\nforma beta:'
BETA_SHAPE_2 = 4.9149
BETA_LOC = 0.05
BETA_SCALE = 0.75

# ---- Distribución Gamma ----
GAMMA = 'Gamma'
GAMMA_SHAPE = 7.0259
GAMMA_LOC = 0
GAMMA_SCALE = 0.02008

# ---- Distribución de Gumbel ----
GUMBEL = 'Gumbel max'
GUMBEL_LOC = 0.59583
GUMBEL_SCALE = 0.04929

# ---- Distribución de Laplace ----
LAPLACE = 'Laplace'
LAPLACE_LOC = 0.56898
LAPLACE_SCALE = 0.11365703

# ---- Distribución Lognormal ----
LOGNORM = 'Lognormal'
LOGNORM_SHAPE = 0.01758
LOGNORM_LOC = 1.86636
LOGNORM_SCALE = -5.8362

# ---- Distribución Normal ----
NORM = 'Normal'
NORM_LOC = 0.60998
NORM_SCALE = 0.06172

# ---- Distribución de Rayleigh ----
RAYLEIGH = 'Rayleigh'
RAYLEIGH_LOC = 0.05
RAYLEIGH_SCALE = 0.1003

# ---- Distribución Uniforme ----
UNIFORM = 'Uniforme'
UNIFORM_INF_LABEL = 'Parámetro de\ncota inferior:'
UNIFORM_INF = 0.27671
UNIFORM_SUP_LABEL = 'Parámetro de\ncota superior:'
UNIFORM_SUP = 0.61845

# ---- Distribución de Weibull ----
WEIBULL = 'Weibull'
WEIBULL_SHAPE = 7.1476
WEIBULL_LOC = -0.01445
WEIBULL_SCALE = 0.58176


# ---- Distribuciones ----
FIRST_PARAMETER = 'Parámetro 1:'
SECOND_PARAMETER = 'Parámetro 2:'
THIRD_PARAMETER = 'Parámetro 3:'
FOURTH_PARAMETER = 'Parámetro 4:'
ONE_PARAMETER = '1P'
TWO_PARAMETERS = '2P'
THREE_PARAMETERS = '3P'


# ---- Errores ----
CHART_SAVE_ERROR = 'No se pudo guardar el gráfico'
FILE_OPEN_ERROR = 'El archivo fue eliminado o no existe!'
JSON_SAVE_ERROR = 'No se pudo guardar el archivo con las configuraciones'
JSON_LOAD_ERROR = 'Archivo de configuración no válido'


# ---- Fechas ----
DATE_FORMAT = "%m-%d-%Y-%H-%M-%S"


# ---- Generadores ----
GENERATORS = {
            BERNOULLI: gen.bernoulli,
            BETA: gen.beta,
            GAMMA: gen.gamma,
            GUMBEL: gen.gumbel,
            LAPLACE: gen.laplace,
            LOGNORM: gen.lognormal,
            NORM: gen.normal,
            RAYLEIGH: gen.rayleigh,
            UNIFORM: gen.uniform,
            WEIBULL: gen.weibull,
        }


# ---- Gráficos ----
SAVE_CHART = 'Guardar gráfico'
SAVE_CHART_MSG = 'Gráfico guardado con éxito'
SERIES = 'series'


# ---- Interfaz gráfica ----
BOX_DEFAULT_ITEM = 'Selecciona'
EXIT_MESSAGE = '¿Estás seguro que deseas salir?'
FILE_LOADED = 'Archivo de configuración cargado'
FILE_SAVED = 'Archivo de configuración guardado'
LOAD_CONFIG = 'Cargar configuración'
SAVE_CONFIG = 'Guardar configuración'


# ---- Letras griegas ----
ALPHA_LETTER = 'α'
BETA_LETTER = 'β'
GAMMA_LETTER = 'γ'
LAMBDA_LETTER = 'λ'
MU_LETTER = 'μ'
SIGMA_LETTER = 'σ'


# ---- Parámetros ----
LOCATION = 'Parámetro de\nubicación:'
SCALE = 'Parámetro de\nescala:'
SHAPE = 'Parámetro de\nforma:'


# ---- Rutas ----
PROJECT_PATH = '../'
SETTINGS_PATH = f'{PROJECT_PATH}/config'
SIMULATIONS_PATH = f'{PROJECT_PATH}/simulations/'


# ---- Simulación ----
CHARTVIEWS = 10
CHARTVIEWS_DISTRIBUTION = 3
CHANNELS = 'channels'
DEFAULT_SPEED = 1
ENERGY = 'energy'
MAX_SPEED = 64
MIN_SPEED = 1/MAX_SPEED
PARAMETERS = 'parameters'
SAMPLING = 'sampling'
DEFAULT_SAMPLE_TIME = 5
DEFAULT_THRESHOLD = 0.33
THRESHOLD = 'threshold'
USAGE = 'usage'
SETTINGS_BODY = {
    CHANNELS: dict(),
    PARAMETERS: dict()
}


# ---- Variables Aleatorias ----
MIN_VALUE = 0
MAX_VALUE = 0.8
