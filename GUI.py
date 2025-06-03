"""The gui for TFT bot program
"""
from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, \
    QPushButton, QWidget, QLabel, QRadioButton, QLCDNumber, \
    QLineEdit, QPlainTextEdit, QCheckBox
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtCore import QFile, SIGNAL
from Script_function import run_and_surr, exist, auto_pick, run_and_surr_party
from threading import Thread
import time
from sys import exit

time_between_games = 6
champ_set = set()
surr_time = 605


class Bot:
    """ A class worked for the TFT bot's window
    """
    def __init__(self) -> None:
        """ Initializing a given ui file.
        """
        # # Reading the ui file.
        # qfile_bot = QFile('ui/main.ui')
        # qfile_bot.open(QFile.ReadOnly)
        # qfile_bot.close()
        #
        # # Creating a window variable represents the whole UI.
        # self.window = QUiLoader().load(qfile_bot)
        #
        # self.window.start_butt.clicked.connect(self.start)
        # self.window.stop_butt.clicked.connect(self.stop)

        self.font1 = QFont()
        self.font1.setFamily('Calibri')
        self.font1.setPointSize(12)

        self.font1_bold = QFont()
        self.font1_bold.setFamily('Calibri')
        self.font1_bold.setBold(True)
        self.font1_bold.setPointSize(12)

        self.window = QWidget()
        self.window.resize(245, 250)
        self.window.setWindowTitle('TFT Helper')
        self.window.setFont(self.font1)
        self.window.setStyleSheet('QPushButton{border: 2px solid rgb(152, 152, 152);'
                                  'border-radius: 15px;}'
                                  'QPushButton:hover{border: 2px solid rgb(226, 226, 226);'
                                  'background: rgb(223, 223, 223);'
                                  'border-radius: 15px;}'
                                  'QPushButton:pressed {border: 2px solid rgb(152, 152, 152);'
                                  'background: rgb(231, 231, 231);'
                                  'border-radius: 15px;}')

        self.game_his_lab = QLabel('Played Games: ', self.window)
        self.game_his_lab.resize(111, 41)
        self.game_his_lab.move(10, 40)
        self.game_his_lab.setFont(self.font1_bold)

        self.mode_lab = QLabel('Mode: ', self.window)
        self.mode_lab.resize(51, 41)
        self.mode_lab.move(10, 100)
        self.mode_lab.setFont(self.font1_bold)

        self.game_his_lcd = QLCDNumber(self.window)
        self.game_his_lcd.resize(101, 51)
        self.game_his_lcd.move(130, 40)

        self.mode1 = QRadioButton('Auto surr', self.window)
        self.mode1.resize(91, 21)
        self.mode1.move(70, 110)
        self.mode1.setChecked(True)

        self.mode2 = QRadioButton('Auto play', self.window)
        self.mode2.resize(91, 21)
        self.mode2.move(70, 140)

        self.start_butt = QPushButton('Start', self.window)
        self.start_butt.resize(101, 61)
        self.start_butt.move(10, 180)
        self.start_butt.clicked.connect(self.start)

        self.stop_butt = QPushButton('Stop', self.window)
        self.stop_butt.resize(101, 61)
        self.stop_butt.move(130, 180)
        self.stop_butt.clicked.connect(self.stop)

        self.setting_butt = QPushButton(self.window)
        self.setting_butt.resize(31, 31)
        self.setting_butt.move(210, 0)
        self.setting_butt.setIcon(QIcon('picture/setting_butt.png'))
        self.setting_butt.setIconSize(QSize(32, 32))
        self.setting_butt.clicked.connect(self.open_setting)
        self.setting_butt.setStyleSheet('QPushButton{border: 0px solid #555;'
                                        'border-style: outset;'
                                        'background: rgb(238, 238, 238);'
                                        'padding: 5px;}'
                                        'QPushButton:hover{'
                                        'border: 1px solid rgb(197, 197, 197);'
                                        'border-style: outset;'
                                        'background: rgb(223, 223, 223);'
                                        'padding: 5px;}'
                                        'QPushButton:pressed {'
                                        'border-style: inset;'
                                        'background: qradialgradient(cx: 0.4, cy: -0.1, '
                                        'fx: 0.4, fy: -0.1,radius: 1.35, '
                                        'stop: 0 #fff, stop: 1 #ddd);}')

        # self.host_check_box = QCheckBox('Not host', self.window)
        # self.host_check_box.move(160, 110)
        # self.host_check_box.resize(81, 21)

        self.setting_window = Setting()

    def start(self) -> None:
        """ Start playing game.
        """
        if self.mode1.isChecked():
            # Creating a new thread to run the loop
            # for avoiding not responding window
            self.start_butt.setEnabled(False)
            # Ver 1.3
            # if self.host_check_box.isChecked():
            #     thread1 = Thread(target=run_and_surr_party, args=(time_between_games, surr_time,),
            #                      daemon=True)
            #     thread1.start()
            # else:
            #     thread1 = Thread(target=run_and_surr, args=(time_between_games, surr_time,),
            #                      daemon=True)
            #     thread2 = Thread(target=self.record, daemon=True)
            #     thread1.start()
            #     thread2.start()
            thread1 = Thread(target=run_and_surr, args=(time_between_games, surr_time,),
                             daemon=True)
            thread2 = Thread(target=self.record, daemon=True)
            thread1.start()
            thread2.start()

        elif self.mode2.isChecked():
            # QMessageBox.about(self.window, 'Notification', 'Coming soon...')
            self.start_butt.setEnabled(False)
            thread1 = Thread(target=auto_pick,
                             args=(champ_set, time_between_games,), daemon=True)
            thread2 = Thread(target=self.record, daemon=True)
            thread1.start()
            thread2.start()

    def stop(self) -> None:
        """ Stop the bot.
        """
        print('Bot stopping...')
        exit(0)

    def record(self) -> None:
        """Record the number of played games.
        """
        record_num = 0
        while True:
            if exist('picture/find_match.png', printability=False):
                record_num += 1
                print('!!!Played Games + 1!!!')
                self.game_his_lcd.display(record_num)
                time.sleep(1)

    def open_setting(self) -> None:
        """ Open setting window
        """
        self.setting_window.window.show()


class Setting:
    """Ui of setting.
    """

    def __init__(self) -> None:
        """Initialize Ui
        """
        self.font1 = QFont()
        self.font1.setFamily('Calibri')
        self.font1.setPointSize(12)

        self.font1_bold = QFont()
        self.font1_bold.setFamily('Calibri')
        self.font1_bold.setBold(True)
        self.font1_bold.setPointSize(12)

        self.window = QWidget()
        self.window.resize(400, 325)
        self.window.setFont(self.font1)
        self.window.setStyleSheet('QPushButton{border: 2px solid rgb(152, 152, 152);'
                                  'border-radius: 15px;}'
                                  'QPushButton:hover{border: 2px solid rgb(226, 226, 226);'
                                  'background: rgb(223, 223, 223);'
                                  'border-radius: 15px;}'
                                  'QPushButton:pressed {border: 2px solid rgb(152, 152, 152);'
                                  'background: rgb(231, 231, 231);'
                                  'border-radius: 15px;}'
                                  'QLineEdit{border: 1px solid rgb(231, 231, 231);'
                                  'border-radius: 10px;'
                                  'background:rgb(250, 250, 250);'
                                  'padding-left: 3px;}'
                                  'QLineEdit:hover{border: 1px solid rgb(206, 206, 206);'
                                  'border-radius: 10px;}'
                                  'QLineEdit:focus{border: 1px solid rgb(85, 170, 255);'
                                  'border-radius: 10px;}'
                                  'QPlainTextEdit{border: 1px solid rgb(231, 231, 231);'
                                  'border-radius: 10px;'
                                  'background:rgb(250, 250, 250);'
                                  'padding-left: 3px;}'
                                  'QPlainTextEdit:hover{border: 1px solid rgb(206, 206, 206);'
                                  'border-radius: 10px;}'
                                  'QPlainTextEdit:focus{border: 1px solid rgb(85, 170, 255);'
                                  'border-radius: 10px;}')

        self.label1 = QLabel('Time between games:', self.window)
        self.label1.resize(151, 41)
        self.label1.move(20, 10)

        self.label2 = QLabel('Build list:', self.window)
        self.label2.resize(91, 31)
        self.label2.move(20, 90)

        self.surr_time_label = QLabel('Surrender time:', self.window)
        self.surr_time_label.resize(151, 41)
        self.surr_time_label.move(20, 40)

        self.second_label = QLabel('sec', self.window)
        self.second_label.resize(21, 21)
        self.second_label.move(215, 20)

        self.second_label2 = QLabel('sec', self.window)
        self.second_label2.resize(21, 21)
        self.second_label2.move(175, 50)

        self.time_interval_line = QLineEdit(self.window)
        self.time_interval_line.resize(31, 21)
        self.time_interval_line.move(180, 20)
        self.time_interval_line.setText(str(time_between_games))

        self.surr_time_line = QLineEdit(self.window)
        self.surr_time_line.resize(31, 21)
        self.surr_time_line.move(140, 50)
        self.surr_time_line.setText(str(surr_time))

        self.build_list_text = QPlainTextEdit(self.window)
        self.build_list_text.resize(271, 191)
        self.build_list_text.move(20, 120)
        self.build_list_text.setPlaceholderText(
            'Please enter your build list (ex. gragas_1, kindred_5, ...)')

        self.save_butt = QPushButton('Save', self.window)
        self.save_butt.resize(81, 31)
        self.save_butt.move(300, 280)
        self.save_butt.clicked.connect(self.save_text)

    def save_text(self) -> None:
        """ Save the text from time_interval_line and build_list_text.
        """
        temp_line = self.time_interval_line.text()
        temp_line2 = self.surr_time_line.text()
        temp_text = self.build_list_text.toPlainText()

        if temp_line is not None and temp_line.isdigit():
            global time_between_games
            time_between_games = int(temp_line)
            print('\'Time between games\' save successfully!!!')
        else:
            print('The \'Time between games\' should be a integer number.')

        if temp_line2 is not None and temp_line2.isdigit():
            global surr_time
            surr_time = int(temp_line2)
            print('\'Surrender time\' save successfully!!!')
        else:
            print('The \'Surrender time\' should be a integer number.')

        if temp_text != '':
            temp = temp_text.strip()
            temp_result = set()
            global champ_set
            for champ in temp.split(','):
                temp_result.add(champ.strip())
            champ_set = temp_result
            print('Your build list save successfully!!!')


def run() -> None:
    """Run the TFT bot.
    """
    app = QApplication([])
    bot = Bot()
    bot.window.show()
    app.exec_()


def show_setting() -> None:
    """Show the setting window
    """
    app = QApplication([])
    setting = Setting()
    setting.window.show()
    app.exec_()


# test_set = {'abc', 'a', 'b'}
# test_int = 5
#
# test_thread = Thread(target=test, args=(test_set, test_int,))
# test_thread.start()
