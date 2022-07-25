from tkinter import *

from ball import Ball


class Game:
    """ ゲームのメインクラス
    このクラスで、ゲーム全体のコントロールをします。
    処理の流れとして、全体像が把握できるように作る。
    """

    def __init__(self):
        """ 基本的な初期化をします。
        Tk オブジェクトの生成や初期設定をします。
        ゲームに必要なオブジェクトの準備をします。
        """

        # tkinter を使用するときの基本部分
        self.tk = Tk()
        self.tk.title("Game")                       # Tk本体(GUIのウィンドウ)
        self.tk.resizable(False, False)             # ウィンドウのサイズ変更を許可するかどうか。横・縦
        self.tk.wm_attributes("-topmost", True)     # ウィンドウを常に前面に。

        # 図形描画に使う Canvas オブジェクトの準備
        self.canvas = Canvas(self.tk, width=500, height=400, bd=False, highlightthickness=False)
        self.canvas.pack()      # canvas をメインウィンドウ(tk)に組み込んで表示
        self.tk.update()        # tk の状態を更新

        # ゲームの準備
        self.ball = Ball(self.canvas, "red")

    def main(self):
        """ ゲームを動かすための関数
        必ず初期化後に呼び出す。
        """
        self.update()       # 更新処理の関数
        self.tk.mainloop()  # Tk 使うときに、プログラムが一瞬で終了しないようにする。

    def update(self):
        # ボールの更新処理
        self.ball.draw()

        # 次回 update の呼び出し予約
        self.canvas.after(1000 // 60, self.update)
        

game = Game()
game.main()













