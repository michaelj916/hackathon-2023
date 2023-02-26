
import json
from PyQt5.QtGui import QColor

from ImportantData import ImportantData

class AddData:
    star_click = False

    def star_clicked_change(self, star, addtask):
        AddData.star_click = ImportantData.star_clicked(star, addtask)


    def write_todo(self, text_string, todolist, counter, placeholder, filename, stickpad):

        if self.check_data(text_string, placeholder):
            with open(filename, 'a') as fileopen:
                fileopen.writelines(f'{text_string}\n')

                if AddData.star_click:
                    todolist.addItem(f'★ {text_string}')
                    lastitem = todolist.item(todolist.count()-1)
                    lastitem.setForeground(QColor('Dark Orange'))

                    stickpad.addItem(f'☆ {text_string}')

                else:
                    todolist.addItem(f' • {text_string}')


                counter.setText(f'{int(counter.text())+1}')



    def check_data(self, text_string, placeholder):
        if len(text_string.strip()) <= 1:
            placeholder.setText('')
            placeholder.setPlaceholderText(" Please add more character...")
            return False
        return True


