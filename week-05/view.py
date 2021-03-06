from tkinter import *

class View:
    def __init__(self):
        self.root = Tk()
        self.size = 720
        self.canvas = Canvas(self.root, width=self.size, height=self.size, bg="white", bd=0)
        self.floor_image = PhotoImage(file = "floor.png")
        self.wall_image = PhotoImage(file = "wall.png")
        self.hero_down = PhotoImage(file = "hero-down.png")
        self.hero_up = PhotoImage(file = "hero-up.png")
        self.hero_right = PhotoImage(file = "hero-right.png")
        self.hero_left = PhotoImage(file = "hero-left.png")
        self.hero_images = {"down": self.hero_down,
                            "up": self.hero_up,
                            "right": self.hero_right,
                            "left": self.hero_left}
        self.skeleton_image = PhotoImage(file = "skeleton.png")
        self.boss_image = PhotoImage(file= "boss.png")
        self.canvas.pack()
        self.canvas.focus_set()    

    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                image = self.floor_image if map[i][j]==0 else self.wall_image
                self.tile = self.canvas.create_image(j*72, i*72, anchor=NW, image=image)
    
    def draw_entity(self, image, coords):
        self.entity = self.canvas.create_image(coords[0]*72, coords[1]*72, anchor=NW, image=image)
        return self.entity      
    
    def draw_stats(self, char, stats):
        text = ("{} (Level {}) HP: {}/{}| DP: {}| SP: {}".format(char,stats["level"],stats["currenthp"], stats["maxhp"],
                stats["dp"],stats["sp"]))
        if char == "Hero":
            self.canvas.create_text(5,650, anchor=NW, font=24, tag="hero_stats", text=text)
        else:
            self.canvas.create_text(715,650, anchor=NE, font=24, tag="monster_stats", text=text)

    def game_over(self):
        self.delete_stats()
        self.canvas.create_text(360,660, font=56, text="GAME OVER")
        self.canvas.create_text(360,680, font=56, text="Press 'x' to quit")

    def quit_app(self):
        self.root.destroy()
    
    def delete_stats(self):
        self.canvas.delete("monster_stats")
        self.canvas.delete("hero_stats")

    def death(self, char):
        self.canvas.delete(char.picture)
    
    def display(self):
        self.root.mainloop()