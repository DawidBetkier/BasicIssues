"""Klocki"""

def make_bricks(small, big, goal):

    if small * 1 + big * 5 >= goal:
        print('OK, uda się')
    else:
        print('Za krótkie klocki')

if __name__ == '__main__':
    user_small= int(input('Podaj ilość małych klocków: '))
    user_big = int(input('Podaj ilość dużych klocków: '))
    user_goal = int(input('Podaj wymaganą długość: '))
    make_bricks(user_small, user_big, user_goal)
