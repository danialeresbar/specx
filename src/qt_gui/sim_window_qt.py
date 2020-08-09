from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


class Ui_sim_window(object):
    def setupUi(self, sim_window):
        sim_window.setObjectName("sim_window")
        sim_window.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sim_window.sizePolicy().hasHeightForWidth())
        sim_window.setSizePolicy(sizePolicy)
        sim_window.setMinimumSize(QtCore.QSize(1280, 720))
        sim_window.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sim_window.setWindowIcon(icon)
        sim_window.setStyleSheet("* {\n"
"    background: #26282b;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator, QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #DDDDDD;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 4px;\n"
"    top: -7px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #191919;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 15px;\n"
"    margin: 0px 0px 0px 32px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 15px;\n"
"    margin: 32px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #353535;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    border-width: 0px 1px 0px 1px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border-width: 1px 0px 1px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background:#353535;\n"
"    border: 1px solid #5A5A5A;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    position: absolute;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: left;\n"
"    left: 15px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    top: 15px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 15px;\n"
"    subcontrol-position: top left;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"}\n"
"\n"
"QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QAbstractButton:disabled {\n"
"	color: #787878;\n"
"}\n"
"\n"
"QAbstractButton:hover {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QAbstractButton:pressed {\n"
"    background: #5A5A5A;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    show-decoration-selected: 1;\n"
"    selection-background-color: #3D7848;\n"
"    selection-color: #DDDDDD;\n"
"    alternate-background-color: #353535;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #191919;\n"
"    border: 1px solid #5A5A5A;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QHeaderView::section:selected, QHeaderView::section::checked {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QTableView {\n"
"    gridline-color: #5A5A5A;\n"
"}\n"
"\n"
"QTabBar {\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-radius: 0px;\n"
"    padding: 4px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"    subcontrol-origin: border;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #353535;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
"    background: #353535;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 1px;\n"
"    background-color: #3D7848;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    background: #353535;\n"
"}")
        self.container = QtWidgets.QWidget(sim_window)
        self.container.setObjectName("container")
        self.main_layout = QtWidgets.QVBoxLayout(self.container)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(5)
        self.main_layout.setObjectName("main_layout")

        self.control_layout = QtWidgets.QHBoxLayout()
        self.control_layout.setSpacing(5)
        self.control_layout.setObjectName("control_layout")

        self.start_button_widget = QtWidgets.QWidget(self.container)
        self.sub_layout_0 = QtWidgets.QHBoxLayout(self.start_button_widget)
        self.sub_layout_0.setSpacing(5)
        self.sub_layout_0.setObjectName("sub_layout_1")
        self.start_button = QtWidgets.QPushButton(self.start_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setText("INICIAR")
        self.start_button.setObjectName("start_button")
        self.sub_layout_0.addWidget(self.start_button)
        self.control_layout.addWidget(self.start_button_widget)
        self.control_layout.setStretch(0, 10)

        self.control_button_widget = QtWidgets.QWidget(self.container)
        self.control_button_widget.setObjectName("control_button_widget")
        self.sub_layout_1 = QtWidgets.QHBoxLayout(self.control_button_widget)
        self.sub_layout_1.setSpacing(5)
        self.sub_layout_1.setObjectName("sub_layout_1")
        self.play_button = QtWidgets.QPushButton(self.control_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QtCore.QSize(16, 16))
        self.play_button.setFlat(True)
        self.play_button.setObjectName("play_button")
        self.sub_layout_1.addWidget(self.play_button)
        self.pause_button = QtWidgets.QPushButton(self.control_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon2)
        self.pause_button.setIconSize(QtCore.QSize(16, 16))
        self.pause_button.setObjectName("pause_button")
        self.sub_layout_1.addWidget(self.pause_button)
        self.stop_button = QtWidgets.QPushButton(self.control_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QtCore.QSize(16, 16))
        self.stop_button.setObjectName("stop_button")
        self.sub_layout_1.addWidget(self.stop_button)
        self.control_layout.addWidget(self.control_button_widget)
        self.time_button_widget = QtWidgets.QWidget(self.container)
        self.time_button_widget.setObjectName("time_button_widget")
        self.sub_layout_2 = QtWidgets.QHBoxLayout(self.time_button_widget)
        self.sub_layout_2.setSpacing(5)
        self.sub_layout_2.setObjectName("sub_layout_2")
        self.defaultt_time_speed_button = QtWidgets.QPushButton(self.time_button_widget)
        self.defaultt_time_speed_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.defaultt_time_speed_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/reset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.defaultt_time_speed_button.setIcon(icon4)
        self.defaultt_time_speed_button.setIconSize(QtCore.QSize(16, 16))
        self.defaultt_time_speed_button.setObjectName("defaultt_time_speed_button")
        self.sub_layout_2.addWidget(self.defaultt_time_speed_button)
        self.decrease_time_speed_button = QtWidgets.QPushButton(self.time_button_widget)
        self.decrease_time_speed_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decrease_time_speed_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icons/decrease.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decrease_time_speed_button.setIcon(icon5)
        self.decrease_time_speed_button.setIconSize(QtCore.QSize(16, 16))
        self.decrease_time_speed_button.setObjectName("decrease_time_speed_button")
        self.sub_layout_2.addWidget(self.decrease_time_speed_button)
        self.time_speed_label = QtWidgets.QLabel(self.time_button_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_speed_label.sizePolicy().hasHeightForWidth())
        self.time_speed_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.time_speed_label.setFont(font)
        self.time_speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_speed_label.setObjectName("time_speed_label")
        self.sub_layout_2.addWidget(self.time_speed_label)
        self.increase_time_speed_button = QtWidgets.QPushButton(self.time_button_widget)
        self.increase_time_speed_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.increase_time_speed_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../icons/increase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.increase_time_speed_button.setIcon(icon6)
        self.increase_time_speed_button.setIconSize(QtCore.QSize(16, 16))
        self.increase_time_speed_button.setObjectName("increase_time_speed_button")
        self.sub_layout_2.addWidget(self.increase_time_speed_button)
        self.max_time_speed_button = QtWidgets.QPushButton(self.time_button_widget)
        self.max_time_speed_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max_time_speed_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../icons/max.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_time_speed_button.setIcon(icon7)
        self.max_time_speed_button.setIconSize(QtCore.QSize(16, 16))
        self.max_time_speed_button.setObjectName("max_time_speed_button")
        self.sub_layout_2.addWidget(self.max_time_speed_button)
        self.sub_layout_2.setStretch(0, 20)
        self.sub_layout_2.setStretch(1, 20)
        self.sub_layout_2.setStretch(2, 20)
        self.sub_layout_2.setStretch(3, 20)
        self.sub_layout_2.setStretch(4, 20)
        self.control_layout.addWidget(self.time_button_widget)
        spacerItem = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.control_layout.addItem(spacerItem)
        self.file_button_widget = QtWidgets.QWidget(self.container)
        self.file_button_widget.setObjectName("file_button_widget")
        self.sub_layout_3 = QtWidgets.QHBoxLayout(self.file_button_widget)
        self.sub_layout_3.setSpacing(5)
        self.sub_layout_3.setObjectName("sub_layout_3")
        self.save_chart_button = QtWidgets.QPushButton(self.file_button_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_chart_button.setFont(font)
        self.save_chart_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../icons/chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_chart_button.setIcon(icon8)
        self.save_chart_button.setIconSize(QtCore.QSize(16, 16))
        self.save_chart_button.setFlat(True)
        self.save_chart_button.setObjectName("save_chart_button")
        self.save_chart_button.setEnabled(False)
        self.sub_layout_3.addWidget(self.save_chart_button)

        self.show_file_button = QtWidgets.QPushButton(self.file_button_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_file_button.setFont(font)
        self.show_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../icons/filepath.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_file_button.setIcon(icon9)
        self.show_file_button.setIconSize(QtCore.QSize(16, 16))
        self.show_file_button.setFlat(True)
        self.show_file_button.setObjectName("show_file_button")
        self.show_file_button.setEnabled(False)
        self.sub_layout_3.addWidget(self.show_file_button)

        self.control_layout.addWidget(self.file_button_widget)
        self.control_layout.setStretch(3, 70)
        self.main_layout.addLayout(self.control_layout)
        
        self.channel_layout = QtWidgets.QHBoxLayout()
        self.channel_layout.setSpacing(5)
        self.channel_layout.setObjectName("channel_layout")
        self.area_1 = QtWidgets.QVBoxLayout()
        self.area_1.setSpacing(5)
        self.area_1.setObjectName("area_1")

        self.chart_test_1 = QChartView()
        self.chart_test_1.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_1.addWidget(self.chart_test_1)
        self.chart_test_2 = QChartView()
        self.chart_test_2.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_1.addWidget(self.chart_test_2)
        self.chart_test_3 = QChartView()
        self.chart_test_3.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_1.addWidget(self.chart_test_3)
        self.channel_layout.addLayout(self.area_1)

        self.area_2 = QtWidgets.QVBoxLayout()
        self.area_2.setSpacing(5)
        self.area_2.setObjectName("area_2")

        self.chart_test_4 = QChartView()
        self.chart_test_4.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_2.addWidget(self.chart_test_4)
        self.chart_test_5 = QChartView()
        self.chart_test_5.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_2.addWidget(self.chart_test_5)
        self.chart_test_6 = QChartView()
        self.chart_test_6.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_2.addWidget(self.chart_test_6)
        self.channel_layout.addLayout(self.area_2)

        self.area_3 = QtWidgets.QVBoxLayout()
        self.area_3.setSpacing(5)
        self.area_3.setObjectName("area_3")

        self.chart_test_7 = QChartView()
        self.chart_test_7.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_3.addWidget(self.chart_test_7)
        self.chart_test_8 = QChartView()
        self.chart_test_8.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_3.addWidget(self.chart_test_8)
        self.chart_test_9 = QChartView()
        self.chart_test_9.setRenderHint(QtGui.QPainter.Antialiasing)
        self.area_3.addWidget(self.chart_test_9)
        self.channel_layout.addLayout(self.area_3)

        self.main_layout.addLayout(self.channel_layout)
        self.chart_layout = QtWidgets.QHBoxLayout()
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setSpacing(5)
        self.chart_layout.setObjectName("chart_layout")
        self.chart_bars_view = QChartView()
        self.chart_bars_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_layout.addWidget(self.chart_bars_view)
        self.main_layout.addLayout(self.chart_layout)
        self.main_layout.setStretch(0, 5)
        self.main_layout.setStretch(1, 60)
        self.main_layout.setStretch(2, 35)
        sim_window.setCentralWidget(self.container)
        """self.statusbar = QtWidgets.QStatusBar(sim_window)
        self.statusbar.setObjectName("statusbar")
        sim_window.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(sim_window)
        self.toolBar.setObjectName("toolBar")
        sim_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)"""

        self.retranslateUi(sim_window)
        QtCore.QMetaObject.connectSlotsByName(sim_window)

    def retranslateUi(self, sim_window):
        _translate = QtCore.QCoreApplication.translate
        sim_window.setWindowTitle(_translate("sim_window", "Simulation"))
        self.time_speed_label.setText(_translate("sim_window", "X1"))
        self.save_chart_button.setText(_translate("sim_window", ""))
        #self.toolBar.setWindowTitle(_translate("sim_window", "toolBar"))
