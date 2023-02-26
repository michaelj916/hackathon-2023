

class ReadData:

    @staticmethod
    def read_todo(todo_list, filename):
        with open(filename, 'r') as fileopen:
            fileopen = fileopen.readlines()

        for items in fileopen:
            if len(items) > 1:
                items = items.replace('\n','')

                todo_list.addItem(f'• {items}')
