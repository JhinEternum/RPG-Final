import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from src.avatar.create_avatar import CreateAvatar
from src.home.home import Home
from src.item.create_item import CreateItem
from src.proficiency.proficiency_level import ProficiencyLevel


def check_frame_existence(frame) -> None:
    if frame is not None and frame.winfo_exists():
        frame.destroy()


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Game')

        self.resizable(False, False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frames = dict()

        self.home_frame = None
        self.create_avatar = None
        self.create_item = None

        self.frames = {
            Home: self.home_frame,
            CreateAvatar: self.create_avatar,
            CreateItem: self.create_item
        }

        self.home_frame = Home(
            parent=self,
            create_entity=self.create_entity_frame,
            proficiencies_level=self.show_proficiencies_level,
        )
        self.home_frame.grid(row=0, column=0, sticky='NSEW')

        self.frames = {
            Home: self.home_frame,
            CreateAvatar: self.create_avatar,
            CreateItem: self.create_item
        }

        self.show_frame(Home)

    def show_frame(self, container_class) -> None:
        frame = self.frames[container_class]
        frame.tkraise()

    def create_entity_frame(self, **kwargs) -> None:
        container = kwargs['container']
        container_class = kwargs['container_class']
        extra_frame = kwargs['extra_frame'] if 'extra_frame' in kwargs else None

        check_frame_existence(container)

        container = container_class(parent=self, home=lambda: self.show_frame(Home), extra_frame=extra_frame)
        container.grid(row=0, column=0, sticky='NSEW')

        self.frames[container_class] = container
        self.show_frame(container_class)

        self.set_frames_to_attributes(container_class, container)

    def set_frames_to_attributes(self, container_class, container):
        if container_class == CreateAvatar:
            self.create_avatar = container
        elif container_class == CreateItem:
            self.create_item = container

    def show_proficiencies_level(self, **kwargs) -> None:
        # proficiencies: list, proficiency_result: list, edit: EditUser = None, user_proficiencies: list = None
        # ProficiencyLevel(self, proficiencies, proficiency_result, self.create_avatar_frame, edit, user_proficiencies)
        ProficiencyLevel(parent=self, create_avatar=self.create_avatar, **kwargs)


root = Game()

style = ttk.Style(root)

font.nametofont('TkDefaultFont').configure(size=12)

root.mainloop()
