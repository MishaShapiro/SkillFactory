from HomeWork import *

mass = [Ladia(0, 1, "Black"), Peshka(5, 6, "White"), Knight(1, 4, "Black")]
desk.create_table(mass)
mass[0].can_move()
desk.draw_desk()
mass[0].get_name()
desk.draw_desk()
mass[0].move_to(1, "H")
desk.draw_desk()
mass[1].get_name()
mass[1].can_move()
desk.draw_desk()
mass[0].can_move()
desk.draw_desk()
