from PyQt5 import QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarCategoryAxis, QBarSeries, QBarSet, QValueAxis, QAbstractBarSeries, QLegend, QSplineSeries, QPercentBarSeries
from PyQt5.QtGui import QFont, QIcon, QPainter, QPixmap, QColor, QColorConstants
from PyQt5.QtCore import Qt, QMargins
import numpy as np
import scipy.stats as stats


class ChartDesign(QChart):
    def __init__(self, **kwargs):
        super().__init__()

        self.title = kwargs.get("title", "Nuevo gráfico")
        self.parameters = kwargs.get("parameters", None)
        self.font = QFont()
        self.font.setPointSize(kwargs.get("font_size", 10))
        #self.chart_view = QChartView()

        # Pruebas
        #self.new_action = QtWidgets.QAction(self)
        #self.new_action.setText("Zoom")
        #self.addAction(self.new_action)

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.setBackgroundRoundness(0)
        self.setTitle(self.title)
        self.setMargins(QMargins(15, 15, 15, 15))
        self.setAnimationOptions(QChart.SeriesAnimations)
        self.setTheme(self.ChartThemeDark)
        self.setDropShadowEnabled(True)
        self.setBackgroundBrush(QColor("#353941"))

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.zoomIn()
        else:
            self.zoomOut()
        #self.scroll(event.delta()/40, event.delta()/40)
        event.accept()

    def plot_bar_chart(self):
        # Etiquetas para eje x
        x = list()

        for k, v in self.parameters.items():
            x.append(v.get("freq"))
        
        # Valores de prueba eje Y
        bars = [30]*9

        self.add_bars(x=x, bars=bars, bar_colors=None, bar_label_format="@value %", y_label_format="%.2f %",y_max=100, y_tickcount=4, legends=x, legend_alignment=Qt.AlignRight )

    def plot_bernoulli(self):
        p = self.parameters.get("success")
        q = self.parameters.get("fail")

        # Etiquetas para eje x
        legends = ["Probabilidad de\néxito", "Probabilidad de\nfallo"]
        x = ["Éxito", "Fallo"]
        bars = [self.parameters.get("success"), self.parameters.get("fail")]
        bar_colors = [QColorConstants.Svg.lightgreen, QColorConstants.Svg.indianred]

        self.add_bars(x=x, bars=bars, bar_colors=bar_colors, bar_label_format="@value", y_label_format="", y_max=1, y_tickcount=5, legends=legends, legend_alignment=Qt.AlignTop)

    def plot_beta(self):
        alpha = self.parameters.get("alpha")
        beta = self.parameters.get("beta")
        a = self.parameters.get("a")
        b = self.parameters.get("b")
        
        x = np.linspace(stats.beta.ppf(0.01, alpha, beta, loc=a, scale=b), stats.beta.ppf(0.99, alpha, beta, loc=a, scale=b), 100)
        y = stats.beta.pdf(x, alpha, beta, loc=a, scale=b)

        serie = QSplineSeries()
        serie.setName("α={:.4f}, β={:.4f}, a={:.4f}, b={:.4f},".format(alpha, beta, a, b))
        self.add_spline_series(serie, x, y)

    def plot_gamma(self):
        alpha = self.parameters.get("alpha")
        lmbda = self.parameters.get("lmbda")
        gamma = self.parameters.get("gamma")
        x = np.linspace(stats.gamma.ppf(0.01, alpha, loc=gamma, scale=lmbda), stats.gamma.ppf(0.99, alpha, loc=gamma, scale=lmbda), 100)
        y = stats.gamma.pdf(x, alpha, loc=gamma, scale=lmbda)

        serie = QSplineSeries()
        serie.setName("α={:.4f}, λ={:.4f}, γ={:.4f}".format(alpha, lmbda, gamma))
        self.add_spline_series(serie, x, y)
        
    def plot_gumbel(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        x = np.linspace(stats.gumbel_r.ppf(0.01, loc=mu, scale=sigma), stats.gumbel_r.ppf(0.99, loc=mu, scale=sigma), 100)
        y = stats.gumbel_r.pdf(x, loc=mu, scale=sigma)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("μ={:.4f}, σ={:.4f}".format(mu, sigma))
        self.add_spline_series(serie, x, y)

    def plot_laplace(self):
        mu = self.parameters.get("mu")
        b = self.parameters.get("b")
        x = np.linspace(stats.laplace.ppf(0.01, loc=mu, scale=b), stats.laplace.ppf(0.99, loc=mu, scale=b), 100)
        y = stats.laplace.pdf(x, loc=mu, scale=b)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("μ={:.4f}, Δ={:.4f}".format(mu, b))
        self.add_spline_series(serie, x, y)

    def plot_lognorm(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        gamma = self.parameters.get("gamma")
        x = np.linspace(stats.lognorm.ppf(0.01, sigma, loc=mu, scale=gamma), stats.lognorm.ppf(0.99, sigma, loc=mu, scale=gamma), 100)
        y = stats.lognorm.pdf(x, sigma, loc=mu, scale=gamma)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("μ={:.4f}, σ²={:.4f}, γ={:.4f}".format(mu, sigma, gamma))
        self.add_spline_series(serie, x, y)

    def plot_norm(self):
        mu = self.parameters.get("mu")
        sigma = self.parameters.get("sigma")
        x = np.linspace(stats.norm.ppf(0.01, loc=mu, scale=sigma), stats.norm.ppf(0.99, loc=mu, scale=sigma), 100)
        y = stats.norm.pdf(x, loc=mu, scale=sigma)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("μ={:.4f}, σ={:.4f}".format(mu, sigma))
        self.add_spline_series(serie, x, y)

    def plot_rayleigh(self):
        sigma = self.parameters.get("sigma")
        lmbda = self.parameters.get("lmbda")
        x = np.linspace(stats.rayleigh.ppf(0.01, loc=lmbda, scale=sigma), stats.rayleigh.ppf(0.99, loc=lmbda, scale=sigma), 100)
        y = stats.rayleigh.pdf(x, loc=lmbda, scale=sigma)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("σ={:.4f}, λ={:.4f}".format(sigma, lmbda))
        self.add_spline_series(serie, x, y)

    def plot_uniform(self):
        a = self.parameters.get("inf")
        b = self.parameters.get("sup")
        x = np.linspace(stats.uniform.ppf(0.01, loc=a, scale=b-a), stats.uniform.ppf(0.99, loc=a, scale=b-a), 100)
        y = stats.uniform.pdf(x, loc=a, scale=b-a)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("a={:.4f}, b={:.4f}".format(a, b))
        self.add_spline_series(serie, x, y)

    def plot_weibull(self):
        gamma = self.parameters.get("gamma")
        alpha = self.parameters.get("alpha")
        mu = self.parameters.get("mu")
        x = np.linspace(stats.weibull_min.ppf(0.01, gamma, loc=mu, scale=alpha), stats.weibull_min.ppf(0.99, gamma, loc=mu, scale=alpha), 100)
        y = stats.weibull_min.pdf(x, gamma, loc=mu, scale=alpha)

        # Serie con los valores (x,y)
        serie = QSplineSeries()
        serie.setName("γ={:.4f}, α={:.4f}, μ={:.4f}".format(gamma, alpha, mu))
        self.add_spline_series(serie, x, y)

    def dynamic_spline(self):
        pass
        
    def add_spline_series(self, serie, x, y):
        for index in range(len(y)):
            serie.append(x[index], y[index])

        pen = serie.pen()
        pen.setColor(QColor("#5f85db"))
        pen.setWidth(3)
        serie.setPen(pen)
        self.addSeries(serie)
        self.createDefaultAxes()
        self.axes(Qt.Vertical, serie)[0].setRange(0, max(y)+0.05)
        self.legend().setFont(self.font)
        self.legend().setVisible(True)
        self.legend().setMarkerShape(QLegend.MarkerShapeFromSeries)
        self.setTitleFont(self.font)

    def add_bars(self, x, bars, bar_colors, bar_label_format, y_label_format, y_max, y_tickcount, legends, legend_alignment):
        for index in range(len(bars)):
            series = QBarSeries()

            bar_set = QBarSet(legends[index])
            if bar_colors:
                bar_set.setColor(bar_colors[index])

            bar_set.setLabelColor(Qt.black)
            bar_set.setLabelFont(self.font)
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
        axis_x.setLabelsFont(self.font)
        axis_y = self.axes(Qt.Vertical, series)[0]
        axis_y.setRange(0, y_max)
        axis_y.setTickCount(y_tickcount)
        axis_y.setLabelFormat(y_label_format)
        axis_y.setLabelsFont(self.font)

        self.legend().setFont(self.font)
        #self.legend().setVisible(True)
        self.legend().setAlignment(legend_alignment)
        self.setTitleFont(self.font) 

    def save_chart(self, chart_view):
        name, ext = QtWidgets.QFileDialog.getSaveFileName(
            self, "Guardar como",
            "chart",
            "JPG (*.jpg);;PNG (*.png)",
            options=QtWidgets.QFileDialog.Options()
            )
                
        if name:
            file = QPixmap(chart_view.grab())
            file.save(name, quality = 100)

            if file:
                QtWidgets.QMessageBox.information(self, "Guardar gráfico", "Gráfico guardado con éxito.",
                                        QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.critical(self, "Guardar gráfico", "Error al guardar el gráfico.", QtWidgets.QMessageBox.Ok)
