def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def obstacle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()


def obstacle_sequence():
    obstacle()
    turn_left()


move()
obstacle_sequence()
obstacle_sequence()
move()
move()
obstacle_sequence()
obstacle_sequence()
move()
obstacle_sequence()
move()
move()
move()


