from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.base_qt_ui.ui_coordWidget import Ui_CoordWidget


# наследует от типа объекта (QWidget)
class CoordWidget(QWidget):
    # пробрасываем сигнал удаления (если кнопка нажата- виджет удалится, передаем интовское значение!!!)
    delete = Signal(int)

    def __init__(self, id_widget: int, parent=None):
        super(CoordWidget, self).__init__(parent)
        # создали экземпляр класса
        self.ui = Ui_CoordWidget()
        # подгрузили файл
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.groupBox.setTitle(str(id_widget))
        # связываем событие нажатия на кнопку со слотом
        self.ui.pushButton.clicked.connect(self.press_del)

    @Slot()
    # вызывается при нажатии на кнопку удаления и передаем инт значение в main
    def press_del(self):
        self.delete.emit(self.id_widget)

