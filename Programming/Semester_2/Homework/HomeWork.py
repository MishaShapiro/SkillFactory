import pygame


class Figurs:  # Класс всех фигур на доске

    def __init__(self, x, y, color):
        self._color = color  # Цвет фигуры (белый или чёрный)
        self._start_position = (x, y)  # Стартовая позиция фигуры
        self._x = x
        self._y = y
        self._attacked = False  # Обозначение, атакована ли фигура
        self._moves = []  # Все возможные ходы фигуры
        self._chosen = False

    def can_move(self, mass):  # Метод для нахождения вариантов хода
        for i in desk._figurs:  # приравнивание всех атрибутов выбора на False
            i._chosen = False
        mass._remover()  # метод удаляющий невозможные ходы
        self._moves = mass._move  # обновление атрибута фигуры
        desk._all_moves = mass._move  # добавление в атрибут доски все видимые пути
        self._chosen = True
        desk._upload()

    def move_to(self, x, y):
        y_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        x = x - 1
        y = y_dict[y]
        if (x, y) in desk._all_moves:
            self._start_position = (x, y)
            self._x = x
            self._y = y
        else:
            print("Нельзя выполнить это действие")
        desk._upload()
        desk._all_moves = []

    def get_name(self, name):
        y_de_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
        print("У выбранной фигуры название:", name)
        print("И позиция:", self._x + 1, y_de_dict[self._y])


class _Desk:  # класс шахматной доски

    def __init__(self, figurs):
        self._dicter = {}  # словарь с ключами: стартовыми позициями, значениями: фигурами
        self._figurs = figurs  # все фигуры на доске
        self._all_moves = []  # все возможные ходы выбранной фигуры
        position_in_desk = []
        for i in self._figurs:  # позиции всех фигур на доске
            self._dicter[i._start_position] = i
            position_in_desk.append(i._start_position)
        self._position_in_desk = position_in_desk  # создание атрибута с таким массивом

    def create_table(self, figurs): # Метод для добавления фигур на доску в другом файле
        self._dicter = {}  # словарь с ключами: стартовыми позициями, значениями: фигурами
        self._figurs = figurs  # все фигуры на доске
        self._all_moves = []  # все возможные ходы выбранной фигуры
        position_in_desk = []
        for i in self._figurs:  # позиции всех фигур на доске
            self._dicter[i._start_position] = i
            position_in_desk.append(i._start_position)
        self._position_in_desk = position_in_desk  # создание атрибута с таким массивом

    def _upload(self):
        self._dicter = {}
        position_in_desk = []
        for i in self._figurs:  # переопределение позиций фигур
            self._dicter[i._start_position] = i
            position_in_desk.append(i._start_position)
        self._position_in_desk = position_in_desk

    def draw_desk(self):  # отрисовка доски
        # стандартный вызов окна pygame

        pixels = 60

        WIDHT = 200 + 8 * pixels
        HEIGHT = 200 + 8 * pixels
        FPS = 30

        pygame.init()
        screen = pygame.display.set_mode((WIDHT, HEIGHT))
        pygame.display.set_caption("Chess")
        clock = pygame.time.Clock()

        # работа с шрифтом и текстом

        f1 = pygame.font.Font(None, 90)
        f2 = pygame.font.Font(None, 60)
        text1 = f1.render('A B C D E F G H', True, (0, 0, 0))

        running = 1

        # запуск программы

        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
            screen.fill((200, 200, 200))
            for i in range(0, 8):  # проход по всем клеткам доски и их отрисовка в зависимости от параметров
                for j in range(0, 8):
                    if (i, j) in self._dicter.keys():  # на этой клетке стоит фигура
                        color_fig = self._dicter[(i, j)]._color
                        sym = self._dicter[(i, j)]._name
                        if color_fig == "Black":
                            color_sym = "White"
                        else:
                            color_sym = "Black"
                        pygame.draw.rect(screen, color_fig, (100 + j * pixels, 100 + i * pixels, pixels, pixels))
                        if sym != "Kn":  # отрисовка названия фигуры
                            screen.blit(f2.render(sym, True, color_sym), (115 + j * pixels, 110 + i * pixels))
                        else:
                            screen.blit(f2.render(sym, True, color_sym), (100 + j * pixels, 110 + i * pixels))
                    elif (i,
                          j) in self._all_moves:  # при вызове метода can_move фигура берётся в руку ==> показываются все ходы фигуры
                        pygame.draw.rect(screen, (255, 230, 0), (100 + j * pixels, 100 + i * pixels, pixels, pixels))
                    elif (i + j) % 2 == 0:
                        pygame.draw.rect(screen, (156, 156, 156), (100 + j * pixels, 100 + i * pixels, pixels, pixels))
                    else:
                        pygame.draw.rect(screen, (163, 116, 73), (100 + j * pixels, 100 + i * pixels, pixels, pixels))
                    # линиии на доске
                    pygame.draw.rect(screen, (128, 128, 128), (100 + j * pixels, i * pixels, 2, HEIGHT))
                    pygame.draw.rect(screen, (128, 128, 128), (j * pixels, 100 + i * pixels, WIDHT, 2))
            pygame.draw.rect(screen, (128, 128, 128), (0 * pixels, 100 + 8 * pixels, WIDHT, 2))
            pygame.draw.rect(screen, (128, 128, 128), (100 + 8 * pixels, 0 * pixels, 2, HEIGHT))
            # прикрепление текста
            screen.blit(text1, (110, 600))
            for i in "12345678":
                text2 = f1.render(i, True, (0, 0, 0))
                screen.blit(text2, (30, 60 * int(i) + 40))
            pygame.display.flip()

        pygame.quit()


class Positions(_Desk):  # дочерний класс позиций на доске

    def __init__(self, move):
        super(Positions, self).__init__(desk._figurs)
        self._move = move  # создание атрибута со всеми путями для определённой фигуры

    def _remover(self):  # метод удаления всех невозможных ходов
        new_move = []
        for i in self._move:
            if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7 and not (i in self._position_in_desk):
                new_move.append(i)
        self._move = new_move


class King(Figurs):  # король

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color)
        self._name = "K"

    def can_move(self):  # метод нахождения всех возможных ходов фигуры
        mass = Positions([(self._x + i, self._y + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0])
        super(King, self).can_move(mass)  # возвращение в метод родительского класса

    def get_name(self):
        super(King, self).get_name(self._name)

        # у остальных фигур аналогичный код отвечает за то же


class Peshka(Figurs):

    def __init__(self, x, y, color):
        super(Peshka, self).__init__(x, y, color)
        self._name = "P"

    def can_move(self):
        if self._color == "White":  # по цыету разные стороны
            mass = Positions([(self._x + 1, self._y)])
        else:
            mass = Positions([(self._x - 1, self._y)])
        super(Peshka, self).can_move(mass)

    def get_name(self):
        super(Peshka, self).get_name(self._name)


class Knight(Figurs):

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color)
        self._name = "Kn"

    def can_move(self):
        mass = Positions(
            [(self._x + i, self._y + j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) == 3])
        super(Knight, self).can_move(mass)

    def get_name(self):
        super(Knight, self).get_name(self._name)


class Eleph(Figurs):

    def __init__(self, x, y, color):
        super(Eleph, self).__init__(x, y, color)
        self._name = "E"

    def can_move(self):
        # удаляет все возможные перепрыгивания через фигуры
        pit = desk._position_in_desk  # все фигуры на доске
        res1 = []
        res2 = []
        x, y = self._x, self._y
        # прохождение по диагонали и удаление всех перепрыгивний
        for i in range(-7, 8):
            if 0 <= x + i <= 7 and 0 <= y + i <= 7 and i != 0:
                res1.append((x + i, y + i))
                if i < 0 and (x + i, y + i) in pit:
                    res1 = []
                if i > 0 and (x + i, y + i) in pit:
                    break
        # прохождение по другой диагонали и удаление всех перепрыгивний
        for i in range(-7, 8):
            if 0 <= x + i <= 7 and 0 <= y - i <= 7 and i != 0:
                res2.append((x + i, y - i))
                if i < 0 and (x + i, y - i) in pit:
                    res2 = []
                if i > 0 and (x + i, y - i) in pit:
                    break
        mass = Positions(res1 + res2)
        super(Eleph, self).can_move(mass)

    def get_name(self):
        super(Eleph, self).get_name(self._name)


class Ladia(Figurs):

    def __init__(self, x, y, color):
        super(Ladia, self).__init__(x, y, color)
        self._name = "L"

    def can_move(self):
        # Аналогично, как у слона, только другой направление
        pit = desk._position_in_desk
        res1 = []
        res2 = []
        x, y = self._x, self._y
        for i in range(-7, 8):
            if 0 <= x + i <= 7 and i != 0:
                res1.append((x + i, y))
            if i < 0 and (x + i, y) in pit:
                res1 = []
            if i > 0 and (x + i, y) in pit:
                break
        for i in range(-7, 8):
            if 0 <= y + i <= 7 and i != 0:
                res2.append((x, y + i))
            if i < 0 and (x, y + i) in pit:
                res2 = []
            if i > 0 and (x, y + i) in pit:
                break

        mass = Positions(res1 + res2)
        super(Ladia, self).can_move(mass)

    def get_name(self):
        super(Ladia, self).get_name(self._name)


class Ferz(Figurs):

    def __init__(self, x, y, color):
        super(Ferz, self).__init__(x, y, color)
        self._name = "F"

    def can_move(self):
        # совмещение ходов слона и ладьи
        eleph = Eleph(self._x, self._y, self._color)
        eleph.can_move()
        ladia = Ladia(self._x, self._y, self._color)
        ladia.can_move()
        mass = Positions(eleph._moves + ladia._moves)
        super(Ferz, self).can_move(mass)

    def get_name(self):
        super(Ferz, self).get_name(self._name)

desk = _Desk([])

