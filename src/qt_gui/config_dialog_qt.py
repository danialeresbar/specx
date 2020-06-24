from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChartView


class Ui_config_dialog(object):
    def setupUi(self, config_dialog):
        config_dialog.setObjectName("config_dialog")
        config_dialog.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(config_dialog.sizePolicy().hasHeightForWidth())
        config_dialog.setSizePolicy(sizePolicy)
        config_dialog.setMinimumSize(QtCore.QSize(800, 400))
        config_dialog.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        config_dialog.setWindowIcon(icon)
        config_dialog.setStyleSheet("* {\n"
"    background: #191919;\n"
"    color: #DDDDDD;\n"
"    border: 1px solid #5A5A5A;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget::item:selected {\n"
"    background: #3D7848;\n"
"}\n"
"\n"
"QCheckBox, QRadioButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox::disabled, QRadioButton:disabled {\n"
"    color: #787878;\n"
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
        config_dialog.setModal(True)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(config_dialog)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.preview_box = QtWidgets.QGroupBox(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_box.sizePolicy().hasHeightForWidth())
        self.preview_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.preview_box.setFont(font)
        self.preview_box.setObjectName("preview_box")
        self.view_layout = QtWidgets.QHBoxLayout(self.preview_box)
        self.view_layout.setContentsMargins(10, 15, 10, 10)
        self.view_layout.setSpacing(5)
        self.view_layout.setObjectName("view_layout")
        self.chart_view = QChartView()
        self.view_layout.addWidget(self.chart_view)
        self.horizontalLayout_3.addWidget(self.preview_box)
        self.control_layout = QtWidgets.QVBoxLayout()
        self.control_layout.setContentsMargins(10, 40, 10, 20)
        self.control_layout.setSpacing(30)
        self.control_layout.setObjectName("control_layout")
        self.param_box = QtWidgets.QGroupBox(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.param_box.sizePolicy().hasHeightForWidth())
        self.param_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.param_box.setFont(font)
        self.param_box.setObjectName("param_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.param_box)
        self.verticalLayout.setContentsMargins(10, 20, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.row_1 = QtWidgets.QHBoxLayout()
        self.row_1.setContentsMargins(40, -1, 10, -1)
        self.row_1.setSpacing(5)
        self.row_1.setObjectName("row_1")
        self.rb_1 = QtWidgets.QRadioButton(self.param_box)
        self.rb_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_1.setFont(font)
        self.rb_1.setObjectName("rb_1")
        self.row_1.addWidget(self.rb_1)
        self.rb_2 = QtWidgets.QRadioButton(self.param_box)
        self.rb_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_2.setFont(font)
        self.rb_2.setObjectName("rb_2")
        self.row_1.addWidget(self.rb_2)
        self.rb_3 = QtWidgets.QRadioButton(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_3.setFont(font)
        self.rb_3.setObjectName("rb_3")
        self.row_1.addWidget(self.rb_3)
        self.verticalLayout.addLayout(self.row_1)
        self.row_2 = QtWidgets.QHBoxLayout()
        self.row_2.setContentsMargins(5, 5, 5, 5)
        self.row_2.setSpacing(5)
        self.row_2.setObjectName("row_2")
        self.param_1_label = QtWidgets.QLabel(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_1_label.setFont(font)
        self.param_1_label.setObjectName("param_1_label")
        self.row_2.addWidget(self.param_1_label)
        self.param_1 = QtWidgets.QDoubleSpinBox(self.param_box)
        self.param_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_1.setFont(font)
        self.param_1.setDecimals(10)
        self.param_1.setObjectName("param_1")
        self.row_2.addWidget(self.param_1)
        self.row_2.setStretch(0, 40)
        self.row_2.setStretch(1, 60)
        self.verticalLayout.addLayout(self.row_2)
        self.row_3 = QtWidgets.QHBoxLayout()
        self.row_3.setContentsMargins(5, 5, 5, 5)
        self.row_3.setSpacing(5)
        self.row_3.setObjectName("row_3")
        self.param_2_label = QtWidgets.QLabel(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_2_label.setFont(font)
        self.param_2_label.setObjectName("param_2_label")
        self.row_3.addWidget(self.param_2_label)
        self.param_2 = QtWidgets.QDoubleSpinBox(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_2.setFont(font)
        self.param_2.setDecimals(10)
        self.param_2.setObjectName("param_2")
        self.row_3.addWidget(self.param_2)
        self.row_3.setStretch(0, 40)
        self.row_3.setStretch(1, 60)
        self.verticalLayout.addLayout(self.row_3)
        self.row_4 = QtWidgets.QHBoxLayout()
        self.row_4.setContentsMargins(5, 5, 5, 5)
        self.row_4.setSpacing(5)
        self.row_4.setObjectName("row_4")
        self.param_3_label = QtWidgets.QLabel(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_3_label.setFont(font)
        self.param_3_label.setObjectName("param_3_label")
        self.row_4.addWidget(self.param_3_label)
        self.param_3 = QtWidgets.QDoubleSpinBox(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_3.setFont(font)
        self.param_3.setDecimals(10)
        self.param_3.setObjectName("param_3")
        self.row_4.addWidget(self.param_3)
        self.row_4.setStretch(0, 40)
        self.row_4.setStretch(1, 60)
        self.verticalLayout.addLayout(self.row_4)
        self.row_5 = QtWidgets.QHBoxLayout()
        self.row_5.setContentsMargins(5, 5, 5, 5)
        self.row_5.setSpacing(5)
        self.row_5.setObjectName("row_5")
        self.param_4_label = QtWidgets.QLabel(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_4_label.setFont(font)
        self.param_4_label.setObjectName("param_4_label")
        self.row_5.addWidget(self.param_4_label)
        self.param_4 = QtWidgets.QDoubleSpinBox(self.param_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.param_4.setFont(font)
        self.param_4.setDecimals(10)
        self.param_4.setObjectName("param_4")
        self.row_5.addWidget(self.param_4)
        self.row_5.setStretch(0, 40)
        self.row_5.setStretch(1, 60)
        self.verticalLayout.addLayout(self.row_5)
        self.control_layout.addWidget(self.param_box)
        self.button_container = QtWidgets.QVBoxLayout()
        self.button_container.setContentsMargins(0, 0, 0, 0)
        self.button_container.setSpacing(10)
        self.button_container.setObjectName("button_container")
        self.b_layout = QtWidgets.QHBoxLayout()
        self.b_layout.setContentsMargins(40, 5, 40, 5)
        self.b_layout.setSpacing(0)
        self.b_layout.setObjectName("b_layout")
        self.submit_button = QtWidgets.QPushButton(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submit_button.setFont(font)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/accept.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.submit_button.setIcon(icon1)
        self.submit_button.setIconSize(QtCore.QSize(60, 60))
        self.submit_button.setFlat(True)
        self.submit_button.setObjectName("submit_button")
        self.b_layout.addWidget(self.submit_button)
        self.reject_button = QtWidgets.QPushButton(config_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reject_button.sizePolicy().hasHeightForWidth())
        self.reject_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reject_button.setFont(font)
        self.reject_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reject_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/reject.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reject_button.setIcon(icon2)
        self.reject_button.setIconSize(QtCore.QSize(60, 60))
        self.reject_button.setFlat(True)
        self.reject_button.setObjectName("reject_button")
        self.b_layout.addWidget(self.reject_button)
        self.b_layout.setStretch(0, 50)
        self.b_layout.setStretch(1, 50)
        self.button_container.addLayout(self.b_layout)
        self.button_container.setStretch(0, 40)
        self.control_layout.addLayout(self.button_container)
        self.control_layout.setStretch(0, 75)
        self.control_layout.setStretch(1, 25)
        self.horizontalLayout_3.addLayout(self.control_layout)
        self.horizontalLayout_3.setStretch(0, 60)
        self.horizontalLayout_3.setStretch(1, 40)

        self.retranslateUi(config_dialog)
        QtCore.QMetaObject.connectSlotsByName(config_dialog)

    def retranslateUi(self, config_dialog):
        _translate = QtCore.QCoreApplication.translate
        config_dialog.setWindowTitle(_translate("config_dialog", "Configuración"))
        self.preview_box.setTitle(_translate("config_dialog", "Vista preliminar"))
        self.param_box.setTitle(_translate("config_dialog", "Parámetros"))
        self.rb_1.setText(_translate("config_dialog", "1P"))
        self.rb_2.setText(_translate("config_dialog", "2P"))
        self.rb_3.setText(_translate("config_dialog", "3P"))
        self.param_1_label.setText(_translate("config_dialog", "Parámetro 1:"))
        self.param_2_label.setText(_translate("config_dialog", "Parámetro 2:"))
        self.param_3_label.setText(_translate("config_dialog", "Parámetro 3:"))
        self.param_4_label.setText(_translate("config_dialog", "Parámetro 4:"))
