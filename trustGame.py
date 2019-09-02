# @Time : 2019/9/2 17:58
# @Author : Nelson Wang Songli
# @File : trustGame.py
# @Software: PyCharm


import Playground
from Entity.Actor import *
from Entity.Storage import *
from tkinter import *
from constant import *


def processKeyboardEvent(event):
    """
    :param event: the keyboard input
    :return: void
    """

    event_type = event.char
    if event_type in ORDER_MOVE:
        principal.move(event.char)
    elif event_type == ORDER_TAKE:
        principal.take()
    elif event_type == ORDER_DROP:
        principal.drop()

    show()


def show():
    """
    @This function constructs the body part of the game according to every component's coordinates

    :return:
    """
    row = 0
    while row < PLAYGROUND_HEIGHT:
        col = 0
        while col < PLAYGROUND_WIDTH:
            item = playground.get(row, col)
            if item == CELL_EMPTY:
                Label(frame, image=ground_img).grid(row=row, column=col)
            elif item == CELL_HUMAN:
                if principal.carriage == CELL_APPLE:
                    Label(frame, image=human_carry_apple_img).grid(row=row, column=col)
                else:
                    Label(frame, image=human_img).grid(row=row, column=col)
            elif item == CELL_APPLE:
                Label(frame, image=apple_img).grid(row=row, column=col)
            elif item == CELL_AGENT:
                if agent.carriage == CELL_APPLE:
                    # this part is not completed
                    Label(frame, image=human_carry_apple_img).grid(row=row, column=col)
                else:
                    Label(frame, image=agent_img).grid(row=row, column=col)
            elif item == CELL_APPLE_STORAGE_CLOSE:
                Label(frame, image=apple_storage_closed_img).grid(row=row, column=col)
            col += 1
        row += 1


# game components initialize
principal = Actor(PRINCIPAL_X, PRINCIPAL_Y)
agent = Actor(AGENT_X, AGENT_Y)
storage = Storage(STORAGE_X, STORAGE_Y)

# bind the playground and the actors
playground = Playground.Playground(PLAYGROUND_HEIGHT, PLAYGROUND_WIDTH, principal, agent, storage)
agent.set_playground(playground)
principal.set_playground(playground)

# graphic UI
root = Tk()
frame = Frame(root)
frame.bind('<KeyPress>', processKeyboardEvent)
frame.pack()
frame.focus_set()

# set image ******************************** maybe optimized later
ground_img = PhotoImage(file=IMAGE_GROUND)
human_img = PhotoImage(file=IMAGE_HUMAN)
human_carry_apple_img = PhotoImage(file=IMAGE_HUMAN_CARRY_APPLE)
agent_img = PhotoImage(file=IMAGE_AGENT)
apple_storage_closed_img = PhotoImage(file=IMAGE_APPLE_STORAGE_CLOSED)
apple_img = PhotoImage(file=IMAGE_APPLE)

# game launch
show()
root.mainloop()
