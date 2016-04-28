#!/usr/bin/env python3
# coding: utf-8
# Lab 8 - Five in a Row GUI
# François Chalifour

from five_in_a_row import Game, Move
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 10

class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, 'Five in a Row')

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = GameUI(container, self)
        self.frames[GameUI] = frame
        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(GameUI)


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class GameUI(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.game = Game()
        self.row, self.col = 0, 0
        self.init_UI()


    def init_UI(self):
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self,
            width=WIDTH,
            height=HEIGHT,
            highlightthickness=0,
            relief='ridge',
            bg='gray10'
        )
        self.canvas.pack(fill=BOTH, side=TOP)

        Button(self,
            text='RESTART',
            height=24,
            fg='white',
            bg='gray20',
            activeforeground='white',
            activebackground='gray15',
            border=0,
            font=('Arial', 12, 'bold'),
            highlightthickness=0,
            relief='ridge',
            command=self.restart
        ).pack(fill=BOTH, side=BOTTOM)

        self.draw_grid()
        self.canvas.bind('<Button-1>', self.play)


    def restart(self):
        self.game = Game()
        self.row, self.col = 0, 0
        self.canvas.delete('all')
        self.draw_grid()


    def draw_grid(self):
        for i in range(self.game.width + 1):
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill='gray25')

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = HEIGHT - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill='gray25')

        self.board = [ [ self.game.get_cell_value(x, y) for x in range(self.game.width + 1) ] for y in range(self.game.height + 1) ]
        self.load_board(self.board)


    def load_board(self, board):
        for y in range(self.game.height + 1):
            for x in range(self.game.width + 1):
                player = self.game.get_cell_value(y, x)
                if player != ' ':
                    self.row, self.col = (self.game.width - 1) - x, y
                    self.draw_player(player)


    def play(self, event):
        if self.game.get_winner():
            return

        x, y = event.x, event.y

        if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            row, col = int((y - MARGIN)  / SIDE), int((x - MARGIN) / SIDE)
            real_x, real_y = col, (self.game.width - 1) - row

            if self.game.is_cell_free(real_x, real_y):
                self.row, self.col = row, col
                player = self.game.get_next_players_turn()
                self.game.make_move(real_x, real_y, player)
                self.draw_player(player)
                winner = self.game.get_winner()
                if winner:
                    self.draw_victory(winner)


    def draw_player(self, player):
        if self.row >= 0 and self.col >=0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1

            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                fill=self.get_color(player),
                outline=''
            )

            x = x0 + SIDE / 2
            y = y0 + SIDE / 2

            self.canvas.create_text(
                x, y,
                text=player,
                fill='white',
                font=('Arial', 12)
            )


    def draw_victory(self, winner):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 8
        self.canvas.create_oval(
            x0, y0, x1, y1,
            fill=self.get_color(winner),
            outline=''
        )

        x = y = MARGIN + 4 * SIDE + SIDE
        message = '{} player wins'.format(winner)
        self.canvas.create_text(
            x, y,
            text=message,
            fill='white',
            font=('Arial', 28)
        )


    def get_color(self, player):
        return 'dark slate gray' if player == 'X' else 'sea green'


if __name__ == '__main__':
    app = GameWindow()
    app.geometry('{width}x{height}'.format(width=WIDTH, height=HEIGHT + SIDE))
    app.mainloop()
