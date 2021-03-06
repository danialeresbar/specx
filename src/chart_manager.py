import constants as c
import math as mt
import numpy as np
from PyQt5.QtChart import (
    QChart,
    QBarCategoryAxis,
    QBarSeries,
    QBarSet,
    QAbstractBarSeries,
    QLegend,
    QLineSeries,
    QSplineSeries
)
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QColor, QColorConstants, QFont
import scipy.stats as stats


FONT_LABEL = QFont()
FONT_TITLE = QFont()


class PDFChart(QChart):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get("title", "Título del gráfico")
        self.parameters = kwargs.get("parameters", None)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setBackgroundRoundness(0)
        self.setTitle(self.title)
        self.setMargins(QMargins(20, 20, 20, 20))
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setTheme(self.ChartThemeLight)

    def plot_bernoulli(self):
        legends = ["Probabilidad de\néxito", "Probabilidad de\nfallo"]
        x = ["Éxito", "Fallo"]
        bars = [self.parameters.get("success"), self.parameters.get("fail")]
        bar_colors = [
            QColorConstants.Svg.lightgreen,
            QColorConstants.Svg.indianred
        ]
        self.add_bars(x=x, bars=bars, bar_colors=bar_colors, bar_label_format="@value", y_label_format="", y_max=1, y_tickcount=6, legends=legends, legend_alignment=Qt.AlignBottom)

    def plot_beta(self):
        alpha = self.parameters.get("alpha")
        beta = self.parameters.get("beta")
        a = self.parameters.get("a")
        b = self.parameters.get("b")

        x = np.linspace(
            stats.beta.ppf(0.01, alpha, beta, loc=a, scale=b),
            stats.beta.ppf(0.99, alpha, beta, loc=a, scale=b),
            100
        )
        y = stats.beta.pdf(x, alpha, beta, loc=a, scale=b)

        serie = QSplineSeries()
        serie.setName(
            f'{c.ALPHA_LETTER}={alpha:.4f}, {c.BETA_LETTER}={beta:.4f}, \
                a={a:.4f}, b={b:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_gamma(self):
        alpha = self.parameters.get("alpha")
        lmbda = self.parameters.get("lmbda")
        gamma = self.parameters.get("gamma")
        x = np.linspace(
            stats.gamma.ppf(0.01, alpha, loc=gamma, scale=lmbda),
            stats.gamma.ppf(0.99, alpha, loc=gamma, scale=lmbda),
            100
        )
        y = stats.gamma.pdf(x, alpha, loc=gamma, scale=lmbda)

        serie = QSplineSeries()
        c.GAMMA_LETTER
        serie.setName(
            f'{c.ALPHA_LETTER}={alpha:.4f}, {c.LAMBDA_LETTER}={lmbda:.4f}, \
                {c.GAMMA_LETTER}={gamma:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_gumbel(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        x = np.linspace(
            stats.gumbel_r.ppf(0.01, loc=mu, scale=sigma),
            stats.gumbel_r.ppf(0.99, loc=mu, scale=sigma),
            100
        )
        y = stats.gumbel_r.pdf(x, loc=mu, scale=sigma)

        serie = QSplineSeries()
        serie.setName(
            f'{c.MU_LETTER}={mu:.4f}, {c.SIGMA_LETTER}={sigma:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_laplace(self):
        mu = self.parameters.get("mu")
        b = self.parameters.get("b")
        x = np.linspace(
            stats.laplace.ppf(0.01, loc=mu, scale=b),
            stats.laplace.ppf(0.99, loc=mu, scale=b),
            100
        )
        y = stats.laplace.pdf(x, loc=mu, scale=b)

        serie = QSplineSeries()
        serie.setName(
            f'{c.MU_LETTER}={mu:.4f}, b={b:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_lognorm(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        gamma = self.parameters.get("gamma")
        x = np.linspace(
            stats.lognorm.ppf(0.01, sigma, loc=gamma, scale=mt.exp(mu)),
            stats.lognorm.ppf(0.99, sigma, loc=gamma, scale=mt.exp(mu)),
            100
        )
        y = stats.lognorm.pdf(x, sigma, loc=gamma, scale=mt.exp(mu))

        serie = QSplineSeries()
        serie.setName(
            f'{c.MU_LETTER}={mu:.4f}, {c.SIGMA_LETTER}={sigma:.4f}, \
                {c.GAMMA_LETTER}={gamma:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_norm(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        x = np.linspace(
            stats.norm.ppf(0.01, loc=mu, scale=sigma),
            stats.norm.ppf(0.99, loc=mu, scale=sigma),
            100
        )
        y = stats.norm.pdf(x, loc=mu, scale=sigma)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName(f'{c.MU_LETTER}={mu:.4f}, {c.SIGMA_LETTER}={sigma:.4f}')
        self.add_spline_series(serie, x, y)

    def plot_rayleigh(self):
        sigma = self.parameters.get("sigma")
        lmbda = self.parameters.get("lmbda")
        x = np.linspace(
            stats.rayleigh.ppf(0.01, loc=lmbda, scale=sigma),
            stats.rayleigh.ppf(0.99, loc=lmbda, scale=sigma),
            100
        )
        y = stats.rayleigh.pdf(x, loc=lmbda, scale=sigma)

        serie = QSplineSeries()
        serie.setName(
            f'{c.SIGMA_LETTER}={sigma:.4f}, {c.LAMBDA_LETTER}={lmbda:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def plot_uniform(self):
        a = self.parameters.get("inf")
        b = self.parameters.get("sup")
        x = np.linspace(
            stats.uniform.ppf(0.01, loc=a, scale=b-a),
            stats.uniform.ppf(0.99, loc=a, scale=b-a),
            100
        )
        y = stats.uniform.pdf(x, loc=a, scale=b-a)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName(f'a={a:.4f}, b={b:.4f}')
        self.add_spline_series(serie, x, y)

    def plot_weibull(self):
        alpha = self.parameters.get("alpha")
        beta = self.parameters.get("beta")
        gamma = self.parameters.get("gamma")
        x = np.linspace(
            stats.weibull_min.ppf(0.01, alpha, loc=gamma, scale=beta),
            stats.weibull_min.ppf(0.99, alpha, loc=gamma, scale=beta),
            100
        )
        y = stats.weibull_min.pdf(x, alpha, loc=gamma, scale=beta)

        serie = QSplineSeries()
        serie.setName(
            f'{c.ALPHA_LETTER}={alpha:.4f}, {c.BETA_LETTER}={beta:.4f}, \
                {c.GAMMA_LETTER}={gamma:.4f}'
        )
        self.add_spline_series(serie, x, y)

    def add_spline_series(self, serie, x, y):
        global FONT_LABEL, FONT_TITLE
        FONT_TITLE.setPointSizeF(12)
        FONT_LABEL.setPointSizeF(8)
        for index in range(len(y)):
            serie.append(x[index], y[index])

        pen = serie.pen()
        pen.setColor(QColor("#5f85db"))
        pen.setWidth(3)
        serie.setPen(pen)
        self.addSeries(serie)
        self.createDefaultAxes()
        self.axes(Qt.Vertical, serie)[0].setRange(0, max(y)+0.1)
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.legend().setAlignment(Qt.AlignTop)
        self.setTitleFont(FONT_TITLE)

    def add_bars(self, x, bars, bar_colors, bar_label_format, y_label_format, y_max, y_tickcount, legends, legend_alignment):
        global FONT_LABEL, FONT_TITLE
        FONT_TITLE.setPointSizeF(12)
        FONT_TITLE.setWeight(QFont.Bold)
        FONT_LABEL.setPointSizeF(8)
        for index in range(len(bars)):
            series = QBarSeries()

            bar_set = QBarSet(legends[index])
            if bar_colors:
                bar_set.setColor(bar_colors[index])

            bar_set.setLabelColor(Qt.black)
            bar_set.setLabelFont(FONT_LABEL)
            bar_set.append(bars[index])

            series.append(bar_set)
            series.setLabelsVisible(True)
            series.setLabelsFormat(bar_label_format)
            if bars[index] < y_max*0.2:
                series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

            else:
                series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            self.addSeries(series)

        self.createDefaultAxes()
        axis_x = self.axes(Qt.Horizontal)[0]
        self.removeAxis(axis_x)
        axis_x = QBarCategoryAxis()
        axis_x.append(x)
        self.addAxis(axis_x, Qt.AlignBottom)
        axis_x.setLabelsFont(FONT_LABEL)
        axis_y = self.axes(Qt.Vertical, series)[0]
        axis_y.setRange(0, y_max)
        axis_y.setTickCount(y_tickcount)
        axis_y.setLabelFormat(y_label_format)
        axis_y.setLabelsFont(FONT_LABEL)
        self.legend().setAlignment(legend_alignment)
        self.legend().setVisible(False)
        self.setTitleFont(FONT_TITLE)


class SplineChart(QChart):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get("title", "Título del gráfico")
        self.parameters = kwargs.get("parameters", None)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setBackgroundRoundness(0)
        self.setTitle(self.title)
        self.setMargins(QMargins(10, 10, 10, 10))
        self.setAnimationOptions(QChart.NoAnimation)
        self.setTheme(self.ChartThemeLight)

    def dynamic_spline(self):
        global FONT_LABEL, FONT_TITLE
        FONT_TITLE.setPointSizeF(10)
        FONT_LABEL.setPointSizeF(8)
        serie = QSplineSeries()
        pen = serie.pen()
        pen.setColor(QColor("#5f85db"))
        pen.setWidth(3)
        serie.setPen(pen)
        serie.setPointsVisible(True)
        self.addSeries(serie)
        self.createDefaultAxes()
        self.axes(Qt.Vertical, serie)[0].setRange(0, 0.8)
        self.axes(Qt.Vertical, serie)[0].setTickCount(3)
        self.axes(Qt.Horizontal, serie)[0].setRange(0, 10)
        self.axes(Qt.Horizontal, serie)[0].setTickCount(5)
        self.legend().setVisible(False)
        self.setTitleFont(FONT_TITLE)
        return serie


class LineChart(QChart):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get("title", "Título del gráfico")
        self.parameters = kwargs.get("parameters", None)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.legend().setVisible(False)
        self.setBackgroundRoundness(0)
        self.setTitle(self.title)
        self.setMargins(QMargins(10, 10, 10, 10))
        self.setAnimationOptions(QChart.NoAnimation)
        self.setTheme(self.ChartThemeLight)

    def dynamic_line(self):
        global FONT_LABEL, FONT_TITLE
        FONT_TITLE.setPointSizeF(10)
        FONT_LABEL.setPointSizeF(8)
        serie = QLineSeries()
        pen = serie.pen()
        pen.setColor(QColor("#5f85db"))
        pen.setWidth(3)
        serie.setPen(pen)
        serie.setPointsVisible(True)
        self.addSeries(serie)
        self.createDefaultAxes()
        self.axes(Qt.Vertical, serie)[0].setRange(0, 1)
        self.axes(Qt.Vertical, serie)[0].setTickCount(3)
        self.axes(Qt.Horizontal, serie)[0].setRange(0, 10)
        self.axes(Qt.Horizontal, serie)[0].setTickCount(5)
        # self.axes(Qt.Horizontal, serie)[0].setLabelsVisible(False)
        self.setTitleFont(FONT_TITLE)
        return serie


class BarChart(QChart):
    def __init__(self, **kwargs):
        super().__init__()
        self.title = kwargs.get("title", "Título del gráfico")
        self.parameters = kwargs.get("parameters", None)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setBackgroundRoundness(0)
        self.setTitle(self.title)
        self.setMargins(QMargins(10, 10, 10, 10))
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setTheme(self.ChartThemeLight)

    def plot_bar_chart(self):
        # Etiquetas para eje x
        x = list()
        for k, v in self.parameters.items():
            x.append(v.get("frequency"))

        # bars = [value for value in range(10, 100, 10)]
        bars = [0]*9
        series = self.add_bars(x=x, bars=bars, bar_colors=None, bar_label_format="@value %", y_max=100, y_tickcount=5, legends=x, legend_alignment=Qt.AlignBottom)
        return series

    def add_bars(self, x, bars, bar_colors, bar_label_format, y_max, y_tickcount, legends, legend_alignment):
        global FONT_LABEL, FONT_TITLE
        FONT_TITLE.setPointSizeF(12)
        FONT_TITLE.setWeight(QFont.Bold)
        FONT_LABEL.setPointSizeF(8)
        for index in range(len(bars)):
            series = QBarSeries()
            bar_set = QBarSet(legends[index])
            if bar_colors:
                bar_set.setColor(bar_colors[index])
            bar_set.setLabelColor(Qt.black)
            bar_set.setLabelFont(FONT_LABEL)
            bar_set.append(bars[index])
            series.append(bar_set)
            series.setLabelsVisible(True)
            series.setLabelsFormat(bar_label_format)
            if bars[index] < y_max*0.2:
                series.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)
            else:
                series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            self.addSeries(series)

        self.createDefaultAxes()
        axis_x = self.axes(Qt.Horizontal)[0]
        self.removeAxis(axis_x)
        axis_x = QBarCategoryAxis()
        axis_x.append(x)
        self.addAxis(axis_x, Qt.AlignBottom)
        axis_x.setLabelsFont(FONT_LABEL)
        axis_y = self.axes(Qt.Vertical, series)[0]
        axis_y.setRange(0, y_max)
        axis_y.setTickCount(y_tickcount)
        axis_y.setLabelsFont(FONT_LABEL)
        axis_y.setTitleText("Porcentaje de ocupación")
        self.legend().setAlignment(legend_alignment)
        self.legend().setVisible(False)
        self.setTitleFont(FONT_TITLE)
        return self.series()
