from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):

        def setupUi(self, main_window):
                main_window.setObjectName("main_window")
                main_window.resize(600, 450)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
                main_window.setSizePolicy(sizePolicy)
                main_window.setMinimumSize(QtCore.QSize(600, 450))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                main_window.setWindowIcon(icon)
                main_window.setStyleSheet("* {\n"
        "    background: #191919;\n"
        "    color: #DDDDDD;\n"
        "    border: 1px solid #5A5A5A;\n"
        "}\n"
        "\n"
        "QWidget::item:selected {\n"
        "    background: #3D7848;\n"
        "}\n"
        "\n"
        "QCheckBox::disabled, QRadioButton:disabled {\n"
	"    color: #787878;\n"
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
        "QComboBox:disabled {\n"
	"color: #787878;\n"
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
        "QAbstractSpinBox:disabled {\n"
	"    color: #787878;\n"
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
                self.container = QtWidgets.QWidget(main_window)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
                self.container.setSizePolicy(sizePolicy)
                self.container.setStyleSheet("QGroupBox::title {\n"
        "    subcontrol-origin: margin;\n"
        "    padding-left: 5px;\n"
        "    padding-right: 5px;\n"
        "    padding-top: 4px;\n"
        "}")
                self.container.setObjectName("container")
                self.main_layout = QtWidgets.QGridLayout(self.container)
                self.main_layout.setObjectName("main_layout")
                self.config_layout = QtWidgets.QVBoxLayout()
                self.config_layout.setContentsMargins(10, 40, 10, 40)
                self.config_layout.setSpacing(60)
                self.config_layout.setObjectName("config_layout")
                self.box_params = QtWidgets.QGroupBox(self.container)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.box_params.sizePolicy().hasHeightForWidth())
                self.box_params.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.box_params.setFont(font)
                self.box_params.setStyleSheet("")
                self.box_params.setObjectName("box_params")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.box_params)
                self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout_2.setSpacing(5)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.param_1 = QtWidgets.QHBoxLayout()
                self.param_1.setSpacing(5)
                self.param_1.setObjectName("param_1")
                self.sample_label = QtWidgets.QLabel(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.sample_label.setFont(font)
                self.sample_label.setObjectName("sample_label")
                self.param_1.addWidget(self.sample_label)
                self.sample_time = QtWidgets.QSpinBox(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.sample_time.setFont(font)
                self.sample_time.setMinimum(1)
                self.sample_time.setMaximum(15)
                self.sample_time.setProperty("value", 5)
                self.sample_time.setObjectName("sample_time")
                self.param_1.addWidget(self.sample_time)
                self.param_1.setStretch(0, 60)
                self.param_1.setStretch(1, 40)
                self.verticalLayout_2.addLayout(self.param_1)
                self.param_2 = QtWidgets.QHBoxLayout()
                self.param_2.setSpacing(5)
                self.param_2.setObjectName("param_2")
                self.threshold_label = QtWidgets.QLabel(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.threshold_label.setFont(font)
                self.threshold_label.setObjectName("threshold_label")
                self.param_2.addWidget(self.threshold_label)
                self.threshold = QtWidgets.QDoubleSpinBox(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.threshold.setFont(font)
                self.threshold.setMinimum(0.01)
                self.threshold.setMaximum(0.8)
                self.threshold.setSingleStep(0.05)
                self.threshold.setProperty("value", 0.33)
                self.threshold.setObjectName("threshold")
                self.param_2.addWidget(self.threshold)
                self.param_2.setStretch(0, 60)
                self.param_2.setStretch(1, 40)
                self.verticalLayout_2.addLayout(self.param_2)
                self.options = QtWidgets.QHBoxLayout()
                self.options.setObjectName("options")
                self.energy_flag = QtWidgets.QCheckBox(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.energy_flag.setFont(font)
                self.energy_flag.setObjectName("energy_flag")
                self.options.addWidget(self.energy_flag)
                self.usage_flag = QtWidgets.QCheckBox(self.box_params)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.usage_flag.setFont(font)
                self.usage_flag.setObjectName("usage_flag")
                self.options.addWidget(self.usage_flag)
                self.verticalLayout_2.addLayout(self.options)
                self.config_layout.addWidget(self.box_params)
                self.buttons_layout = QtWidgets.QHBoxLayout()
                self.buttons_layout.setContentsMargins(20, -1, 20, -1)
                self.buttons_layout.setSpacing(5)
                self.buttons_layout.setObjectName("buttons_layout")
                self.run_button = QtWidgets.QPushButton(self.container)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
                self.run_button.setSizePolicy(sizePolicy)
                self.run_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.run_button.setStyleSheet("QPushButton{\n"
        "    border: none;\n"
        "}")
                self.run_button.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("icons/run.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.run_button.setIcon(icon1)
                self.run_button.setIconSize(QtCore.QSize(110, 110))
                self.run_button.setFlat(True)
                self.run_button.setObjectName("run_button")
                self.buttons_layout.addWidget(self.run_button)
                self.run_button.setEnabled(False)
                self.clean_button = QtWidgets.QPushButton(self.container)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.clean_button.sizePolicy().hasHeightForWidth())
                self.clean_button.setSizePolicy(sizePolicy)
                self.clean_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.clean_button.setStyleSheet("QPushButton{\n"
        "    border: none;\n"
        "}")
                self.clean_button.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("icons/clean.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.clean_button.setIcon(icon2)
                self.clean_button.setIconSize(QtCore.QSize(110, 110))
                self.clean_button.setFlat(True)
                self.clean_button.setObjectName("clean_button")
                self.buttons_layout.addWidget(self.clean_button)
                self.config_layout.addLayout(self.buttons_layout)
                self.config_layout.setStretch(0, 50)
                self.config_layout.setStretch(1, 50)
                self.main_layout.addLayout(self.config_layout, 0, 1, 1, 1)
                self.freq_layout = QtWidgets.QGridLayout()
                self.freq_layout.setContentsMargins(5, 5, 5, 5)
                self.freq_layout.setSpacing(5)
                self.freq_layout.setObjectName("freq_layout")
                self.box_freq = QtWidgets.QGroupBox(self.container)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.box_freq.sizePolicy().hasHeightForWidth())
                self.box_freq.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.box_freq.setFont(font)
                self.box_freq.setObjectName("box_freq")
                self.freq_layout_2 = QtWidgets.QVBoxLayout(self.box_freq)
                self.freq_layout_2.setContentsMargins(10, 10, 10, 5)
                self.freq_layout_2.setSpacing(5)
                self.freq_layout_2.setObjectName("freq_layout_2")
                self.field_1 = QtWidgets.QHBoxLayout()
                self.field_1.setSpacing(5)
                self.field_1.setObjectName("field_1")
                self.channel_1_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_1_label.setFont(font)
                self.channel_1_label.setObjectName("channel_1_label")
                self.field_1.addWidget(self.channel_1_label)
                self.pdf_1 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_1.setFont(font)
                self.pdf_1.setMaxVisibleItems(5)
                self.pdf_1.setObjectName("pdf_1")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.pdf_1.addItem("")
                self.field_1.addWidget(self.pdf_1)
                self.field_1.setStretch(0, 30)
                self.field_1.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_1)
                self.field_2 = QtWidgets.QHBoxLayout()
                self.field_2.setSpacing(5)
                self.field_2.setObjectName("field_2")
                self.channel_2_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_2_label.setFont(font)
                self.channel_2_label.setObjectName("channel_2_label")
                self.field_2.addWidget(self.channel_2_label)
                self.pdf_2 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_2.setFont(font)
                self.pdf_2.setMaxVisibleItems(5)
                self.pdf_2.setObjectName("pdf_2")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.pdf_2.addItem("")
                self.field_2.addWidget(self.pdf_2)
                self.field_2.setStretch(0, 30)
                self.field_2.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_2)
                self.field_3 = QtWidgets.QHBoxLayout()
                self.field_3.setSpacing(5)
                self.field_3.setObjectName("field_3")
                self.channel_3_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_3_label.setFont(font)
                self.channel_3_label.setObjectName("channel_3_label")
                self.field_3.addWidget(self.channel_3_label)
                self.pdf_3 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_3.setFont(font)
                self.pdf_3.setMaxVisibleItems(5)
                self.pdf_3.setObjectName("pdf_3")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.pdf_3.addItem("")
                self.field_3.addWidget(self.pdf_3)
                self.field_3.setStretch(0, 30)
                self.field_3.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_3)
                self.field_4 = QtWidgets.QHBoxLayout()
                self.field_4.setSpacing(5)
                self.field_4.setObjectName("field_4")
                self.channel_4_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_4_label.setFont(font)
                self.channel_4_label.setObjectName("channel_4_label")
                self.field_4.addWidget(self.channel_4_label)
                self.pdf_4 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_4.setFont(font)
                self.pdf_4.setMaxVisibleItems(5)
                self.pdf_4.setObjectName("pdf_4")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.pdf_4.addItem("")
                self.field_4.addWidget(self.pdf_4)
                self.field_4.setStretch(0, 30)
                self.field_4.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_4)
                self.field_5 = QtWidgets.QHBoxLayout()
                self.field_5.setSpacing(5)
                self.field_5.setObjectName("field_5")
                self.channel_5_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_5_label.setFont(font)
                self.channel_5_label.setObjectName("channel_5_label")
                self.field_5.addWidget(self.channel_5_label)
                self.pdf_5 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_5.setFont(font)
                self.pdf_5.setMaxVisibleItems(5)
                self.pdf_5.setObjectName("pdf_5")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.pdf_5.addItem("")
                self.field_5.addWidget(self.pdf_5)
                self.field_5.setStretch(0, 30)
                self.field_5.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_5)
                self.field_6 = QtWidgets.QHBoxLayout()
                self.field_6.setSpacing(5)
                self.field_6.setObjectName("field_6")
                self.channel_6_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_6_label.setFont(font)
                self.channel_6_label.setObjectName("channel_6_label")
                self.field_6.addWidget(self.channel_6_label)
                self.pdf_6 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_6.setFont(font)
                self.pdf_6.setMaxVisibleItems(5)
                self.pdf_6.setObjectName("pdf_6")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.pdf_6.addItem("")
                self.field_6.addWidget(self.pdf_6)
                self.field_6.setStretch(0, 30)
                self.field_6.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_6)
                self.field_7 = QtWidgets.QHBoxLayout()
                self.field_7.setSpacing(5)
                self.field_7.setObjectName("field_7")
                self.channel_7_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_7_label.setFont(font)
                self.channel_7_label.setObjectName("channel_7_label")
                self.field_7.addWidget(self.channel_7_label)
                self.pdf_7 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_7.setFont(font)
                self.pdf_7.setMaxVisibleItems(5)
                self.pdf_7.setObjectName("pdf_7")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.pdf_7.addItem("")
                self.field_7.addWidget(self.pdf_7)
                self.field_7.setStretch(0, 30)
                self.field_7.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_7)
                self.field_8 = QtWidgets.QHBoxLayout()
                self.field_8.setSpacing(5)
                self.field_8.setObjectName("field_8")
                self.channel_8_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_8_label.setFont(font)
                self.channel_8_label.setObjectName("channel_8_label")
                self.field_8.addWidget(self.channel_8_label)
                self.pdf_8 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_8.setFont(font)
                self.pdf_8.setMaxVisibleItems(5)
                self.pdf_8.setObjectName("pdf_8")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.pdf_8.addItem("")
                self.field_8.addWidget(self.pdf_8)
                self.field_8.setStretch(0, 30)
                self.field_8.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_8)
                self.field_9 = QtWidgets.QHBoxLayout()
                self.field_9.setSpacing(5)
                self.field_9.setObjectName("field_9")
                self.channel_9_label = QtWidgets.QLabel(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.channel_9_label.setFont(font)
                self.channel_9_label.setObjectName("channel_9_label")
                self.field_9.addWidget(self.channel_9_label)
                self.pdf_9 = QtWidgets.QComboBox(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.pdf_9.setFont(font)
                self.pdf_9.setMaxVisibleItems(5)
                self.pdf_9.setObjectName("pdf_9")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.pdf_9.addItem("")
                self.field_9.addWidget(self.pdf_9)
                self.field_9.setStretch(0, 30)
                self.field_9.setStretch(1, 70)
                self.freq_layout_2.addLayout(self.field_9)
                self.foot_layout = QtWidgets.QHBoxLayout()
                self.foot_layout.setSpacing(5)
                self.foot_layout.setObjectName("foot_layout")
                self.save_file_button = QtWidgets.QPushButton(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.save_file_button.setFont(font)
                self.save_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.save_file_button.setObjectName("save_file_button")
                self.foot_layout.addWidget(self.save_file_button)
                self.load_file_button = QtWidgets.QPushButton(self.box_freq)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.load_file_button.setFont(font)
                self.load_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.load_file_button.setObjectName("load_file_button")
                self.foot_layout.addWidget(self.load_file_button)
                self.foot_layout.setStretch(0, 50)
                self.foot_layout.setStretch(1, 50)
                self.freq_layout_2.addLayout(self.foot_layout)
                self.freq_layout.addWidget(self.box_freq, 0, 0, 1, 1)
                self.main_layout.addLayout(self.freq_layout, 0, 0, 1, 1)
                self.main_layout.setColumnStretch(0, 50)
                self.main_layout.setColumnStretch(1, 50)
                main_window.setCentralWidget(self.container)
                self.menubar = QtWidgets.QMenuBar(main_window)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.menubar.setFont(font)
                self.menubar.setObjectName("menubar")
                self.file_menu = QtWidgets.QMenu(self.menubar)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.file_menu.setFont(font)
                self.file_menu.setObjectName("file_menu")
                self.about_menu = QtWidgets.QMenu(self.menubar)
                font = QtGui.QFont()
                font.setPointSize(10)
                self.about_menu.setFont(font)
                self.about_menu.setObjectName("about_menu")
                main_window.setMenuBar(self.menubar)
                self.statusBar = QtWidgets.QStatusBar(main_window)
                self.statusBar.setObjectName("statusBar")
                main_window.setStatusBar(self.statusBar)
                self.toolBar = QtWidgets.QToolBar(main_window)
                self.toolBar.setObjectName("toolBar")
                main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
                self.new_action_menu = QtWidgets.QAction(main_window)
                self.new_action_menu.setObjectName("new_action_menu")
                self.exit_action_menu = QtWidgets.QAction(main_window)
                self.exit_action_menu.setObjectName("exit_action_menu")
                self.about_action_menu = QtWidgets.QAction(main_window)
                self.about_action_menu.setObjectName("about_action_menu")
                self.help_action_menu = QtWidgets.QAction(main_window)
                self.help_action_menu.setObjectName("help_action_menu")
                self.file_menu.addAction(self.new_action_menu)
                self.file_menu.addAction(self.exit_action_menu)
                self.about_menu.addAction(self.about_action_menu)
                self.about_menu.addAction(self.help_action_menu)
                self.menubar.addAction(self.file_menu.menuAction())
                self.menubar.addAction(self.about_menu.menuAction())

                self.retranslateUi(main_window)
                QtCore.QMetaObject.connectSlotsByName(main_window)

        def retranslateUi(self, main_window):
                _translate = QtCore.QCoreApplication.translate
                main_window.setWindowTitle(_translate("main_window", "Specx"))
                self.box_params.setTitle(_translate("main_window", "Parámetros"))
                self.sample_label.setText(_translate("main_window", "Tiempo de muestreo:"))
                self.sample_time.setSuffix(_translate("main_window", "min"))
                self.threshold_label.setText(_translate("main_window", "Umbral de energía:"))
                self.energy_flag.setText(_translate("main_window", "Energía"))
                self.usage_flag.setText(_translate("main_window", "Ocupación de canal"))
                self.box_freq.setTitle(_translate("main_window", "Frecuencias"))
                self.channel_1_label.setText(_translate("main_window", "473 MHz"))
                self.pdf_1.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_1.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_1.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_1.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_1.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_1.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_1.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_1.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_1.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_1.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_1.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_2_label.setText(_translate("main_window", "479 MHz"))
                self.pdf_2.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_2.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_2.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_2.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_2.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_2.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_2.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_2.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_2.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_2.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_2.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_3_label.setText(_translate("main_window", "485 MHz"))
                self.pdf_3.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_3.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_3.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_3.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_3.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_3.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_3.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_3.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_3.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_3.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_3.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_4_label.setText(_translate("main_window", "491 MHz"))
                self.pdf_4.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_4.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_4.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_4.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_4.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_4.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_4.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_4.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_4.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_4.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_4.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_5_label.setText(_translate("main_window", "497 MHz"))
                self.pdf_5.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_5.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_5.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_5.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_5.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_5.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_5.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_5.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_5.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_5.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_5.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_6_label.setText(_translate("main_window", "503 MHz"))
                self.pdf_6.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_6.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_6.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_6.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_6.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_6.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_6.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_6.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_6.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_6.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_6.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_7_label.setText(_translate("main_window", "509 MHz"))
                self.pdf_7.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_7.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_7.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_7.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_7.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_7.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_7.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_7.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_7.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_7.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_7.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_8_label.setText(_translate("main_window", "551 MHz"))
                self.pdf_8.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_8.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_8.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_8.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_8.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_8.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_8.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_8.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_8.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_8.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_8.setItemText(10, _translate("main_window", "Weibull"))
                self.channel_9_label.setText(_translate("main_window", "557 MHz"))
                self.pdf_9.setItemText(0, _translate("main_window", "Selecciona"))
                self.pdf_9.setItemText(1, _translate("main_window", "Bernoulli"))
                self.pdf_9.setItemText(2, _translate("main_window", "Beta"))
                self.pdf_9.setItemText(3, _translate("main_window", "Gamma"))
                self.pdf_9.setItemText(4, _translate("main_window", "Gumbel max"))
                self.pdf_9.setItemText(5, _translate("main_window", "Laplace"))
                self.pdf_9.setItemText(6, _translate("main_window", "Lognormal"))
                self.pdf_9.setItemText(7, _translate("main_window", "Normal"))
                self.pdf_9.setItemText(8, _translate("main_window", "Rayleigh"))
                self.pdf_9.setItemText(9, _translate("main_window", "Uniforme"))
                self.pdf_9.setItemText(10, _translate("main_window", "Weibull"))
                self.save_file_button.setText(_translate("main_window", "Cargar"))
                self.load_file_button.setText(_translate("main_window", "Guardar"))
                self.file_menu.setTitle(_translate("main_window", "Archivo"))
                self.about_menu.setTitle(_translate("main_window", "Acerca"))
                self.toolBar.setWindowTitle(_translate("main_window", "toolBar"))
                self.new_action_menu.setText(_translate("main_window", "Nuevo..."))
                self.exit_action_menu.setText(_translate("main_window", "Salir"))
                self.about_action_menu.setText(_translate("main_window", "Acerca de"))
                self.help_action_menu.setText(_translate("main_window", "Ayuda"))
