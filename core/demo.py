from tkinter import ttk, Tk, PhotoImage, RIDGE


# GUI graphical user interface
class FrontEnd:
    def __init__(self, master):
        self.master = master                   # this is teh master window

        self.frame_header = ttk.Frame(self.master)    # first frame header
        self.frame_header.pack()

        self.logo = PhotoImage(file='logo.png').subsample(10,10)
        print(self.logo)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)


        ttk.Label(self.frame_header, text='Welcome to image editor app!').grid(row=0, column=1)
        ttk.Label(self.frame_header, text='Update, edit and save your images').grid(row=1, column=1)

        self.frame_menu = ttk.Frame(self.master)                      # second frame header
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))  # PADDING IS SPACE BETWEEN THE FRAMES, this make the menu to stands out

        ttk.Button(
            self.frame_menu, text='Upload image', command=self.upload_action).grid(row=0, column=0, padx=5, pady=5,
                                                                                    sticky='sw'
                                                                                    )

        ttk.Button(
            self.frame_menu, text='Apply filters', command=self.filter_action).grid(row=1, column=0, padx=5, pady=5,
                                                                                    sticky='sw'
                                                                                    )

        ttk.Button(
            self.frame_menu, text='Text action 1', command=self.text_action_1()).grid(row=2, column=0, padx=5, pady=5,
                                                                                    sticky='sw'
                                                                                    )

        ttk.Button(
            self.frame_menu, text='Draw', command=self.draw_action()).grid(row=3, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Crop', command=self.crop_action()).grid(row=3, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Filter', command=self.filter_action()).grid(row=4, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Blur', command=self.blur_action()).grid(row=5, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Rotate', command=self.rotate_action()).grid(row=6, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Flip', command=self.flip_action()).grid(row=7, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Save', command=self.save_action()).grid(row=8, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Adjust', command=self.adjust_action()).grid(row=9, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

    def upload_action(self):
        pass

    def text_action_1(self):
        pass

    def draw_action(self):
        pass

    def crop_action(self):
        pass

    def filter_action(self):
        pass

    def blur_action(self):
        pass

    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def save_action(self):
        pass

    def adjust_action(self):
        pass


root = Tk()
FrontEnd(root)
root.mainloop()
