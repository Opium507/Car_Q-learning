from Game_test import Game_test
from pyglet.window import key
import pyglet
from pyglet.gl import *
from Global import displayHeight, displayWidth
import random as ran

frameRate = 25.0
dt=100

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # set background color
        backgroundColor = [0, 0, 0, 255]
        backgroundColor = [i / 255 for i in backgroundColor]
        glClearColor(*backgroundColor)
        # load background image

        self.game = Game_test()
        
    """
    called when a key is hit
    """

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.game.car.turningRight = True
            print('right pressed')
        
        if symbol == key.LEFT:
            self.game.car.turningLeft = True
            print('left pressed')
            
        if symbol == key.UP:
            self.game.car.accelerating = True
            print('up pressed')

        if symbol == key.DOWN:
            self.game.car.reversing = True
            print("down pressed")

    # action = ran.randint(1, 4)
    # print(action)

    # def randAction(self, action):
    #         if action == 1:
    #             self.game.car.turningRight = True
    #             print('right pressed')
            
    #         if action == 2:
    #             self.game.car.turningLeft = True
    #             print('left pressed')
                
    #         if action == 3:
    #             self.game.car.accelerating = True
    #             print('up pressed')

    #         if action == 4:
    #             self.game.car.reversing = True
    #             print("down pressed")

    """
    called when a key is released     
    """
    def on_key_release(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.game.car.turningRight = False
            print('right unpressed')
            
        if symbol == key.LEFT:
            self.game.car.turningLeft = False
            print('left unpressed')
        
        if symbol == key.UP:
            self.game.car.accelerating = False
            print('up unpressed')
        
        if symbol == key.DOWN:
            self.game.car.reversing = False
            print('down unpressed')

    """
    called every frame
    """
    def on_draw(self):
        self.game.render()
        
        glPushMatrix()
        
        glTranslatef(-1, -1, 0)
        glScalef(1/(displayWidth/2), 1/(displayHeight/2) , 1)
        
        self.clear()
        self.game.trackSprite.draw()
        self.game.car.show()
        
        # for w in self.game.walls:
        #     w.draw()
        # for g in self.game.gates:
        #     g.draw()

        pyglet.gl.glPopMatrix()

    """
    called when window resized
    """
    def on_resize(self, width, height):
        glViewport(0, 0, width, height)

    def update(self, dt):
        self.game.car.update()

if __name__ == "__main__":
    window = MyWindow(900, 500, "AI Learns to Drive", resizable=True)
    pyglet.clock.schedule_interval(window.update, 1 / frameRate)
    pyglet.app.run()
