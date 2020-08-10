# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

def normalize(arr):
    s = 0
    for i in range(len(arr)):
        s += sum(arr[i])
    q = []
    for i in range(len(arr)):
        w = []
        for j in range(len(arr[i])):
            w.append(arr[i][j] / s)
        q.append(w)

    return q


def sense(p, colors, measurement, sensor_right):
    q = []
    sensor_wrong = 1.0 - sensor_right
    for i in range(len(colors)):
        w = []
        for j in range(len(colors[i])):
            hit = (measurement == colors[i][j])
            s = p[i][j] * (hit * sensor_right + (1.0 - hit) * sensor_wrong)
            w.append(s)
        q.append(w)
    return normalize(q)


def move(p, motion, p_move):
    q = []
    p_stay = 1.0 - p_move
    for i in range(len(p)):
        w = []
        for j in range(len(p[i])):
            s = (p_move * p[(i - motion[0]) % len(p)][(j - motion[1]) % len(p[i])]) + \
                (p_stay * p[i][j])
            w.append(s)
        q.append(w)
    return q


def histogram_localization(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    # before the Robot has moved, each Grid-cell has a chance of (pinit) to be the location the Robot it Thinks it is on.
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    for i in range(len(measurements)):
        p = move(p, motions[i], p_move)
        p = sense(p, colors, measurements[i], sensor_right)
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')
