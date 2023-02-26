

class ImportantData:
    count = 0

    @staticmethod
    def star_clicked(star, lineedit):
        if ImportantData.count % 2 == 0:
            star.setStyleSheet("color: rgb(255, 150, 29); font: 23pt \"MS Shell Dlg 2\";")

            lineedit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                            "color: rgb(255, 150, 29);\n"
                                            "border: 3px solid rgb(214, 214, 214) ;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 5px;")
            ImportantData.count += 1
            return True
        else:
            star.setStyleSheet("color: rgb(214, 214, 214); font: 23pt \"MS Shell Dlg 2\";") #gray

            lineedit.setStyleSheet("font: 15pt \"Century Gothic\";\n"
                                            "color: rgb(112, 112, 112);\n"
                                            "border: 3px solid rgb(214, 214, 214) ;\n"
                                            "border-width: 2px;\n"
                                            "border-radius: 5px;")
            ImportantData.count += 1
            return False