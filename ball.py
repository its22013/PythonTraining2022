import random
import math


class Ball:
    """ ボールクラス
    円を描く関数を使って表現する。
    """
    
    def __init__(self, canvas, color, paddle):
        """ 初期化処理
        メイン側から Canvas を受け取る。
        ボールの色も str 型で受け取る。
        衝突判定に使うパドルを受け取る。
        """
        self.canvas = canvas
        self.paddle = paddle
        
        # 楕円を描く関数できれいな円を描画する。識別番号を保持しておく。
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        # 画面サイズ(縦/横)を取得しておく。
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # ボールの初期位置を計算で決める。リセット時のことを考えて保存しておく。
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        # ボールの移動スピードをとりあえず0で作っておく
        self.speed = 0
        # ボールのx/yのスピードを0でとりあえず初期化
        self.x = 0
        self.y = 0
        

    def start(self, evt):
        # ボール移動中なら何もしない
        if self.speed != 0:
            return
        
        # 初期位置へ移動(絶対座標)
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3      # 移動スピード
        """ 発射角度のリストを生成(angle の処理内容)
            1 - range() で 20 - 60 のデータを作成
            2 - list() でリスト型に変換
            3 - random.choice() でリストから1個をランダムで選択
            4 - math.radians() で度数法から弧度法(ラジアン)に変換
        """
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])  # xの向きをランダムに。
        # 三角関数をつかって、x軸y軸それぞれの移動速度を求める。
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    
    def draw(self):
        # ボールを移動させる
        self.canvas.move(self.id, self.x, self.y)

        # 移動したあとの座標(左上xy,右下xy)を取得する
        pos = self.canvas.coords(self.id)

        # 左に当たった(pos[0]が越えた)かどうか
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)

        # 上に当たった(pos[1]が越えた)かどうか
        if pos[1] <= 0:
            self.fix(0, pos[1])

        # 右に当たった(pos[2]が越えた)かどうか
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)

        # 下に当たった(pos[3]が越えた)かどうか
        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()  #プレイヤーのミスを処理する関数を呼ぶ

        # パドルとの衝突判定
        paddle_pos = self.canvas.coords(self.paddle.id)
        # b.x2 >= p.x1
        # b.x1 <= p.x2
        # p.y1 <= b.y2 <= p.y2
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
        
        
    def fix(self, diff_x, diff_y):
        # x/y の差分を受け取って、2倍した数を逆に移動する。
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))

        # 差分があったら(0でなければ)跳ね返ったとして向きを反転させる。
        if diff_x != 0:
            self.x = -self.x
            
        if diff_y != 0:
            self.y = -self.y

    def failed(self):
        # 動きを止める
        self.x = 0
        self.y = 0
        self.speed = 0

        





















    
