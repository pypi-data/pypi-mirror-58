import bear_kids_player_main
from PyQt5.QtWidgets import QApplication
# from config_processing import get_config
import sys
def run_bear_kids_player():
    app = QApplication(sys.argv)
    player = bear_kids_player_main.VideoWindow(app =app)
    player.resize(680, 550)
    # showMaximized()
    # show()
    player.setStyleSheet("background-color:black;");
    player.showFullScreen()
    sys.exit(app.exec_())
