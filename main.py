# Импорт библиотек
import turtle
import random

WIDTH = 500
HEIGHT = 500
MEAL_SIZE = 10
DELAY = 100

moves = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def renew():
    global snake, moving_direction, meals_position, pen
    # Начальное положение змейки
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    # Начальное направление
    moving_direction = "up"
    # Получение расположения еды
    meals_position = get_meals_position()
    meal.goto(meals_position)
    # Работа с передвижением
    move_snake()


def move_snake():
    global moving_direction

    #  Определение следующего положения змейки
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + moves[moving_direction][0]
    new_head[1] = snake[-1][1] + moves[moving_direction][1]

    # Проверка на пересечение хвоста
    if new_head in snake[:-1]:
        renew()
    else:
        # Нет столкновений, продолжение игры
        snake.append(new_head)

        # Проверка на захват еды
        if not meal_collision():
            snake.pop(0)  # Змейка остается одного размера, до захвата еды

        #  Перенос змейки при столкновении со стеной
        if snake[-1][0] > WIDTH / 2:
            snake[-1][0] -= WIDTH
        elif snake[-1][0] < - WIDTH / 2:
            snake[-1][0] += WIDTH
        elif snake[-1][1] > HEIGHT / 2:
            snake[-1][1] -= HEIGHT
        elif snake[-1][1] < -HEIGHT / 2:
            snake[-1][1] += HEIGHT

        pen.clearstamps()

        # Рисуем змейку
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        # Обновляем окно
        screen.update()

        # Повтор
        turtle.ontimer(move_snake, DELAY)


def meal_collision():
    # Если змея съела еду, добавляем новую
    global meals_position
    if count_dist(snake[-1], meals_position) < 20:
        meals_position = get_meals_position()
        meal.goto(meals_position)
        return True
    return False


def get_meals_position():
    # Получение рандомной позиции для еды
    # С учетом расположения змеи
    x = random.randint(- WIDTH / 2 + MEAL_SIZE, WIDTH / 2 - MEAL_SIZE)
    y = random.randint(- HEIGHT / 2 + MEAL_SIZE, HEIGHT / 2 - MEAL_SIZE)
    return (x, y)


def count_dist(pos1, pos2):
    # Подсчет расстояния между головой змейки и едой
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

# Определение направления движения змейки


def move_up():
    global moving_direction
    if moving_direction != "down":
        moving_direction = "up"


def move_right():
    global moving_direction
    if moving_direction != "left":
        moving_direction = "right"


def move_down():
    global moving_direction
    if moving_direction != "up":
        moving_direction = "down"


def move_left():
    global moving_direction
    if moving_direction != "right":
        moving_direction = "left"


# Работа с окном вывода
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)

# Рисуем
pen = turtle.Turtle("square")
pen.penup()

# Еда
meal = turtle.Turtle()
meal.shape("circle")
meal.color("red")
meal.shapesize(MEAL_SIZE / 20)  # Обозначаем размер еды
meal.penup()

# Обрабатываем события, куда идет движение
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")

# Начало игры
renew()
turtle.done()