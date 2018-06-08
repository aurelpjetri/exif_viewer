from custom_design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QTransform, QPixmap


# For data view
class CustomViewer(QMainWindow, Ui_MainWindow):
    def __init__(self, model):
        super(self.__class__, self).__init__()

        # model data
        self.model = model

        # from Ui_MainWindow class
        self.setupUi(self)

        # keeps track of the index of the displayed image
        self.displayed_index = -1

        # customize behavior
        self.customize_behavior()

    def customize_behavior(self):

        # open action in the File menu
        self.action_open.triggered.connect(self._load_images)
        # remove action in the File menu
        self.action_remove.triggered.connect(self._remove_current_image)
        # rotate actions in the Tools menu
        self.actionRotate_clockwise.triggered.connect(self._rotate_image_cw)
        self.actionRotate_counter.triggered.connect(self._rotate_image_cc)
        # toggle side list action
        self.actionShowSideList.triggered.connect(self._toggle_side_list)

        # INIT list view
        # associate the view to the model
        self.list_view.setModel(self.model.list_model)
        # set up the image selection controller
        self.list_view.clicked.connect(self._on_clicked_list_item)

        # EXPERIMENT
        # self.list_view.customContextMenuRequested()

        # set the initial message
        self.img_lbl.setText('Go to "File -> Open..." or press "Ctrl+O" to select one or more jpegs')
        self.setWindowTitle('ExifViewer - Wellcome')

        # initially hide table and side list
        self.table_container_w.hide()
        self.leftwidget.hide()
        self.actionShowSideList.setChecked(False)

    def _load_images(self):
        # load one or multiple files
        file_name = QFileDialog.getOpenFileNames(self, 'Open file', '/Users/aurel/Pictures', "Image files (*.jpg *.jpeg)")
        print(file_name[0])

        if len(file_name[0]) > 0:
            self.model.load_data(file_name[0])

            # display the last loaded image
            self._view_image(-1)
            self.setWindowTitle('ExifViewer')

            self.displayed_index = len(self.model.pixmaps)-1

            # if more then one image is loaded show the side list
            if len(self.model.pixmaps) > 1:
                self.actionShowSideList.setChecked(True)
                self._toggle_side_list()

    def _view_image(self, index):
        # views the image associated to the index

        # put the picture in the label
        self.img_lbl.setPixmap(self.model.pixmaps[index])
        # show exif table
        self.table_container_w.show()
        # associate the table view to the correct model
        self.table_view.setModel(self.model.table_models[index])

    def _on_clicked_list_item(self):
        # extract the selected image's index
        selected_index = self.list_view.selectionModel().currentIndex().row()
        self.displayed_index = selected_index
        # view the image
        self._view_image(selected_index)

    def _rotate_image_cw(self):
        # rotate image clockwise
        if self.img_lbl.pixmap() is not None:
            rotation = QTransform().rotate(90.0)
            pm = self.img_lbl.pixmap()
            pm = pm.transformed(rotation)
            self.model.pixmaps[self.displayed_index] = pm
            self.img_lbl.setPixmap(pm)

    def _rotate_image_cc(self):
        # rotate image anticlockwise
        if self.img_lbl.pixmap() is not None:
            rotation = QTransform().rotate(-90.0)
            pm = self.img_lbl.pixmap()
            pm = pm.transformed(rotation)
            self.model.pixmaps[self.displayed_index] = pm
            self.img_lbl.setPixmap(pm)

    def _toggle_side_list(self):
        # show/hide side list
        if self.actionShowSideList.isChecked() is False:
            self.leftwidget.hide()
        else:
            self.leftwidget.show()

    def _remove_current_image(self):
        # remove the currently displayed image
        if self.displayed_index >= 0:
            self.model.remove_image(self.displayed_index)
            self.displayed_index -= 1
            # if there are images left view the next one
            if len(self.model.pixmaps) > 0:
                self._view_image(self.displayed_index)
            # else hide table and side list and restore the initial message
            else:
                self.table_container_w.hide()
                self.actionShowSideList.setChecked(False)
                self._toggle_side_list()
                self.img_lbl.setPixmap(QPixmap())
                self.img_lbl.setText('Go to "File -> Open..." or press "Ctrl+O" to select one or more jpegs')
