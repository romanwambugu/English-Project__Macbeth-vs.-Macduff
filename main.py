#-------------------------------------Imports-----------------------------
import turtle as trtl
import random as rand
#------------------------------------Functions----------------------------
#Health Bar Create & Destroy
#This fucntion will play at the start to represent a full healthbar and when the enemy or user takes damage to indicate a loss of health.
def health_square(health_bar, amount, color, x_cord):
  health_bar.penup()
  health_bar.goto(x_cord, 110)
  health_bar.pendown()
  health_bar.begin_fill()
  health_bar.color(color)
  x = health_bar.xcor()
  y = health_bar.ycor()
  for i in range(amount):
    health_bar.goto(x, y)
    x += 30
    health_bar.setx(x)
    y += 45
    health_bar.sety(y)
    x -= 30
    health_bar.setx(x)
    y -= 45
    health_bar.sety(y)
    x += 30
  health_bar.end_fill()

#Player Move Left Function
#This function represents the user's left movement.
def user_left():
  global user_xcor
  global user_ycor
  user.shape(macbeth_left)
  user.speed(0)    
  if user_xcor > -340:
    user_xcor -= 25
  user.setx(user_xcor)
  user.sety(user_ycor)

#Player Move Right Function
#This function represents the user's right movement.
def user_right():
  global user_xcor
  global user_ycor
  user.shape(macbeth_right)
  user.speed(0)    
  if user_xcor < 340:
    user_xcor += 25
  user.setx(user_xcor)
  user.sety(user_ycor)

#Player Jump Function
#This function represents the user's jumping movement.
def user_jump():
  global currently_jumping
  global user_xcor
  global user_ycor
  screen.onkey(None, "space")
  currently_jumping = True
  ground = -105
  user.speed(1.8)
  y = user.ycor()
  if y == -105:
    for i in range(10):
      user_ycor += 20
      user.sety(user_ycor)
      user.setx(user_xcor)
    for i in range(10):
      user_ycor -= 20
      user.sety(user_ycor)
      user.setx(user_xcor)
  user.sety(ground)
  user.setx(user_xcor)
  currently_jumping = False
  screen.onkey(user_jump, "space")

#Player Punches
#This function is a punch ability that plays when the user is close enough. The function puts a knockback affect on the enemy when the enemy gets hit by the user.
def user_punch():
  global enemy_health
  global enemy_take_damage
  global user_xcor
  global enemy_xcor
  screen.onkey(None, "f")
  if enemy_health > 0 and user.distance(enemy) < 100 and currently_jumping == False:
    x = enemy.xcor()
    if enemy.xcor() > user_xcor:
      if x < 340:
        x += 50
      enemy.setx(x)
      enemy.shape(red_macduff_right) #Change enemy color to red when hit
    elif enemy.xcor() < user_xcor:
      if x > -340:
        x -= 50
      enemy.setx(x)
      enemy.shape(red_macduff_left) #Change enemy color to red when hit
    else:
      random_num = rand.randint(0, 1)
      if random_num == 0:
        x += 100
        enemy.setx(x)
        enemy.shape(red_macduff_right) #Change enemy color to red when hit
      elif random_num == 1:
        x -= 100
        enemy.setx(x)
        enemy.shape(red_macduff_left) #Change enemy color to red when hit

    screen.ontimer(change_enemy_color, 300)  #Delay for 0.3 seconds
    enemy_health -= 10
    enemy_take_damage += 30
    health_square(enemy_health_bar, 1, "black", enemy_take_damage)
    print("\n                     Macduff Health: " + str(enemy_health))
    if enemy_health == 0:
      game_win(True)
  screen.onkey(user_punch, "f")

#Enemy Movement Function
#This fucntion represents every movement the enemy should be able to make. This should only include the punching ability and the Right & Left movements.
def enemy_movement():
  global user_health
  global user_take_damage
  global user_xcor
  global enemy_xcor
  x = enemy.xcor()
  #Enemy Moves Right
  #This conditional represents the enemy's right movement.
  if user_xcor > enemy.xcor():
    enemy.shape(macduff_right)
    enemy.speed(3)
    if x < 340:
      x += 100
    enemy.setx(x)
    if enemy.xcor() > 340:
      enemy.setx(340)
  #Enemy Move Left
  #This conditional represents the enemy's left movement.
  elif user_xcor < enemy.xcor():
    enemy.shape(macduff_left)
    enemy.speed(3)
    if x > -340:
      x -= 100
    enemy.setx(x)
    if enemy.xcor() < -340:
      enemy.setx(-340)

  #Enemy Punch
  #This conditional is a punch ability that plays when the enemy is close enough. The conditional puts a knockback affect on the enemy when the user gets hit by the enemy.
  if user_health > 0 and enemy.distance(user) < 50:
    user.speed(4)
    if user_xcor > enemy.xcor():
      if x < 340:
        x += 100
      user.setx(x)
      user.shape(red_macbeth_left) #Change enemy color to red when hit
    elif user_xcor < enemy.xcor():
      if x > -340:
        x -= 100
      user.setx(x)
      user.shape(red_macbeth_right) #Change enemy color to red when hit
    else:
      random_num = rand.randint(0, 1)
      if random_num == 0:
        x += 100
        user.setx(x)
        user.shape(red_macbeth_left) #Change enemy color to red when hit
      elif random_num == 1:
        x -= 100
        user.setx(x)
        user.shape(red_macbeth_right) #Change enemy color to red when hit

    screen.ontimer(change_user_color, 300)  #Delay for 0.3 seconds
    user_health -= 10
    user_take_damage -= 30
    health_square(user_health_bar, 1, "black", user_take_damage)
    print("\nMacbeth Health: " + str(user_health))
    if user_health == 0:
      game_win(False)

  #This Triggers the function again after a delay in milliseconds
  screen.ontimer(enemy_movement, 800)

#Enemy Change Color
#This function changes the enemy's image back to it's original.
def change_enemy_color():
  global user_xcor
  global enemy_xcor
  if enemy.xcor() > user_xcor:
    enemy.shape(macduff_right)
  elif enemy.xcor() < user_xcor:
    enemy.shape(macduff_left)

#User Change Color
#This function changes the user's image back to it's original.
def change_user_color():
  global user_xcor
  global enemy_xcor
  if user_xcor > enemy.xcor():
    user.shape(macbeth_left)
  elif user_xcor < enemy.xcor():
    user.shape(macbeth_right)

#Game Over Function
#This function plays when the user or enemy healthbar reaches sero. A scren wll display depending on which character reaches zero first.
def game_win(win):
  screen.clear()
  screen.bgcolor("black")
  user.goto(0, 0)
  enemy.color("black")
  if win == True:
    print("\nMacbeth Wins!")
    screen.title("Macbeth Wins!")
    user.hideturtle()
    enemy.hideturtle()
    screen.bgpic(macbeth_won_background)
  elif win == False:
    print("\nMacduff Wins!")
    screen.title("Macduff Wins!")
    user.hideturtle()
    enemy.hideturtle()
    screen.bgpic(macduff_won_background)
#-----------------------------------ImageFiles----------------------------
#Screen Turtle
screen = trtl.Screen()
screen.setup(width=1.0, height=1.0)
screen.title("The Castle")

#Background Image Files
main_background = "3. Background Image Files/Main_Background.gif"
macbeth_won_background = "3. Background Image Files/Macbeth_Won_Background.gif"
macduff_won_background = "3. Background Image Files/Macduff_Won_Background.gif"

#macbeth Image Files
macbeth_right = "1. Macbeth Image Files/Macbeth_Right.gif"
macbeth_left = "1. Macbeth Image Files/Macbeth_Left.gif"
red_macbeth_right = "1. Macbeth Image Files/Red_Macbeth_Right.gif"
red_macbeth_left = "1. Macbeth Image Files/Red_Macbeth_Left.gif"

screen.addshape(macbeth_right)
screen.addshape(macbeth_left)
screen.addshape(red_macbeth_right)
screen.addshape(red_macbeth_left)

#macduff Image Files
macduff_right = "2. Macduff Image Files/Macduff_Right.gif"
macduff_left = "2. Macduff Image Files/Macduff_Left.gif"
red_macduff_right = "2. Macduff Image Files/Red_Macduff_Right.gif"
red_macduff_left = "2. Macduff Image Files/Red_Macduff_Left.gif"

screen.addshape(macduff_right)
screen.addshape(macduff_left)
screen.addshape(red_macduff_right)
screen.addshape(red_macduff_left)
#----------------------------------Initializations------------------------
#Background Image
screen.bgpic(main_background)

#User Turtle
user = trtl.Turtle()
user.shape(macbeth_right)
user.penup()
user.goto(-250, -70)
user_health = 100
user_take_damage = -40
currently_jumping = False
user_xcor = user.xcor()
user_ycor = user.ycor()

#Enemy Turtle
enemy = trtl.Turtle()
enemy.shape(macduff_left)
enemy.penup()
enemy.goto(250, -50)
enemy_health = 100
enemy_take_damage = 10
enemy_xcor = enemy.xcor()

#User Healthbar
user_health_bar = trtl.Turtle()
user_health_bar.hideturtle()
user_health_bar.width(2)
user_health_bar.speed(0)
health_square(user_health_bar, 10, "yellow", -340)

#Enemy Healthbar
enemy_health_bar = trtl.Turtle()
enemy_health_bar.hideturtle()
enemy_health_bar.width(2)
enemy_health_bar.speed(0)
health_square(enemy_health_bar, 10, "yellow", 40)

print("Macbeth Health: " + str(user_health))
print("                     Macduff Health: " + str(enemy_health))
#-------------------------------------Events------------------------------
#The Program starts here.
while True:
  screen.listen()
  screen.onkey(user_left, "a")
  screen.onkey(user_right, "d")
  screen.onkey(user_jump, "space")
  screen.onkey(user_punch, "f")
  enemy_movement() #This continually plays the enemy movement function.
  screen.update()
  screen.mainloop()
#-------------------------------------------------------------------------