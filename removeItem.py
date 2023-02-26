

class RemoveItem:
    @classmethod
    def remove_itemdata(cls,widget):
        return str(widget.currentItem().text())


class DoubleClickAdd:
    def completed_items(self, item, widget, complete_widget, counter):
        item_name = str(widget.currentItem().text())[2:]
        counter.setText(str(int(counter.text()) - 1))
        widget.takeItem(widget.row(item))

        with open('CompleteItem', 'a') as fileopen:
            fileopen.writelines(f'{item_name}\n')
            complete_widget.addItem(item_name)


    def remove_from_file(self, text, filename):
        with open(filename, 'r') as fileread:
            updated_file = ''





