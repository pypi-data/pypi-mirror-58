# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapsVisualizer(object):
    def setupUi(self, MapsVisualizer):
        MapsVisualizer.setObjectName("MapsVisualizer")
        MapsVisualizer.resize(1000, 754)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MapsVisualizer.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MapsVisualizer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandTabs = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandTabs.sizePolicy().hasHeightForWidth())
        self.commandTabs.setSizePolicy(sizePolicy)
        self.commandTabs.setMinimumSize(QtCore.QSize(250, 0))
        self.commandTabs.setObjectName("commandTabs")
        self.generalOptions = QtWidgets.QWidget()
        self.generalOptions.setAccessibleName("")
        self.generalOptions.setObjectName("generalOptions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.generalOptions)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.generalTabPosition = QtWidgets.QGridLayout()
        self.generalTabPosition.setSpacing(0)
        self.generalTabPosition.setObjectName("generalTabPosition")
        self.gridLayout_4.addLayout(self.generalTabPosition, 0, 0, 1, 1)
        self.commandTabs.addTab(self.generalOptions, "")
        self.mapOptions = QtWidgets.QWidget()
        self.mapOptions.setObjectName("mapOptions")
        self.gridLayout = QtWidgets.QGridLayout(self.mapOptions)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.mapSpecificTabPosition = QtWidgets.QGridLayout()
        self.mapSpecificTabPosition.setSpacing(0)
        self.mapSpecificTabPosition.setObjectName("mapSpecificTabPosition")
        self.gridLayout.addLayout(self.mapSpecificTabPosition, 0, 0, 1, 1)
        self.commandTabs.addTab(self.mapOptions, "")
        self.textInfoTab = QtWidgets.QWidget()
        self.textInfoTab.setObjectName("textInfoTab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.textInfoTab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.textInfoTabPosition = QtWidgets.QGridLayout()
        self.textInfoTabPosition.setSpacing(0)
        self.textInfoTabPosition.setObjectName("textInfoTabPosition")
        self.gridLayout_9.addLayout(self.textInfoTabPosition, 0, 0, 1, 1)
        self.commandTabs.addTab(self.textInfoTab, "")
        self.verticalLayout.addWidget(self.commandTabs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.auto_rendering = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.auto_rendering.setObjectName("auto_rendering")
        self.horizontalLayout.addWidget(self.auto_rendering)
        self.manual_render = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.manual_render.setIconSize(QtCore.QSize(16, 16))
        self.manual_render.setObjectName("manual_render")
        self.horizontalLayout.addWidget(self.manual_render)
        self.undo_config = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.undo_config.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main/arrow_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_config.setIcon(icon1)
        self.undo_config.setObjectName("undo_config")
        self.horizontalLayout.addWidget(self.undo_config)
        self.redo_config = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.redo_config.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main/arrow_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo_config.setIcon(icon2)
        self.redo_config.setObjectName("redo_config")
        self.horizontalLayout.addWidget(self.redo_config)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.plotLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setSpacing(0)
        self.plotLayout.setObjectName("plotLayout")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_2.setStretch(0, 1)
        MapsVisualizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapsVisualizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MapsVisualizer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MapsVisualizer)
        self.statusbar.setObjectName("statusbar")
        MapsVisualizer.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MapsVisualizer)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSaveImage = QtWidgets.QAction(MapsVisualizer)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionAbout = QtWidgets.QAction(MapsVisualizer)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExtra_plot_options = QtWidgets.QAction(MapsVisualizer)
        self.actionExtra_plot_options.setObjectName("actionExtra_plot_options")
        self.actionSave_settings = QtWidgets.QAction(MapsVisualizer)
        self.actionSave_settings.setObjectName("actionSave_settings")
        self.actionLoad_settings = QtWidgets.QAction(MapsVisualizer)
        self.actionLoad_settings.setObjectName("actionLoad_settings")
        self.actionAdd_new_files = QtWidgets.QAction(MapsVisualizer)
        self.actionAdd_new_files.setObjectName("actionAdd_new_files")
        self.action_Clear = QtWidgets.QAction(MapsVisualizer)
        self.action_Clear.setObjectName("action_Clear")
        self.actionNew_window = QtWidgets.QAction(MapsVisualizer)
        self.actionNew_window.setObjectName("actionNew_window")
        self.menuFile.addAction(self.actionAdd_new_files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_settings)
        self.menuFile.addAction(self.actionLoad_settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSaveImage)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_window)
        self.menuFile.addAction(self.action_Clear)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MapsVisualizer)
        self.commandTabs.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MapsVisualizer.close)
        QtCore.QMetaObject.connectSlotsByName(MapsVisualizer)

    def retranslateUi(self, MapsVisualizer):
        _translate = QtCore.QCoreApplication.translate
        MapsVisualizer.setWindowTitle(_translate("MapsVisualizer", "MDT Maps Visualizer"))
        self.commandTabs.setTabText(self.commandTabs.indexOf(self.generalOptions), _translate("MapsVisualizer", "General"))
        self.commandTabs.setTabText(self.commandTabs.indexOf(self.mapOptions), _translate("MapsVisualizer", "Maps"))
        self.commandTabs.setTabText(self.commandTabs.indexOf(self.textInfoTab), _translate("MapsVisualizer", "Textual"))
        self.auto_rendering.setText(_translate("MapsVisualizer", "Auto redraw"))
        self.manual_render.setToolTip(_translate("MapsVisualizer", "Manually redraw the figure"))
        self.manual_render.setText(_translate("MapsVisualizer", "Redraw"))
        self.undo_config.setToolTip(_translate("MapsVisualizer", "Undo"))
        self.redo_config.setToolTip(_translate("MapsVisualizer", "Redo"))
        self.menuFile.setTitle(_translate("MapsVisualizer", "&File"))
        self.menuAbout.setTitle(_translate("MapsVisualizer", "&Help"))
        self.actionQuit.setText(_translate("MapsVisualizer", "&Quit"))
        self.actionQuit.setShortcut(_translate("MapsVisualizer", "Ctrl+Q"))
        self.actionSaveImage.setText(_translate("MapsVisualizer", "&Save image"))
        self.actionSaveImage.setShortcut(_translate("MapsVisualizer", "Ctrl+S"))
        self.actionAbout.setText(_translate("MapsVisualizer", "&About"))
        self.actionExtra_plot_options.setText(_translate("MapsVisualizer", "&Extra plot options"))
        self.actionSave_settings.setText(_translate("MapsVisualizer", "&Export settings"))
        self.actionLoad_settings.setText(_translate("MapsVisualizer", "&Import settings"))
        self.actionAdd_new_files.setText(_translate("MapsVisualizer", "&Add new file(s)"))
        self.action_Clear.setText(_translate("MapsVisualizer", "&Clear"))
        self.actionNew_window.setText(_translate("MapsVisualizer", "&New window"))

from . import main_rc
