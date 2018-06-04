import sys
from PyQt5.QtWidgets import QApplication
from custom_viewer import CustomViewer
from custom_model import CustomModel


def run():
    app = QApplication(sys.argv)
    tool = CustomViewer(CustomModel())
    tool.show()
    tool.activateWindow()
    sys.exit(app.exec_())
run()
