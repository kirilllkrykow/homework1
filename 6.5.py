class Stationery:
    title = "канцелярский предмет"

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("отрисовка ручкой")

class Pencil(Stationery):
    def draw(self):
        print("отрисовка карандашом")

class Handle(Stationery):
    def draw(self):
        print("отрисовка маркером")

brush = Stationery()
brush.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()