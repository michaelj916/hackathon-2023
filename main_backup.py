

from PyQt5 import QtCore, QtGui, QtWidgets
from function_nagivation import Nagivation
from storeData import AddData
from readData import ReadData

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 700)
        MainWindow.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.side_menu_bar_label = QtWidgets.QLabel(self.centralwidget)
        self.side_menu_bar_label.setGeometry(QtCore.QRect(10, 10, 91, 681))
        self.side_menu_bar_label.setStyleSheet("border-radius: 15px;\n"
                                               "background-color: rgb(234, 234, 234);")
        self.side_menu_bar_label.setText("")
        self.side_menu_bar_label.setObjectName("side_menu_bar_label")

        self.menu_title1 = QtWidgets.QLabel(self.centralwidget)
        self.menu_title1.setGeometry(QtCore.QRect(20, 370, 71, 31))
        self.menu_title1.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                       "font-weight: bold;\n"
                                       "color: rgb(149, 149, 149);\n"
                                       "background-color: rgb(234, 234, 234);")
        self.menu_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_title1.setObjectName("menu_title1")

        self.schooltitle2 = QtWidgets.QLabel(self.centralwidget)
        self.schooltitle2.setGeometry(QtCore.QRect(20, 460, 71, 31))
        self.schooltitle2.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                         "font-weight: bold;\n"
                                         "color: rgb(149, 149, 149);\n"
                                         "background-color: rgb(234, 234, 234);")
        self.schooltitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.schooltitle2.setObjectName("menu_title2")



        self.work_title1 = QtWidgets.QLabel(self.centralwidget)
        self.work_title1.setGeometry(QtCore.QRect(20, 550, 71, 31))
        self.work_title1.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                       "font-weight: bold;\n"
                                       "color: rgb(149, 149, 149);\n"
                                       "background-color: rgb(234, 234, 234);")
        self.work_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.work_title1.setObjectName("work_title1")

        self.todo_title1 = QtWidgets.QLabel(self.centralwidget)
        self.todo_title1.setGeometry(QtCore.QRect(20, 120, 71, 31))
        self.todo_title1.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                       "font-weight: bold;\n"
                                       "color: rgb(149, 149, 149);\n"
                                       "background-color: rgb(234, 234, 234);")
        self.todo_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_title1.setObjectName("todo_title1")

        self.completed_title1 = QtWidgets.QLabel(self.centralwidget)
        self.completed_title1.setGeometry(QtCore.QRect(20, 650, 71, 31))
        self.completed_title1.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                            "font-weight: bold;\n"
                                            "color: rgb(149, 149, 149);\n"
                                            "background-color: rgb(234, 234, 234);")
        self.completed_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.completed_title1.setObjectName("completed_title1")

        self.important_title1 = QtWidgets.QLabel(self.centralwidget)
        self.important_title1.setGeometry(QtCore.QRect(20, 220, 71, 31))
        self.important_title1.setStyleSheet("font: 8pt \"Century Gothic\";\n"
                                            "font-weight: bold;\n"
                                            "color: rgb(149, 149, 149);\n"
                                            "background-color: rgb(234, 234, 234);")
        self.important_title1.setAlignment(QtCore.Qt.AlignCenter)
        self.important_title1.setObjectName("important_title1")

        self.menu_title = QtWidgets.QLabel(self.centralwidget)
        self.menu_title.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.menu_title.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                      "font-weight: bold;\n"
                                      "background-color: rgb(234, 234, 234);\n"
                                      "color: rgb(149, 149, 149);")
        self.menu_title.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_title.setObjectName("menu_title")




        self.home_todo = QtWidgets.QPushButton(self.centralwidget)
        self.home_todo.setGeometry(QtCore.QRect(30, 340, 51, 41))
        self.home_todo.setStyleSheet("\n"
                                     "QPushButton {\n"
                                     "background-color: rgb(234, 234, 234);\n"
                                     "    border: 0px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     "}\n"
                                     "    \n"
                                     "QPushButton:pressed {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     " }")
        self.home_todo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/home.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.home_todo.setIcon(icon)
        self.home_todo.setIconSize(QtCore.QSize(30, 30))
        self.home_todo.setObjectName("home_todo")

        self.school_todo = QtWidgets.QPushButton(self.centralwidget)
        self.school_todo.setGeometry(QtCore.QRect(30, 430, 51, 41))
        self.school_todo.setStyleSheet("\n"
                                       "QPushButton {\n"
                                       "background-color: rgb(234, 234, 234);\n"
                                       "    border: 0px;\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 0px;\n"
                                       "}\n"
                                       "    \n"
                                       "QPushButton:pressed {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 0px;\n"
                                       " }")
        self.school_todo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/open-book.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.school_todo.setIcon(icon1)
        self.school_todo.setIconSize(QtCore.QSize(35, 35))
        self.school_todo.setObjectName("school_todo")
        self.todo = QtWidgets.QPushButton(self.centralwidget)
        self.todo.setGeometry(QtCore.QRect(30, 90, 51, 41))
        self.todo.setStyleSheet("\n"
                                "QPushButton {\n"
                                "background-color: rgb(234, 234, 234);\n"
                                "    border: 0px;\n"
                                "    border-radius: 5px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "        \n"
                                "    background-color: rgb(199, 199, 199);\n"
                                "    border-radius: 5px;\n"
                                "    border: 0px;\n"
                                "}\n"
                                "    \n"
                                "QPushButton:pressed {\n"
                                "        \n"
                                "    background-color: rgb(199, 199, 199);\n"
                                "    border-radius: 5px;\n"
                                "    border: 0px;\n"
                                " }")
        self.todo.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/menu (4).png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.todo.setIcon(icon2)
        self.todo.setIconSize(QtCore.QSize(30, 30))
        self.todo.setObjectName("todo")
        self.task_title = QtWidgets.QLabel(self.centralwidget)
        self.task_title.setGeometry(QtCore.QRect(10, 280, 91, 31))
        self.task_title.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                      "font-weight: bold;\n"
                                      "background-color: rgb(234, 234, 234);\n"
                                      "color: rgb(149, 149, 149);")
        self.task_title.setAlignment(QtCore.Qt.AlignCenter)
        self.task_title.setObjectName("task_title")
        self.work_todo = QtWidgets.QPushButton(self.centralwidget)
        self.work_todo.setGeometry(QtCore.QRect(30, 520, 51, 41))
        self.work_todo.setStyleSheet("\n"
                                     "QPushButton {\n"
                                     "background-color: rgb(234, 234, 234);\n"
                                     "    border: 0px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     "}\n"
                                     "    \n"
                                     "QPushButton:pressed {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     " }")
        self.work_todo.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/suitcase.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.work_todo.setIcon(icon3)
        self.work_todo.setIconSize(QtCore.QSize(35, 35))
        self.work_todo.setObjectName("work_todo")
        self.menu_screens = QtWidgets.QTabWidget(self.centralwidget)
        self.menu_screens.setGeometry(QtCore.QRect(110, 10, 641, 721))
        self.menu_screens.setStyleSheet("border: 0px;")
        self.menu_screens.setTabPosition(QtWidgets.QTabWidget.South)
        self.menu_screens.setObjectName("menu_screens")
        self.todolist = QtWidgets.QWidget()
        self.todolist.setObjectName("todolist")
        self.today_label = QtWidgets.QLabel(self.todolist)
        self.today_label.setGeometry(QtCore.QRect(20, 10, 161, 51))
        self.today_label.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                       "font-weight: bold;\n"
                                       "color: rgb(112, 112, 112);")
        self.today_label.setObjectName("today_label")
        self.counter_todo = QtWidgets.QLabel(self.todolist)
        self.counter_todo.setGeometry(QtCore.QRect(130, 17, 51, 41))
        self.counter_todo.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.counter_todo.setObjectName("counter_todo")
        self.counter_todo.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_addtask = QtWidgets.QLineEdit(self.todolist)
        self.todo_addtask.setGeometry(QtCore.QRect(10, 70, 541, 51))
        self.todo_addtask.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.todo_addtask.setObjectName("todo_addtask")
        self.todo_submit = QtWidgets.QPushButton(self.todolist)
        self.todo_submit.setGeometry(QtCore.QRect(560, 70, 51, 51))
        self.todo_submit.setStyleSheet("\n"
                                       "QPushButton {\n"
                                       "background-color: rgb(234, 234, 234);\n"
                                       "    border: 0px;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       "}\n"
                                       "    \n"
                                       "QPushButton:pressed {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       " }")
        self.todo_submit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/plus.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.todo_submit.setIcon(icon4)
        self.todo_submit.setIconSize(QtCore.QSize(30, 30))
        self.todo_submit.setObjectName("todo_submit")


        self.todo_list_widget = QtWidgets.QListWidget(self.todolist)
        self.todo_list_widget.setGeometry(QtCore.QRect(10, 150, 611, 521))
        self.todo_list_widget.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                            "")
        self.todo_list_widget.setProperty("isWrapping", False)
        self.todo_list_widget.setObjectName("todo_list_widget")
        item = QtWidgets.QListWidgetItem()
        self.todo_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.todo_list_widget.addItem(item)


        self.doubleclicklabel = QtWidgets.QLabel(self.todolist)
        self.doubleclicklabel.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.doubleclicklabel.setStyleSheet("font: 10\n"
                                            "pt \"Century Gothic\";\n"
                                            "color: rgb(112, 112, 112);")
        self.doubleclicklabel.setObjectName("doubleclicklabel")
        self.background_label = QtWidgets.QLabel(self.todolist)
        self.background_label.setGeometry(QtCore.QRect(10, -20, 611, 151))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\istockphoto-679896446-612x612.jpeg"))
        self.background_label.setScaledContents(False)
        self.background_label.setObjectName("background_label")
        self.background_label.raise_()
        self.today_label.raise_()
        self.counter_todo.raise_()
        self.todo_addtask.raise_()
        self.todo_submit.raise_()
        self.todo_list_widget.raise_()
        self.doubleclicklabel.raise_()
        self.menu_screens.addTab(self.todolist, "")
        self.important_2 = QtWidgets.QWidget()
        self.important_2.setObjectName("important_2")
        self.stickypad_todo = QtWidgets.QListWidget(self.important_2)
        self.stickypad_todo.setGeometry(QtCore.QRect(10, 70, 611, 601))
        self.stickypad_todo.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                          "")
        self.stickypad_todo.setObjectName("stickypad_todo")
        item = QtWidgets.QListWidgetItem()
        self.stickypad_todo.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.stickypad_todo.addItem(item)
        self.completed_label_2 = QtWidgets.QLabel(self.important_2)
        self.completed_label_2.setGeometry(QtCore.QRect(0, 0, 631, 51))
        self.completed_label_2.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                             "font-weight: bold;\n"
                                             "color: rgb(112, 112, 112);\n"
                                             "background-color: rgb(226, 226, 226);\n"
                                             "border-radius: 10px;")
        self.completed_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.completed_label_2.setObjectName("completed_label_2")
        self.menu_screens.addTab(self.important_2, "")
        self.home_todo1 = QtWidgets.QWidget()
        self.home_todo1.setObjectName("home_todo1")
        self.home_label = QtWidgets.QLabel(self.home_todo1)
        self.home_label.setGeometry(QtCore.QRect(20, 10, 201, 51))
        self.home_label.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                      "font-weight: bold;\n"
                                      "color: rgb(112, 112, 112);")
        self.home_label.setObjectName("home_label")
        self.home_submit = QtWidgets.QPushButton(self.home_todo1)
        self.home_submit.setGeometry(QtCore.QRect(560, 70, 51, 51))
        self.home_submit.setStyleSheet("\n"
                                       "QPushButton {\n"
                                       "background-color: rgb(234, 234, 234);\n"
                                       "    border: 0px;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       "}\n"
                                       "    \n"
                                       "QPushButton:pressed {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       " }")
        self.home_submit.setText("")
        self.home_submit.setIcon(icon4)
        self.home_submit.setIconSize(QtCore.QSize(30, 30))
        self.home_submit.setObjectName("home_submit")
        self.home_counter = QtWidgets.QLabel(self.home_todo1)
        self.home_counter.setGeometry(QtCore.QRect(230, 17, 51, 41))
        self.home_counter.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.home_counter.setObjectName("home_counter")
        self.home_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.home_list_widget = QtWidgets.QListWidget(self.home_todo1)
        self.home_list_widget.setGeometry(QtCore.QRect(10, 150, 611, 521))
        self.home_list_widget.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                            "")
        self.home_list_widget.setObjectName("home_list_widget")
        item = QtWidgets.QListWidgetItem()
        self.home_list_widget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.home_list_widget.addItem(item)
        self.home_addtask = QtWidgets.QLineEdit(self.home_todo1)
        self.home_addtask.setGeometry(QtCore.QRect(10, 70, 541, 51))
        self.home_addtask.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.home_addtask.setObjectName("home_addtask")
        self.label = QtWidgets.QLabel(self.home_todo1)
        self.label.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.label.setStyleSheet("font: 10\n"
                                 "pt \"Century Gothic\";\n"
                                 "color: rgb(112, 112, 112);")
        self.label.setObjectName("label")
        self.school_label_background_2 = QtWidgets.QLabel(self.home_todo1)
        self.school_label_background_2.setGeometry(QtCore.QRect(10, -10, 611, 151))
        self.school_label_background_2.setText("")
        self.school_label_background_2.setPixmap(
            QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\istockphoto-679896446-612x612.jpeg"))
        self.school_label_background_2.setObjectName("school_label_background_2")
        self.school_label_background_2.raise_()
        self.home_label.raise_()
        self.home_submit.raise_()
        self.home_counter.raise_()
        self.home_list_widget.raise_()
        self.home_addtask.raise_()
        self.label.raise_()
        self.menu_screens.addTab(self.home_todo1, "")
        self.school_todo1 = QtWidgets.QWidget()
        self.school_todo1.setObjectName("school_todo1")
        self.school_addtask = QtWidgets.QLineEdit(self.school_todo1)
        self.school_addtask.setGeometry(QtCore.QRect(10, 70, 541, 51))
        self.school_addtask.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                          "color: rgb(112, 112, 112);\n"
                                          "border: 3px solid rgb(214, 214, 214) ;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 5px;")
        self.school_addtask.setObjectName("school_addtask")
        self.school_submit = QtWidgets.QPushButton(self.school_todo1)
        self.school_submit.setGeometry(QtCore.QRect(560, 70, 51, 51))
        self.school_submit.setStyleSheet("\n"
                                         "QPushButton {\n"
                                         "background-color: rgb(234, 234, 234);\n"
                                         "    border: 0px;\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "        \n"
                                         "    background-color: rgb(199, 199, 199);\n"
                                         "    order-radius: 10px;\n"
                                         "    border: 0px;\n"
                                         "}\n"
                                         "    \n"
                                         "QPushButton:pressed {\n"
                                         "        \n"
                                         "    background-color: rgb(199, 199, 199);\n"
                                         "    order-radius: 10px;\n"
                                         "    border: 0px;\n"
                                         " }")
        self.school_submit.setText("")
        self.school_submit.setIcon(icon4)
        self.school_submit.setIconSize(QtCore.QSize(30, 30))
        self.school_submit.setObjectName("school_submit")
        self.doubleclick_label = QtWidgets.QLabel(self.school_todo1)
        self.doubleclick_label.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.doubleclick_label.setStyleSheet("font: 10\n"
                                             "pt \"Century Gothic\";\n"
                                             "color: rgb(112, 112, 112);")
        self.doubleclick_label.setObjectName("doubleclick_label")
        self.school_label = QtWidgets.QLabel(self.school_todo1)
        self.school_label.setGeometry(QtCore.QRect(20, 10, 201, 51))
        self.school_label.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                        "font-weight: bold;\n"
                                        "color: rgb(112, 112, 112);")
        self.school_label.setObjectName("school_label")
        self.school_counter = QtWidgets.QLabel(self.school_todo1)
        self.school_counter.setGeometry(QtCore.QRect(230, 17, 51, 41))
        self.school_counter.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                          "color: rgb(112, 112, 112);\n"
                                          "border: 3px solid rgb(214, 214, 214) ;\n"
                                          "border-width: 2px;\n"
                                          "border-radius: 5px;")
        self.school_counter.setObjectName("school_counter")
        self.school_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.school_lists = QtWidgets.QListWidget(self.school_todo1)
        self.school_lists.setGeometry(QtCore.QRect(10, 150, 611, 521))
        self.school_lists.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                        "")
        self.school_lists.setObjectName("school_lists")
        item = QtWidgets.QListWidgetItem()
        self.school_lists.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.school_lists.addItem(item)
        self.school_label_background = QtWidgets.QLabel(self.school_todo1)
        self.school_label_background.setGeometry(QtCore.QRect(10, -10, 611, 151))
        self.school_label_background.setText("")
        self.school_label_background.setPixmap(
            QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\istockphoto-679896446-612x612.jpeg"))
        self.school_label_background.setObjectName("school_label_background")
        self.school_label_background.raise_()
        self.school_addtask.raise_()
        self.school_submit.raise_()
        self.doubleclick_label.raise_()
        self.school_label.raise_()
        self.school_counter.raise_()
        self.school_lists.raise_()
        self.menu_screens.addTab(self.school_todo1, "")
        self.work_todo1 = QtWidgets.QWidget()
        self.work_todo1.setObjectName("work_todo1")
        self.work_lists = QtWidgets.QListWidget(self.work_todo1)
        self.work_lists.setGeometry(QtCore.QRect(10, 150, 611, 521))
        self.work_lists.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                      "")
        self.work_lists.setObjectName("work_lists")
        item = QtWidgets.QListWidgetItem()
        self.work_lists.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.work_lists.addItem(item)
        self.work_addtask = QtWidgets.QLineEdit(self.work_todo1)
        self.work_addtask.setGeometry(QtCore.QRect(10, 70, 541, 51))
        self.work_addtask.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.work_addtask.setObjectName("work_addtask")
        self.work_submit = QtWidgets.QPushButton(self.work_todo1)
        self.work_submit.setGeometry(QtCore.QRect(560, 70, 51, 51))
        self.work_submit.setStyleSheet("\n"
                                       "QPushButton {\n"
                                       "background-color: rgb(234, 234, 234);\n"
                                       "    border: 0px;\n"
                                       "    border-radius: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       "}\n"
                                       "    \n"
                                       "QPushButton:pressed {\n"
                                       "        \n"
                                       "    background-color: rgb(199, 199, 199);\n"
                                       "    order-radius: 10px;\n"
                                       "    border: 0px;\n"
                                       " }")
        self.work_submit.setText("")
        self.work_submit.setIcon(icon4)
        self.work_submit.setIconSize(QtCore.QSize(30, 30))
        self.work_submit.setObjectName("work_submit")
        self.work_label = QtWidgets.QLabel(self.work_todo1)
        self.work_label.setGeometry(QtCore.QRect(20, 10, 201, 51))
        self.work_label.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                      "font-weight: bold;\n"
                                      "color: rgb(112, 112, 112);")
        self.work_label.setObjectName("work_label")
        self.doublelabel3 = QtWidgets.QLabel(self.work_todo1)
        self.doublelabel3.setGeometry(QtCore.QRect(10, 120, 321, 16))
        self.doublelabel3.setStyleSheet("font: 10\n"
                                        "pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);")
        self.doublelabel3.setObjectName("doublelabel3")
        self.work_counter = QtWidgets.QLabel(self.work_todo1)
        self.work_counter.setGeometry(QtCore.QRect(230, 17, 51, 41))
        self.work_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.work_counter.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                        "color: rgb(112, 112, 112);\n"
                                        "border: 3px solid rgb(214, 214, 214) ;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 5px;")
        self.work_counter.setObjectName("work_counter")
        self.work_background = QtWidgets.QLabel(self.work_todo1)
        self.work_background.setGeometry(QtCore.QRect(10, -10, 611, 151))
        self.work_background.setText("")
        self.work_background.setPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/computer.png"))
        self.work_background.setScaledContents(False)
        self.work_background.setObjectName("work_background")
        self.work_background.raise_()
        self.work_lists.raise_()
        self.work_addtask.raise_()
        self.work_submit.raise_()
        self.work_label.raise_()
        self.doublelabel3.raise_()
        self.work_counter.raise_()
        self.menu_screens.addTab(self.work_todo1, "")
        self.completedtodo = QtWidgets.QWidget()
        self.completedtodo.setObjectName("completedtodo")
        self.completed_tasks = QtWidgets.QListWidget(self.completedtodo)
        self.completed_tasks.setGeometry(QtCore.QRect(10, 70, 621, 601))
        self.completed_tasks.setStyleSheet("text-decoration: line-through;\n"
                                           "font: 15pt \"Century Gothic\";\n"
                                           "color: rgb(121, 121, 121);")
        self.completed_tasks.setObjectName("completed_tasks")
        item = QtWidgets.QListWidgetItem()
        self.completed_tasks.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.completed_tasks.addItem(item)
        self.completed_label = QtWidgets.QLabel(self.completedtodo)
        self.completed_label.setGeometry(QtCore.QRect(0, 0, 631, 51))
        self.completed_label.setStyleSheet("font: 20pt \"Century Gothic\";\n"
                                           "font-weight: bold;\n"
                                           "color: rgb(112, 112, 112);\n"
                                           "background-color: rgb(226, 226, 226);\n"
                                           "border-radius: 10px;")
        self.completed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.completed_label.setObjectName("completed_label")

        self.menu_screens.addTab(self.completedtodo, "")
        self.important = QtWidgets.QPushButton(self.centralwidget)
        self.important.setGeometry(QtCore.QRect(30, 190, 51, 41))
        self.important.setStyleSheet("\n"
                                     "QPushButton {\n"
                                     "background-color: rgb(234, 234, 234);\n"
                                     "    border: 0px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     "}\n"
                                     "    \n"
                                     "QPushButton:pressed {\n"
                                     "        \n"
                                     "    background-color: rgb(199, 199, 199);\n"
                                     "    border-radius: 5px;\n"
                                     "    border: 0px;\n"
                                     " }")
        self.important.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/star.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.important.setIcon(icon5)
        self.important.setIconSize(QtCore.QSize(40, 40))
        self.important.setObjectName("important")
        self.completed_todo = QtWidgets.QPushButton(self.centralwidget)
        self.completed_todo.setGeometry(QtCore.QRect(30, 620, 51, 41))
        self.completed_todo.setStyleSheet("\n"
                                          "QPushButton {\n"
                                          "background-color: rgb(234, 234, 234);\n"
                                          "    border: 0px;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "        \n"
                                          "    background-color: rgb(199, 199, 199);\n"
                                          "    border-radius: 5px;\n"
                                          "    border: 0px;\n"
                                          "}\n"
                                          "    \n"
                                          "QPushButton:pressed {\n"
                                          "        \n"
                                          "    background-color: rgb(199, 199, 199);\n"
                                          "    border-radius: 5px;\n"
                                          "    border: 0px;\n"
                                          " }")
        self.completed_todo.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:\\Users\\mikab\\Desktop\\../Downloads/check.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.completed_todo.setIcon(icon6)
        self.completed_todo.setIconSize(QtCore.QSize(35, 35))

        self.completed_todo.setObjectName("completed_todo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_screens.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ================================== Side Bar Navigation =====================================================
        nav = Nagivation()
        self.todo.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 0))
        self.important.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 1))
        self.home_todo.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 2))
        self.school_todo.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 3))
        self.work_todo.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 4))
        self.completed_todo.clicked.connect(lambda x: nav.change_screen(self.menu_screens, 5))

        # ======================================Add Item ===============================================
        add_task = AddData()
        self.todo_submit.clicked.connect(lambda x: add_task.write_todo(self.todo_addtask.text(), self.todo_list_widget, self.counter_todo, self.todo_addtask, 'ToDo-Datas'))
        self.home_submit.clicked.connect(lambda x: add_task.write_todo(self.home_addtask.text(), self.home_list_widget, self.home_counter, self.home_addtask, 'ToDo-Datas-Home'))
        self.school_submit.clicked.connect(lambda x: add_task.write_todo(self.school_addtask.text(), self.school_lists, self.school_counter, self.school_addtask, 'ToDo-Datas-School'))
        self.work_submit.clicked.connect(lambda x: add_task.write_todo(self.work_addtask.text(), self.work_lists, self.work_counter, self.work_addtask, 'ToDo-Datas-Work'))


        # ====================================== Pre - Read Item ===============================================

        ReadData.read_todo(self.todo_list_widget, 'ToDo-Datas')
        ReadData.read_todo(self.home_list_widget, 'ToDo-Datas-Home')
        ReadData.read_todo(self.school_lists, 'ToDo-Datas-School')
        ReadData.read_todo(self.work_lists, 'ToDo-Datas-Work')



        self.counter_todo.setText(str(self.todo_list_widget.count()))
        self.home_counter.setText(str(self.home_list_widget.count()))
        self.school_counter.setText(str(self.school_lists.count()))
        self.work_counter.setText(str(self.work_lists.count()))

        # ====================================== Pre - Read Item ===============================================

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_title.setText(_translate("MainWindow", "Menu"))
        self.menu_title1.setText(_translate("MainWindow",'Menu'))
        self.task_title.setText(_translate("MainWindow", "Tasks"))
        self.today_label.setText(_translate("MainWindow", "Today"))
        self.todo_addtask.setPlaceholderText(_translate("MainWindow", "  Add New Task"))
        __sortingEnabled = self.todo_list_widget.isSortingEnabled()
        self.todo_list_widget.setSortingEnabled(False)
        item = self.todo_list_widget.item(0)
        item.setText(_translate("MainWindow", "• Banana"))
        item = self.todo_list_widget.item(1)
        item.setText(_translate("MainWindow", "• Apple"))
        self.todo_list_widget.setSortingEnabled(__sortingEnabled)
        self.doubleclicklabel.setText(_translate("MainWindow", "Double click to mark as completed."))
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.todolist), _translate("MainWindow", "todolist"))
        __sortingEnabled = self.stickypad_todo.isSortingEnabled()
        self.stickypad_todo.setSortingEnabled(False)
        item = self.stickypad_todo.item(0)
        item.setText(_translate("MainWindow", "☆ Apple"))
        item = self.stickypad_todo.item(1)
        item.setText(_translate("MainWindow", "☆ Banana"))
        self.stickypad_todo.setSortingEnabled(__sortingEnabled)
        self.completed_label_2.setText(_translate("MainWindow", "Important Tasks"))
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.important_2),
                                     _translate("MainWindow", "stickytodo"))
        self.home_label.setText(_translate("MainWindow", "Home Tasks"))
        self.home_counter.setText(_translate("MainWindow", "0"))
        __sortingEnabled = self.home_list_widget.isSortingEnabled()
        self.home_list_widget.setSortingEnabled(False)
        item = self.home_list_widget.item(0)
        item.setText(_translate("MainWindow", "• Apple"))
        item = self.home_list_widget.item(1)
        item.setText(_translate("MainWindow", "• Banana"))
        self.home_list_widget.setSortingEnabled(__sortingEnabled)
        self.home_addtask.setPlaceholderText(_translate("MainWindow", "  Add Home Task"))
        self.label.setText(_translate("MainWindow", "Double click to mark as completed."))
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.home_todo1), _translate("MainWindow", "home_todo"))
        self.school_addtask.setPlaceholderText(_translate("MainWindow", "  Add Home Task"))
        self.doubleclick_label.setText(_translate("MainWindow", "Double click to mark as completed."))
        self.school_label.setText(_translate("MainWindow", "School Tasks"))
        self.school_counter.setText(_translate("MainWindow", "0"))
        __sortingEnabled = self.school_lists.isSortingEnabled()
        self.school_lists.setSortingEnabled(False)
        item = self.school_lists.item(0)
        item.setText(_translate("MainWindow", "• Apple"))
        item = self.school_lists.item(1)
        item.setText(_translate("MainWindow", "• Banana"))
        self.school_lists.setSortingEnabled(__sortingEnabled)
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.school_todo1),
                                     _translate("MainWindow", "school_todo"))
        __sortingEnabled = self.work_lists.isSortingEnabled()
        self.work_lists.setSortingEnabled(False)
        item = self.work_lists.item(0)
        item.setText(_translate("MainWindow", "• Apple"))
        item = self.work_lists.item(1)
        item.setText(_translate("MainWindow", "• Banana"))
        self.work_lists.setSortingEnabled(__sortingEnabled)
        self.work_addtask.setPlaceholderText(_translate("MainWindow", "  Add Home Task"))
        self.work_label.setText(_translate("MainWindow", "Work Tasks"))
        self.doublelabel3.setText(_translate("MainWindow", "Double click to mark as completed."))
        self.work_counter.setText(_translate("MainWindow", "0"))
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.work_todo1), _translate("MainWindow", "work_todo"))
        __sortingEnabled = self.completed_tasks.isSortingEnabled()
        self.completed_tasks.setSortingEnabled(False)
        item = self.completed_tasks.item(0)
        item.setText(_translate("MainWindow", "Apple"))
        item = self.completed_tasks.item(1)
        item.setText(_translate("MainWindow", "Banana"))
        self.completed_tasks.setSortingEnabled(__sortingEnabled)
        self.completed_label.setText(_translate("MainWindow", "Completed Tasks"))
        self.menu_screens.setTabText(self.menu_screens.indexOf(self.completedtodo),
                                     _translate("MainWindow", "completedtodo"))
        self.schooltitle2.setText(_translate("MainWindow", "School"))
        self.work_title1.setText(_translate("MainWindow", "Work"))
        self.todo_title1.setText(_translate("MainWindow", "To-Do"))
        self.important_title1.setText(_translate("MainWindow",'Important'))
        self.completed_title1.setText(_translate("MainWindow", "Completed"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
