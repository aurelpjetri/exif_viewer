# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class PixmapLabel(QtWidgets.QLabel):
    '''
    Custom class inheriting from QLabel.
    'paintEvent' function is overridden in order to
     resize the contained pixmap (image) along with the window
    but conserving the aspect ratio
    '''
    def __init__(self, parent=QtWidgets.QWidget):
        super(PixmapLabel, self).__init__(parent=parent)
        self.setScaledContents(True)

    def paintEvent(self, event: QtGui.QPaintEvent):
        if self.pixmap() is not None:
            style = self.style()
            painter = QtGui.QPainter(self)
            self.drawFrame(painter)
            cr = self.contentsRect()
            cr.adjust(self.margin(), self.margin(), -self.margin(), -self.margin())
            align = QtWidgets.QStyle.visualAlignment(self.layoutDirection(), self.alignment())
            style.drawItemPixmap(painter, cr, align, self.pixmap().scaled(cr.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
        else:
            super().paintEvent(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))

        # central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # main layout and splitter
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalSplitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.centralwidget)
        self.horizontalSplitter.setObjectName("horizontalSplitter")

        # right widget containing viewed image
        self.rightwidget = QtWidgets.QWidget(self.centralwidget)
        self.rightwidget.setObjectName("rightwidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightwidget.sizePolicy().hasHeightForWidth())
        self.rightwidget.setSizePolicy(sizePolicy)

        # ========== LIST SECTION ==========

        # left widget containing selection list of loaded images
        self.leftwidget = QtWidgets.QWidget(self.centralwidget)
        self.leftwidget.setObjectName("leftwidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftwidget.sizePolicy().hasHeightForWidth())
        self.leftwidget.setSizePolicy(sizePolicy)

        # ***** List View Section *****

        # layout used to resize the table along with the window and center it
        self.gridLayout_l = QtWidgets.QGridLayout(self.leftwidget)
        self.gridLayout_l.setObjectName("gridLayout_l")

        # list view of the loaded images
        self.list_view = QtWidgets.QListView(self.leftwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_view.sizePolicy().hasHeightForWidth())
        self.list_view.setSizePolicy(sizePolicy)
        self.list_view.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.list_view.setProperty("isWrapping", False)
        self.list_view.setWordWrap(False)
        self.list_view.setObjectName("list_view")
        self.list_view.setAlternatingRowColors(True)
        self.list_view.setTabKeyNavigation(True)
        self.list_view.setSpacing(3)
        self.list_view.setIconSize(QtCore.QSize(50, 50))
        # EXPERIMENT
        # self.list_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # add list view to its layout so that resizes with the window and its centered
        self.gridLayout_l.addWidget(self.list_view, 0, 0, 1, 1)

        # ========== IMAGE SECTION ==========

        # right widget's layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rightwidget)
        # splitter to enable dragging for widgets resizing
        self.verticalSplitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self.rightwidget)
        self.verticalSplitter.setObjectName("verticalSplitter")

        # ***** Picture Section *****

        # container widget for the label
        self.container_img_lbl = QtWidgets.QWidget(self.rightwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container_img_lbl.sizePolicy().hasHeightForWidth())
        self.container_img_lbl.setSizePolicy(sizePolicy)
        self.container_img_lbl.setObjectName("container_img_lbl")
        self.container_img_lbl.setMinimumSize(256, 256)

        # layout used to center the image
        self.gridLayout = QtWidgets.QGridLayout(self.container_img_lbl)
        self.gridLayout.setObjectName("gridLayout")

        # # customized label class used to contain the loaded image
        self.img_lbl = PixmapLabel(parent=self.container_img_lbl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_lbl.sizePolicy().hasHeightForWidth())
        self.img_lbl.setSizePolicy(sizePolicy)
        self.img_lbl.setMaximumSize(512, 512)
        # self.img_lbl.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(20)
        self.img_lbl.setFont(font)
        self.img_lbl.setAutoFillBackground(False)
        self.img_lbl.setText("")
        self.img_lbl.setScaledContents(True)
        self.img_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.img_lbl.setWordWrap(True)
        self.img_lbl.setObjectName("img_lbl")

        # add image label to its layout so that its centered
        self.gridLayout.addWidget(self.img_lbl, 0, 0, 1, 1)

        self.verticalSplitter.addWidget(self.container_img_lbl)

        # ***** Table Section *****

        # widget used as container for the table view
        self.table_container_w = QtWidgets.QWidget(self.rightwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_container_w.sizePolicy().hasHeightForWidth())
        self.table_container_w.setSizePolicy(sizePolicy)
        self.table_container_w.setObjectName("table_container_w")

        # layout used to resize the table along with the window and center it
        self.gridLayout_2 = QtWidgets.QGridLayout(self.table_container_w)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # table view of the exif data extracted
        self.table_view = QtWidgets.QTableView(self.table_container_w)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_view.sizePolicy().hasHeightForWidth())
        self.table_view.setSizePolicy(sizePolicy)
        self.table_view.setMinimumSize(QtCore.QSize(512, 150))
        self.table_view.setAutoFillBackground(True)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_view.setDragEnabled(False)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setShowGrid(False)
        self.table_view.setWordWrap(True)
        self.table_view.setCornerButtonEnabled(True)
        self.table_view.setObjectName("table_view")
        self.table_view.horizontalHeader().setCascadingSectionResizes(True)
        self.table_view.horizontalHeader().setDefaultSectionSize(256)
        self.table_view.horizontalHeader().setMinimumSectionSize(256)
        self.table_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # the last column of the sable stretches to fill the available space
        self.table_view.horizontalHeader().setStretchLastSection(True)

        # add table view to its layout so that resizes with the window and its centered
        self.gridLayout_2.addWidget(self.table_view, 0, 0, 1, 1)

        # ========== WIDGETS COMPOSITION SECTION ==========

        # add the container to the splitter
        self.verticalSplitter.addWidget(self.table_container_w)

        # add the splitter to the central widget
        self.verticalLayout.addWidget(self.verticalSplitter)

        self.horizontalSplitter.addWidget(self.leftwidget)
        self.horizontalSplitter.addWidget(self.rightwidget)
        self.horizontalLayout.addWidget(self.horizontalSplitter)

        MainWindow.setCentralWidget(self.centralwidget)

        # ========== MENU SECTION ==========

        # MENU BAR
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 560, 22))
        self.menuBar.setObjectName("menuBar")

        # menu File
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        #  open action
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        #  add actions to menu
        self.menuFile.addAction(self.action_open)

        #  open action
        self.action_remove = QtWidgets.QAction(MainWindow)
        self.action_remove.setObjectName("action_remove")
        #  add actions to menu
        self.menuFile.addAction(self.action_remove)

        # menu Tools
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")

        #  action rotate clockwise
        self.actionRotate_clockwise = QtWidgets.QAction(MainWindow)
        self.actionRotate_clockwise.setObjectName("actionRotate_clockwise")
        # action rotate anticlockwise
        self.actionRotate_counter= QtWidgets.QAction(MainWindow)
        self.actionRotate_counter.setObjectName("actionRotate_counter")

        #  add actions to menu
        self.menuTools.addAction(self.actionRotate_clockwise)
        self.menuTools.addAction(self.actionRotate_counter)

        # menu View
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")

        #  action rotate clockwise
        self.actionShowSideList = QtWidgets.QAction(MainWindow)
        self.actionShowSideList.setObjectName("actionShowSideList")
        self.actionShowSideList.setCheckable(True)
        self.actionShowSideList.setChecked(False)

        #  add actions to menu
        self.menuView.addAction(self.actionShowSideList)

        #  add menus to menu Bar
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        # menu bar is within the window independently from the system
        self.menuBar.setNativeMenuBar(False)

        # set composed MENU BAR as main window menu bar
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # set displayed labels
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exiff Viewer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuView.setTitle(_translate("MainWindow", "View"))

        self.action_open.setText(_translate("MainWindow", "Open..."))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))

        self.action_remove.setText(_translate("MainWindow", "Remove current image"))
        self.action_remove.setShortcut(_translate("MainWindow", "Ctrl+W"))

        self.actionRotate_clockwise.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.actionRotate_clockwise.setText(_translate("MainWindow", "Rotate Left ↻"))

        self.actionRotate_counter.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.actionRotate_counter.setText(_translate("MainWindow", "Rotate Right ↺"))

        self.actionShowSideList.setText(_translate("MainWindow", "Side List"))
        self.actionShowSideList.setShortcut(_translate("MainWindow", "Ctrl+M"))
