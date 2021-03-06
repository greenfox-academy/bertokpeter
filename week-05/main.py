from view import View
from map import Map
from entity import *
from game_logic import Logic
import random

class Game:
    def __init__(self):
        self.mymap = Map()
        self.myview = View()
        self.logic = Logic()
        self.myview.root.bind("<KeyPress>", self.on_key_press)
        self.myview.draw_map(self.mymap.tiles)
        self.chars_on_screen = []
        self.myhero = Hero(self.myview.draw_entity(self.myview.hero_down, [0, 0]))
        self.chars_on_screen.append(self.myhero)
        self.skeleton1 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton1)
        self.skeleton2 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton2)
        self.skeleton3 = Skeleton(self.myview.draw_entity(self.myview.skeleton_image, self.rand_gen()))
        self.chars_on_screen.append(self.skeleton3)
        self.myboss = Boss(self.myview.draw_entity(self.myview.boss_image, self.rand_gen()))
        self.chars_on_screen.append(self.myboss)  
        self.myview.draw_stats(self.myhero.name, self.myhero.stats)
        self.myview.display()
    
    def rand_gen(self):
        coords = [0, 0]
        while (self.is_occupied(self.chars_on_screen, coords[0],coords[1]) 
              or self.mymap.get_cell(coords[0],coords[1]) == 1):
            coords[0] = random.randint(0,9)
            coords[1] = random.randint(0,8)
        return coords
        
    def is_occupied(self, char_list, x, y):
        for char in char_list:
            coords = self.myview.canvas.coords(char.picture)
            its_occupied = int(coords[0]//72) == x and int(coords[1]//72) == y
            if its_occupied:
                break
        return its_occupied

    def move(self, char, dx, dy):
         self.myview.canvas.move(char, dx*72, dy*72)
    
    def turn_hero(self, image):
        self.myview.canvas.itemconfig(self.myhero.picture, image=self.myview.hero_images[image])

    def who_is_here(self):
        coords = self.myhero.get_coords(self.myview.canvas.coords(self.myhero.picture))
        if self.is_occupied(self.chars_on_screen[1:], coords[0], coords[1]):
            for char in self.chars_on_screen[1:]:
                coords2 = char.get_coords(self.myview.canvas.coords(char.picture))
                if coords[0] == coords2[0] and coords[1] == coords2[1]:
                    self.myhero.status = "in combat"
                    return char
    
    def fight(self, char):
        self.logic.battle(self.myhero, char)
        if self.myhero.status == "dead":
            self.myview.death(self.myhero)
            self.myview.game_over()
        else:
            if not char.status == "dead":
                char.get_stats()  
                self.myview.draw_stats(char.name, char.stats)
                self.myhero.get_stats()
                self.myview.draw_stats(self.myhero.name, self.myhero.stats)
            elif char.status == "dead": 
                self.myview.death(char)
                self.chars_on_screen.remove(char)
                self.myhero.status = "peace"
                self.myhero.level_up()
                self.myhero.get_stats()
                self.myview.draw_stats(self.myhero.name, self.myhero.stats)

    def on_key_press(self, e):
        if self.myhero.status == "peace":
            self.myview.delete_stats()
            self.myview.draw_stats(self.myhero.name, self.myhero.stats)
            coords = self.myhero.get_coords(self.myview.canvas.coords(self.myhero.picture))
            if e.keysym == 'Up':
                self.turn_hero("up")
                if coords[1] >= 1 and not self.mymap.get_cell(coords[0],coords[1]-1) == 1:
                    self.move(self.myhero.picture, 0, -1)
            elif e.keysym == 'Down':
                self.turn_hero("down")
                if coords[1] <= 7 and not self.mymap.get_cell(coords[0],coords[1]+1) == 1:
                    self.move(self.myhero.picture, 0, 1)
            elif e.keysym == 'Right':
                self.turn_hero("right")
                if coords[0] <= 8 and not self.mymap.get_cell(coords[0]+1,coords[1]) == 1:
                    self.move(self.myhero.picture, 1, 0)
            elif e.keysym == 'Left':
                self.turn_hero("left")
                if coords[0] >= 1 and not self.mymap.get_cell(coords[0]-1,coords[1]) == 1:
                    self.move(self.myhero.picture, -1, 0)
            if len(self.chars_on_screen) > 1:
                if self.who_is_here():
                    self.myview.draw_stats(self.who_is_here().name, self.who_is_here().stats)
        elif self.myhero.status == "in combat":
            if e.keysym == 'space':
                self.myview.delete_stats()
                self.fight(self.who_is_here())
        else:
            if e.keysym == 'x':
                self.myview.quit_app()

game = Game()