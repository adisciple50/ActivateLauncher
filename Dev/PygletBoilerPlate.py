#__author__ = 'Jason Crockett'

import pyglet

Window = pyglet.window.Window()
Label = pyglet.text.Label('Activate Launcher',font_size=36,x=Window.width()//2,y=Window.height//2,anchor_x='center',anchor_y='center')

"""
@Window.event
def on_draw():
    Window.clear()
    Label.draw()
"""

pyglet.app.run()