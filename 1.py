import turtle

# === Настройка окна ===
screen = turtle.Screen()
screen.title("Черепашка-художник")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Для плавности

# === Создаём черепашку ===
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pensize(3)
t.pendown()  # ←←← ВАЖНО: перо ОПУЩЕНО — рисуем при движении!
t.speed(0)

# === Функции управления ===
def go_forward():
    t.forward(15)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def toggle_pen():
    if t.isdown():
        t.penup()
        t.color("gray")  # меняем цвет, чтобы видеть, что не рисуем
    else:
        t.pendown()
        t.color("purple")

def clear_all():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.color("purple")

def quit_gracefully():
    screen.clear()
    screen.bgcolor("black")
    text = turtle.Turtle()
    text.hideturtle()
    text.color("gold")
    text.penup()
    text.goto(0, 0)
    text.write("🎨 Рисунок завершён!\nСпасибо за творчество!", 
               align="center", font=("Arial", 20, "bold"))
    screen.ontimer(screen.bye, 2000)

# === Привязка клавиш ===
screen.listen()
screen.onkey(go_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(toggle_pen, "space")   # Пробел — поднять/опустить перо
screen.onkey(clear_all, "c")        # C — очистить всё
screen.onkey(quit_gracefully, "q")  # Q — выйти красиво
screen.onkey(quit_gracefully, "Escape")

# === Плавное обновление ===
def update():
    screen.update()
    screen.ontimer(update, 30)

update()

# === Завершение по клику (на всякий случай) ===
screen.exitonclick()