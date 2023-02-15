from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE, Scale, HORIZONTAL


# GUI graphical user interface
class FrontEnd:
    def __init__(self, master):
        self.master = master  # this is teh master window

        self.frame_header = ttk.Frame(self.master)  # first frame header
        self.frame_header.pack()

        self.logo = PhotoImage(file='logo.png').subsample(10, 10)
        print(self.logo)
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)

        ttk.Label(self.frame_header, text='Welcome to image editor app!').grid(row=0, column=1)
        ttk.Label(self.frame_header, text='Update, edit and save your images').grid(row=1, column=1)

        self.frame_menu = ttk.Frame(self.master)  # second frame header
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(
            50, 15))  # PADDING IS SPACE BETWEEN THE FRAMES, this make the menu to stands out

        ttk.Button(
            self.frame_menu, text='Upload image', command=self.upload_action).grid(row=0, column=0, padx=5, pady=5,
                                                                                   sticky='sw'
                                                                                   )

        ttk.Button(
            self.frame_menu, text='Apply filters', command=self.filter_action).grid(row=1, column=0, padx=5, pady=5,
                                                                                    sticky='sw'
                                                                                    )

        ttk.Button(
            self.frame_menu, text='Text action 1', command=self.text_action_1).grid(row=2, column=0, padx=5, pady=5,
                                                                                      sticky='sw'
                                                                                      )

        ttk.Button(
            self.frame_menu, text='Draw', command=self.draw_action).grid(row=3, column=0, padx=5, pady=5,
                                                                           sticky='sw'
                                                                           )

        ttk.Button(
            self.frame_menu, text='Crop', command=self.crop_action).grid(row=3, column=0, padx=5, pady=5,
                                                                           sticky='sw'
                                                                           )

        ttk.Button(
            self.frame_menu, text='Filter', command=self.filter_action).grid(row=4, column=0, padx=5, pady=5,
                                                                               sticky='sw'
                                                                               )

        ttk.Button(
            self.frame_menu, text='Blur', command=self.blur_action).grid(row=5, column=0, padx=5, pady=5,
                                                                           sticky='sw'
                                                                           )

        ttk.Button(
            self.frame_menu, text='Rotate', command=self.rotate_action).grid(row=6, column=0, padx=5, pady=5,
                                                                               sticky='sw'
                                                                               )

        ttk.Button(
            self.frame_menu, text='Flip', command=self.flip_action).grid(row=7, column=0, padx=5, pady=5,
                                                                           sticky='sw'
                                                                           )

        ttk.Button(
            self.frame_menu, text='Save', command=self.save_action).grid(row=8, column=0, padx=5, pady=5,
                                                                           sticky='sw'
                                                                           )

        ttk.Button(
            self.frame_menu, text='Adjust', command=self.adjust_action).grid(row=9, column=0, padx=5, pady=5,
                                                                               sticky='sw'
                                                                               )

        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()

        ttk.Button(self.apply_and_cancel, text='Apply', command=self.apply_action).grid(row=0, column=0, padx=5, pady=5,
                                                                                        sticky='sw')

        ttk.Button(self.apply_and_cancel, text='Cancel', command=self.cancel_action).grid(row=0, column=1, padx=5,
                                                                                          pady=5,
                                                                                          sticky='sw')

        ttk.Button(self.apply_and_cancel, text='Revert all changes', command=self.revert_action).grid(row=0, column=2,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky='sw')

        self.canvas = Canvas(self.frame_menu, bg='gray', width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)

    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass

        # self.canvas.unbind("<ButtonPress>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease>")
        # self.display_image(self.edited_image)
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

    def upload_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Please Upload an image").grid(row=0, column=0)

    def text_action_1(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text='Please enter a text').grid(row=0, column=0)

    def draw_action(self):
        pass

    def crop_action(self):
        pass

    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text='Negative', command=self.negative_action).grid(row=0,column=2,padx=5,pady=5,sticky='sw'
        )
        ttk.Button(
            self.side_frame, text='Black and White', command=self.bw_action).grid(row=1, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Stylisation', command=self.stylisation_action).grid(row=2, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Sketch Effect', command=self.sketch_action).grid(row=3, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Emboss', command=self.emb_action).grid(row=4, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Sepia', command=self.sepia_action).grid(row=5, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Binary Thresholding', command=self.binary_threshold_action).grid(row=6, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Erosion', command=self.erosion_action).grid(row=7, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )
        ttk.Button(
            self.side_frame, text='Dilation', command=self.dilation_action).grid(row=8, column=2, padx=5, pady=5,
                                                                                 sticky='sw'
                                                                                 )



    def blur_action(self):
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame, text="Averaging Blur"
        ).grid(row=0, column=2, padx=5, sticky='sw')

        self.average_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5, sticky='sw')

        ttk.Label(
            self.side_frame, text="Gaussian Blur"
        ).grid(row=2, colum=2, padx=5, sticky='sw')

        self.gaussian_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action
        )
        self.gaussian_slider.grid(row=3, column=2, padx=5, sticky='sw')


    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def save_action(self):
        pass

    def adjust_action(self):
        pass

    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        pass

    def negative_action(self):
        pass
    def bw_action(self):
        pass

    def stylisation_action(self):
        pass

    def sketch_action(self):
        pass

    def emb_action(self):
        pass

    def sepia_action(self):
        pass

    def binary_threshold_action(self):
        pass

    def erosion_action(self):
        pass

    def dilation_action(self):
        pass

    def averaging_action(self):
        pass

    def gaussian_action(self):
        pass

root = Tk()
FrontEnd(root)
root.mainloop()
