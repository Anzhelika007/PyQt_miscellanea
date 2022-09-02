from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot

from ui.base_qt_ui.ui_mainWindow import Ui_MainWindow
from ui.coordwidget import CoordWidget
# второй рукописный
from ui.flowlayout import FlowLayout

# тип главного объекта QMainWindow - его наследуем
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # переменная класса экземпляра интовского типа, которая при добавлении виджета лойаута будет увеличиваться и добавлять id каждому виджету
        self.counter_id: int = 0

        #---------------------------------------------
        # создаем переменную с классом
        self.flowlaout = FlowLayout()


        #----------------------------------------------


        # связываем кнопки со слотами
        self.ui.add_pushButton.clicked.connect(self.add_coordwidget)
        self.ui.clear_pushButton.clicked.connect(self.clear_area)

    @Slot()
    # 1 слот - отвечает за добавление виджета
    def add_coordwidget(self):
        # увеличиваем значение id
        self.counter_id += 1
        # создаем экземпляр класса виджета координат (второго!) и присваиваем id
        coord_widget = CoordWidget(self.counter_id)
        # добавляем на наше основное окно
        self.ui.coordWidget_layout.addWidget(coord_widget)
        # связали сигнал со слотом кнопки удалить
        coord_widget.delete.connect(self.delete_coordwidget)


    @Slot()
    # 2 слот - отвечает за очистку окна от всех виджетов координат
    def clear_area(self):
        while self.ui.coordWidget_layout.count() > 0:
            # пробежались по всем виджетам получили ссылку и удалили
            item = self.ui.coordWidget_layout.takeAt(0)
            item.widget().deleteLater()

    @Slot(int)
    # 3 слот - отвечает за удаление одного виджета. Мы получаем инт значение из слота файла coordwidget
    def delete_coordwidget(self, wid: int):
        print(f'Удаляемый виджет с id: {wid}')
        widget = self.sender()
        self.ui.coordWidget_layout.removeWidget(widget)
        widget.deleteLater()
