import pygame  # 导入pygame库，用于游戏开发
import time    # 导入time库，用于时间相关操作（本程序未直接使用）
import random  # 导入random库，用于生成随机数

# 初始化pygame模块
pygame.init()

# 定义常用颜色的RGB值
white = (255, 255, 255)      # 白色
yellow = (255, 255, 102)     # 黄色
black = (0, 0, 0)            # 黑色
red = (213, 50, 80)          # 红色
green = (0, 255, 0)          # 绿色
blue = (50, 153, 213)        # 蓝色

# 设置游戏窗口的宽度和高度
width = 600
height = 400
screen = pygame.display.set_mode((width, height))  # 创建游戏窗口
pygame.display.set_caption('Snake Game')           # 设置窗口标题

# 创建时钟对象，用于控制游戏帧率
clock = pygame.time.Clock()

# 设置蛇的每个块的大小和移动速度
snake_block = 10    # 蛇身每块的像素大小
snake_speed = 10    # 蛇的移动速度（帧率）

# 定义字体对象，用于显示消息和分数
font_style = pygame.font.SysFont("bahnschrift", 25)      # 普通消息字体
score_font = pygame.font.SysFont("comicsansms", 35)      # 分数字体（未使用）


# 绘制蛇的函数
def our_snake(snake_block, snake_list):
    """
    根据蛇身块列表绘制蛇，每个块用黑色矩形表示
    """
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])  # 绘制每个蛇身块


# 显示消息的函数
def message(msg, color):
    """
    在屏幕指定位置显示消息文本
    """
    mesg = font_style.render(msg, True, color)  # 渲染文本
    screen.blit(mesg, [width / 6, height / 3])  # 显示在屏幕上


# 游戏主循环函数
def gameLoop():
    game_over = False   # 游戏总结束标志
    game_close = False  # 游戏失败标志（用于显示失败界面）

    # 初始化蛇头坐标为屏幕中心
    x1 = width / 2
    y1 = height / 2

    # 初始化蛇头移动方向
    x1_change = 0
    y1_change = 0

    snake_List = []         # 蛇身块坐标列表
    Length_of_snake = 1     # 初始蛇长度

    # 随机生成食物坐标，保证在网格上
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # 游戏主循环
    while not game_over:

        # 游戏失败后，进入失败界面
        while game_close == True:
            screen.fill(blue)  # 填充背景为蓝色
            message("You lost!\nPress C to continue or press Q to quit.", red)  # 显示失败消息
            pygame.display.update()  # 刷新屏幕

            # 处理用户按键事件
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # 按Q退出游戏
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # 按C重新开始游戏
                        gameLoop()  # 递归调用，重新开始

        # 处理游戏中的事件（方向键和退出）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击关闭窗口
                game_over = True
            if event.type == pygame.KEYDOWN:  # 按下方向键
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block  # 向左移动
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block   # 向右移动
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block  # 向上移动
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block   # 向下移动
                    x1_change = 0

        # 检查蛇头是否碰到边界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True  # 出界则失败

        # 更新蛇头坐标
        x1 += x1_change
        y1 += y1_change

        screen.fill(blue)  # 填充背景为蓝色
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])  # 绘制食物

        # 更新蛇身列表
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:  # 保持蛇身长度
            del snake_List[0]  # 删除最早的块（蛇尾）

        # 检查蛇头是否碰到自身
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True  # 碰到自身则失败

        our_snake(snake_block, snake_List)  # 绘制蛇身

        pygame.display.update()  # 刷新屏幕

        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            # 吃到食物后，随机生成新食物坐标
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # 蛇长度加一

        clock.tick(snake_speed)  # 控制帧率，决定蛇移动速度

    pygame.quit()  # 退出pygame
    quit()         # 退出程序


gameLoop()  # 启动游戏主循环
