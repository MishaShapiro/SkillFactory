import pygame

class Figurs: # Класс всех фигур на доске

    def __init__(self, x, y, color):
        self.color = color # Цвет фигуры (белый или чёрный)
        self.start_position = (x, y) # Стартовая позиция фигуры
        self.x = x
        self.y = y
        self.attacked = False # Обозначение, атакована ли фигура
        self.moves = [] # Все возможные ходы фигуры
        self.chosen = False

    def can_move(self, mass): # Метод для нахождения вариантов хода
        for i in desk.figurs: # приравнивание всех атрибутов выбора на False
            i.chosen = False
        mass.remover() # метод удаляющий невозможные ходы
        self.moves = mass.move # обновление атрибута фигуры
        desk.all_moves = mass.move # добавление в атрибут доски все видимые пути
        self.chosen = True
        desk.upload()

    def move_to(self, x, y):
        if (x, y) in desk.all_moves:
            self.start_position = (x, y)
            self.x = x
            self.y = y
        else:
            print("Нельзя выполнить это действие")

class Desk: # класс шахматной доски

    def __init__(self, figurs):
        self.dicter = {} # словарь с ключами: стартовыми позициями, значениями: фигурами
        self.figurs = figurs # все фигуры на доске
        self.all_moves = [] # все возможные ходы выбранной фигуры
        position_in_desk = []
        for i in self.figurs: # позиции всех фигур на доске
            self.dicter[i.start_position] = i
            position_in_desk.append(i.start_position)
        self.position_in_desk = position_in_desk # создание атрибута с таким массивом

    def upload(self):
        self.dicter = {}
        position_in_desk = []
        for i in self.figurs:  # переопределение позиций фигур
            self.dicter[i.start_position] = i
            position_in_desk.append(i.start_position)
        self.position_in_desk = position_in_desk

    def draw_desk(self): # отрисовка доски
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
            for i in range(0, 8): # проход по всем клеткам доски и их отрисовка в зависимости от параметров
                for j in range(0, 8):
                    if (i, j) in self.dicter.keys(): # на этой клетке стоит фигура
                        color_fig = self.dicter[(i, j)].color
                        sym = self.dicter[(i, j)].name
                        if color_fig == "Black":
                            color_sym = "White"
                        else:
                            color_sym = "Black"
                        pygame.draw.rect(screen, color_fig, (100 + j * pixels, 100 + i * pixels, pixels, pixels))
                        if sym != "Kn": # отрисовка названия фигуры
                            screen.blit(f2.render(sym, True, color_sym), (115 + j * pixels, 110 + i * pixels))
                        else:
                            screen.blit(f2.render(sym, True, color_sym), (100 + j * pixels, 110 + i * pixels))
                    elif (i, j) in self.all_moves: # при вызове метода can_move фигура берётся в руку ==> показываются все ходы фигуры
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

class Positions(Desk): # дочерний класс позиций на доске

    def __init__(self, move):
        super(Positions, self).__init__(desk.figurs)
        self.move = move # создание атрибута со всеми путями для определённой фигуры

    def remover(self): # метод удаления всех невозможных ходов
        new_move = []
        for i in self.move:
            if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7 and not(i in self.position_in_desk):
                new_move.append(i)
        self.move = new_move

class King(Figurs): # король

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color)
        self.name = "K"

    def can_move(self): # метод нахождения всех возможных ходов фигуры
        mass = Positions([(self.x + i, self.y + j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0])
        super(King, self).can_move(mass) # возвращение в метод родительского класса

        # у остальных фигур аналогичный код отвечает за то же

class Peshka(Figurs):

    def __init__(self, x, y, color):
        super(Peshka, self).__init__(x, y, color)
        self.name = "P"

    def can_move(self):
        if self.color == "White": # по цыету разные стороны
            mass = Positions([(self.x + 1, self.y)])
        else:
            mass = Positions([(self.x - 1, self.y)])
        super(Peshka, self).can_move(mass)

class Knight(Figurs):

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color)
        self.name = "Kn"

    def can_move(self):
        mass = Positions([(self.x + i, self.y + j) for i in range(-2, 3) for j in range(-2, 3) if abs(i) + abs(j) == 3])
        super(Knight, self).can_move(mass)

class Eleph(Figurs):

    def __init__(self, x, y, color):
        super(Eleph, self).__init__(x, y, color)
        self.name = "E"

    def can_move(self):
        # удаляет все возможные перепрыгивания через фигуры
        pit = desk.position_in_desk # все фигуры на доске
        res1 = []
        res2 = []
        x, y = self.x, self.y
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

class Ladia(Figurs):

    def __init__(self, x, y, color):
        super(Ladia, self).__init__(x, y, color)
        self.name = "L"

    def can_move(self):
        # Аналогично, как у слона, только другой направление
        pit = desk.position_in_desk
        res1 = []
        res2 = []
        x, y = self.x, self.y
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

class Ferz(Figurs):

    def __init__(self, x, y, color):
        super(Ferz, self).__init__(x, y, color)
        self.name = "F"

    def can_move(self):
        # совмещение ходов слона и ладьи
        eleph = Eleph(self.x, self.y, self.color)
        eleph.can_move()
        ladia = Ladia(self.x, self.y, self.color)
        ladia.can_move()
        mass = Positions(eleph.moves + ladia.moves)
        super(Ferz, self).can_move(mass)

a = Ladia(0, 1, "Black")
b = Peshka(5, 6, "White")
c = Knight(5, 1, "Black")
d = Eleph(3, 2, "White")
e = Ladia(2, 2, "Black")
f = Ferz(4, 4, "White")
mass = [a, b, c, d, e, f]
desk = Desk(mass)
desk.draw_desk()
c.can_move()
desk.draw_desk()
a.can_move()
desk.draw_desk()
a.move_to(4, 1)
f.can_move()
desk.draw_desk()
a.can_move()
desk.draw_desk()
