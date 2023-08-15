import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(root, text=" ", font=("Helvetica", 24),
                                   width=6, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner_message(self.current_player)
                self.reset_game()
            elif self.is_draw():
                self.show_draw_message()
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def show_winner_message(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")

    def show_draw_message(self):
        messagebox.showinfo("Game Over", "It's a draw!")

    def reset_game(self):
        for row in self.board:
            for col in row:
                col = " "
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.config(text=" ")
        self.current_player = "X"

def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
