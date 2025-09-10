import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('打砖块游戏')

# 设置时钟
clock = pygame.time.Clock()

# 板和球的参数
paddle_width = 100
paddle_height = 20
ball_radius = 10


# 创建一个板类
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect((screen_width - paddle_width) / 2, screen_height - 40, paddle_width, paddle_height)

    def move(self, x):
        if 0 < self.rect.x + x < screen_width - paddle_width:
            self.rect.x += x

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)


# 创建一个球类
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(screen_width / 2 - ball_radius, screen_height / 2 - ball_radius, ball_radius * 2,
                                ball_radius * 2)
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 碰撞检测
        if self.rect.x <= 0 or self.rect.x >= screen_width - ball_radius * 2:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0:
            self.speed_y = -self.speed_y

    def draw(self):
        pygame.draw.circle(screen, yellow, (self.rect.x + ball_radius, self.rect.y + ball_radius), ball_radius)


# 创建砖块类
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 75, 20)

    def draw(self):
        pygame.draw.rect(screen, green, self.rect)


# 创建砖块数组
def create_bricks(rows, cols):
    bricks = []
    for row in range(rows):
        for col in range(cols):
            bricks.append(Brick(col * 80 + 10, row * 30 + 50))
    return bricks


# 主游戏循环
def game_loop():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks(5, 10)
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-8)
        if keys[pygame.K_RIGHT]:
            paddle.move(8)

        ball.move()

        # 检查球与砖块的碰撞
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                bricks.remove(brick)
                ball.speed_y = -ball.speed_y
                score += 1

        # 检查球与板的碰撞
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y = -ball.speed_y

        # 检查球是否掉落
        if ball.rect.y > screen_height:
            # 游戏结束，显示消息
            display_game_over(score)
            running = False

        screen.fill(black)  # 清空屏幕
        paddle.draw()  # 绘制板
        ball.draw()  # 绘制球

        for brick in bricks:
            brick.draw()  # 绘制砖块

        pygame.display.flip()  # 更新屏幕
        clock.tick(60)  # 限制帧率

    pygame.quit()


# 显示游戏结束消息
def display_game_over(score):
    screen.fill(black)  # 清空屏幕
    font = pygame.font.SysFont("Microsoft YaHei", 50)  # 使用支持中文的字体
    game_over_text = font.render("游戏结束！得分: " + str(score), True, red)
    instructions_text = font.render("按 R 重新开始，按 Q 退出", True, white)

    screen.blit(game_over_text, (screen_width / 2 - 200, screen_height / 2 - 50))
    screen.blit(instructions_text, (screen_width / 2 - 250, screen_height / 2 + 10))

    pygame.display.flip()  # 更新屏幕

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    game_loop()  # 重新开始游戏
                    waiting = False


# 启动游戏
game_loop()
