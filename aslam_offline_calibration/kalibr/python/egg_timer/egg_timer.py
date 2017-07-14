# install Pygame
from Tkinter import *
import tkMessageBox
import time
import pygame
 
# RING
 
def ring(sound='./ring.wav'):
     
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound)
    sound.play()
    time.sleep(sound.get_length())
    pygame.mixer.quit()
 
 
 
def ringatend(target):
    """ a decorator to make your functions rings when they are done """
     
    def f(*args,**kwargs):
         
        result = target(*args,**kwargs)
        ring()
        return result
         
    return f
 
 
 
# IN MUSIC !
 
def inmusic(target):
    """ a decorator to play your functions in music """
             
    def f(*args,**kwargs):
         
        pygame.mixer.init()
        sound = pygame.mixer.Sound('./music.wav')
        sound.play(loops=-1)
        result = target(*args,**kwargs)
        sound.stop()
        pygame.mixer.quit()
        return result
             
    return f
 
 
 
# POPUPS
 
def popup(txt='Finished'):
    root = Tk()
    tkMessageBox.showinfo('Finished!',txt)
    root.destroy()
    root.mainloop()
 
 
 
def popupatend(target):
     
     
    def f(*args,**kwargs):
         
        # Run the function
        result = target(*args,**kwargs)
         
        # Make a pretty text
        fname = target.func_name
        pretty_args = ','.join([str(a) for a in args])
        pretty_kwargs = ','.join(['%s=%s'%(str(k),str(v))
                       for k,v in kwargs.iteritems()])  
        descr ='%s(%s,%s)'%(fname,pretty_args, pretty_kwargs)
        descr = descr[:100] # in case it really is too long
         
        # popup description
        popup(txt='%s done !'%(descr))
     
        return result
     
    return f
 
 
 
### EXAMPLES
 
@ringatend
@inmusic
def myLongFunction():
        for i in range(1000000):
            print "I'm the world's most useless function !"
 
myLongFunction()
 
@popupatend
def myLongFunction():
        for i in range(100000):
            print "I'm the most useless function !"
 
myLongFunction()
