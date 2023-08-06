#####################################################################################################
#####################################################################################################
#################   _____ ____________ ______ ______          _                     #################
#################  |  ___|___  /| ___ \___  / | ___ \        | |                    #################
#################  | |__    / / | |_/ /  / /  | |_/ /_ _  ___| | ____ _  __ _  ___  #################
#################  |  __|  / /  |  __/  / /   |  __/ _` |/ __| |/ / _` |/ _` |/ _ \ #################
#################  | |___./ /___| |   ./ /___ | | | (_| | (__|   < (_| | (_| |  __/ #################
#################  \____/\_____/\_|   \_____/ \_|  \__,_|\___|_|\_\__,_|\__, |\___| #################
#################                                                        __/ |      #################
#################                                                       |___/       #################
#################                                                                   #################
#################                                        Author: Jacob Brehm (2019) #################
#####################################################################################################
#####################################################################################################

## GUI PACKAGES
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import filedialog as fd
from tkinter import messagebox as mb

#####################################################################################################
#################                            GUI BUILDING                           #################
#####################################################################################################

class Application(tk.Frame):

    def __init__(self, *args, padding=None, center=True, **kwargs):

        self.center = center

        self.root = tk.Tk()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        tk.Frame.__init__(self, *args, master=self.root, **kwargs)

        if padding and type(padding) == int:
            padx = padding
            pady = padding
        elif padding and type(padding) == tuple:
            padx = padding[0]
            pady = padding[1]
        else:
            padx = 0
            pady = 0

        self.grid(row=0, column=0, padx=padx, pady=pady, sticky='NSEW')
        self.grid_columnconfigure(0, weight=1)

    def configure(self, title=None, icon=None, resizable=None):
        self.root.title(title)

        if icon: self.root.iconbitmap(default=icon)

        if resizable and type(resizable) == bool:
            self.root.resizable(width=True, height=True)
        elif not resizable and type(resizable) == bool:
            self.root.resizable(width=False, height=False)
        elif resizable and type(resizable) == tuple and len(resizable) == 2:
            self.root.resizable(width=resizable[0], height=resizable[1])

    def geometry(self, width, height):
        self.root.geometry(f'{width}x{height}')

    def _position(self, center=True):
        if center: CenterWindow(self.root)

    def bind(self, key, command):
        self.root.bind(key, command)

    @property
    def parent(self):
        return self.root

    def mainloop(self):
        self._position(self.center)
        self.root.mainloop()


class Header(tk.Frame):

    def __init__(self, *args, logo=None, downscale=None, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        logo_title = tk.Frame(self)
        logo_title.grid_columnconfigure(0, weight=1)
        logo_title.grid(row=0, column=0, sticky='EW')

        if logo:
            try:
                logo_render = RenderImage(logo, downscale=downscale)
                title = ttk.Label(logo_title, image=logo_render)
                title.photo = logo_render
            except FileNotFoundError:
                title = ttk.Label(logo_title, text=logo, font=('Helvetica', 22, 'bold'))
        else:
            title = ttk.Label(logo_title, text='EZPZ', font=('Helvetica', 22, 'bold'))
        title.grid(row=0, column=0, padx=10)

        self.grid_columnconfigure(0, weight=1)


class Separator(tk.Frame):

    def __init__(self, *args, padding=None, orientation='horizontal', **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        if padding and type(padding) == int:
            padx = (padding, padding)
            pady = (padding, padding)
        elif padding and type(padding) == tuple:
            if type(padding[0]) == tuple and len(padding[0]) == 2:
                padx = padding[0]
            else:
                padx = (padding[0], padding[0])

            if type(padding[1]) == tuple and len(padding[1]) == 2:
                pady = padding[1]
            else:
                pady = (padding[1], padding[1])
        else:
            padx = (0, 0)
            pady = (0, 0)

        sticky = 'EW' if orientation == 'horizontal' else 'NS'
        separator = ttk.Separator(self, orient=orientation)
        separator.grid(row=0, column=0, padx=padx, pady=pady, sticky=sticky)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class PaddedFrame(tk.Frame):

    def __init__(self, *args, padding=20, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)
        self.grid(padx=padding, pady=padding)


# class PaddedLabelFrame(tk.Frame):

#     # def __init__(self, *args, padding=20, **kwargs):
#     def __init__(self, master, text=None, padding=20, **kwargs):

#         master = args[0]
#         args = args[1:]

#         container = tk.LabelFrame(master, text=text)
#         container.grid()

#         tk.Frame.__init__(self, *args, **kwargs)
#         self.grid(padx=padding, pady=padding)


class Space(tk.Frame):

    def __init__(self, *args, row, column, padding=None,
                 rowspan=None, columnspan=None, **kwargs):

        tk.Frame.__init__(self, *args, height=padding, width=padding, **kwargs)
        self.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='NSEW')


class InputField(tk.Frame):

    def __init__(self, *args, quantity, appearance='entry', fullpath=True, width=40,
                 title='Select the input', image=None, command=None, filetypes=None, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        self.quantity = quantity
        self.appearance = appearance
        self.width = width
        self.fullpath = fullpath
        self.title = title
        self.image = image
        self.command = command
        self.filetypes = filetypes

        self.inputs = []

        if self.appearance == 'entry':
            self.label = ttk.Label(self, text='Input location:')
            self.label.grid(row=0, column=0, sticky='EW')
            self.field = ttk.Entry(self, takefocus=False, width=self.width, state='readonly')
            self.field.grid(row=1, column=0, padx=(0,2), sticky='EW')
            button = ttk.Button(self, takefocus=False, text='Browse...', image=self.image,
                                command=self.Browse)
            button.grid(row=1, column=1, sticky='NSEW')
            self.columnconfigure(0, weight=1)

        elif self.appearance == 'list':
            self.field = tk.Listbox(self, state='normal', height=5, width=self.width,
                                   justify='center')
            self.field.grid(row=1, column=0, padx=(0,2), sticky="EW")
            info = ['',
                    '',
                    ' Selecting multiple files is optional.',
                    '',
                    '']
            [self.field.insert('end', item) for item in info]
            self.field.config(state='disabled')

            controls = tk.Frame(self)
            button = ttk.Button(controls, takefocus=False, text='Browse...', image=self.image,
                                command=self.Browse)
            button.grid(row=0, column=0, sticky="NSEW")
            controls.grid_rowconfigure(0, weight=1)
            controls.grid(row=1, column=1, sticky="NSEW")

        self.grid_columnconfigure(0, weight=1)

    def Browse(self):

        if self.quantity == 'single':
            if self.filetypes is None:
                file = fd.askopenfilename(title=self.title)
            else:
                file = fd.askopenfilename(title=self.title, filetypes=self.filetypes)
            if file:
                self.field.config(state='normal')
                self.field.delete(0, 'end')
                if self.fullpath:
                    self.field.insert(0, file)
                else:
                    filename = file.split('/')[-1]
                    self.field.insert(0, filename)
                self.field.config(state='readonly')
                self.field.update_idletasks()
                self.field.xview_moveto(1)
            self.inputs = file

        elif self.quantity == 'multiple':
            if self.filetypes is None:
                files = fd.askopenfilenames(title=self.title)
            else:    
                files = fd.askopenfilenames(title=self.title, filetypes=self.filetypes)
            if files:
                self.inputs = list(files)
                self.field.config(state='normal')
                self.field.delete(0, 'end')

                for file in self.inputs:
                    display = ' ' + ( file if self.fullpath else file.split('/')[-1] )
                    if self.appearance == 'entry': display += ';'
                    self.field.insert('end', display)
                if self.appearance == 'entry':
                    text = self.field.get()[:-1]
                    self.field.delete(0, 'end')
                    self.field.insert(0, text)

                if self.appearance == 'entry':
                    self.field.config(state='readonly')
                    self.field.update_idletasks()
                    self.field.xview_moveto(1)
                elif self.appearance == 'list':
                    self.field.config(state='disabled')
                    self.field.config(justify='left')

        if self.command: self.command()

    def clear(self):
        self.field.config(state='normal')
        self.field.delete(0, 'end')
        self.field.config(state='readonly' if self.quantity == 'single' else 'disabled')
        self.inputs = []

    def get(self):
        return self.inputs


class OutputField(tk.Frame):

    def __init__(self, *args, quantity, filetypes=None, default=None, fullpath=True,
                 title='Choose output destination', **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        self.quantity = quantity
        self.filetypes = filetypes
        self.default = default
        self.fullpath = fullpath
        self.title = title

        self.output = None

        if self.filetypes is None: self.filetypes = ()
        if self.default is None: self.default = ()

        self.label = ttk.Label(self, text='Output destination:')
        self.label.grid(row=0, column=0, sticky='EW')
        self.entry = ttk.Entry(self, takefocus=False, state='readonly')
        self.entry.grid(row=1, column=0, padx=(0,2), sticky='EW')
        button = ttk.Button(self, takefocus=False, text='Browse...', command=self.Browse)
        button.grid(row=1, column=1, sticky='NSEW')
        self.columnconfigure(0, weight=1)

    def Browse(self):

        if self.quantity == 'saveas':
            self.output = fd.asksaveasfilename(title=self.title,
                                               filetypes=self.filetypes,
                                               defaultextension=self.default)
            if self.output:
                self.entry.config(state='normal')
                self.entry.delete(0, 'end')
                if self.fullpath:
                    self.entry.insert(0, self.output)
                else:
                    filename = self.output.split('/')[-1]
                    self.entry.insert(0, filename)
                # self.entry.insert(0, self.output)
                self.entry.config(state='readonly')
                self.entry.update_idletasks()
                self.entry.xview_moveto(1)

        elif self.quantity == 'directory':
            self.output = fd.askdirectory(title=self.title)
            if self.output:
                self.entry.config(state='normal')
                self.entry.delete(0, 'end')
                self.entry.insert(0, self.output)
                self.entry.config(state='readonly')
                self.entry.update_idletasks()
                self.entry.xview_moveto(1)

    def get(self):
        return self.output


class ScrollableTab(tk.Frame):

    def __init__(self, notebook, title, *args, cheight=False, cwidth=False, **kwargs):

        self.notebook = notebook

        parent_name = self.notebook.winfo_parent()
        parent = self.notebook._nametowidget(parent_name)

        self.frame = tk.Frame(parent)
        self.frame.columnconfigure(0, weight=1)
        self.notebook.add(self.frame, text=title)

        self.canvas = tk.Canvas(self.frame, bd=0, highlightthickness=0)
        if cwidth: self.canvas.config(width=cwidth)
        if cheight: self.canvas.config(height=cheight)
        self.scrollbar = tk.Scrollbar(self.frame)
        self.canvas.grid(row=0, column=0, sticky='NSEW')
        self.scrollbar.grid(row=0, column=1, sticky='NSE')

        tk.Frame.__init__(self, *args, master=self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self, anchor='nw', tags='window')
        self.columnconfigure(0, weight=1)
        if cwidth: self.columnconfigure(0, minsize=cwidth)

        self.bind('<Visibility>', self.update)
        self.bind('<Configure>', self.update)

    def scroll(self):

        def EnterCanvas(event):
            self.canvas.bind_all('<MouseWheel>', ScrollCanvas)

        def LeaveCanvas(event):
            self.canvas.unbind_all('<MouseWheel>')

        def ScrollCanvas(event):
            self.canvas.yview_scroll(int(-1*(event.delta/2)), 'units')

        self.frame.bind('<Enter>', EnterCanvas)
        self.frame.bind('<Leave>', LeaveCanvas)

    def update(self, event=None):
        self.update_idletasks()
        self.canvas.itemconfig(
            'window',
            # height=self.canvas.winfo_height(),
            width=self.canvas.winfo_width(),
        )
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        if self.canvas.bbox('all')[-1] > self.canvas.winfo_height():
            self.scrollbar['command'] = self.canvas.yview
            self.canvas.config(yscrollincrement=1)
            self.scroll()
        else:
            self.frame.unbind('<Enter>')
            self.frame.unbind('<Leave>')
            self.canvas.unbind_all('<MouseWheel>')



class ScrollableFrame(ScrollableTab):

    def __init__(self, master, *args, cheight=False, cwidth=False, **kwargs):

        parent = master

        self.frame = tk.Frame(parent)
        self.frame.columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.frame, bd=0, highlightthickness=0)
        if cwidth: self.canvas.config(width=cwidth)
        if cheight: self.canvas.config(height=cheight)
        self.scrollbar = tk.Scrollbar(self.frame)
        self.canvas.grid(row=0, column=0, sticky='NSEW')
        self.scrollbar.grid(row=0, column=1, sticky='NSE')

        tk.Frame.__init__(self, *args, master=self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self, anchor='nw', tags='window')
        self.columnconfigure(0, weight=1)
        if cwidth: self.columnconfigure(0, minsize=cwidth)

        self.back_frame = tk.Frame(self.canvas)
        self.back_frame['width'] = self['width']
        self.back_frame['height'] = self['height']

        self.bind('<Visibility>', self.update)
        self.bind('<Configure>', self.update)

    def grid(self, *args, **kwargs):
        self.frame.grid(*args, **kwargs)

    def grid_remove(self, *args, **kwargs):
        self.frame.grid_remove()
        

    # def __getattr__(self, name):
    #     # print(type(name))
    #     # def wrapper(*args, **kwargs):
    #     #     # print(f'{name} was called')
    #     #     getattr()
    #     # return wrapper
    #     print(name)
    #     # if name == 'grid':
    #     #     print('nice')
    #         # print(getattr(self.frame, name))


class StatusBar(tk.Frame):

    def __init__(self, *args, panels=1, weight=None, update=False, **kwargs):

        self.update = update

        if weight is not None and len(weight) != panels:
            raise ValueError('Number of items in the weight tuple does not ' \
                'match the number of panels.')

        tk.Frame.__init__(self, *args, **kwargs)
        for column in range(panels):
            self.columnconfigure(column, weight=weight[column] if weight else 1)

        self._texts = []
        self._labels = []
        for panel in range(panels):
            text_variable = tk.StringVar()
            label = tk.Label(self, textvariable=text_variable, relief='sunken')
            label.grid(row=0, column=panel, sticky='EW')
            self._texts.append(text_variable)
            self._labels.append(label)

    def _update(self):
        longest, index = None, None
        for t, text in enumerate(self._texts):
            if longest is None or ( len(text.get()) > longest ):
                longest, index = len(text.get()), t
        for label in self._labels: label['width'] = longest

    def get(self, number):
        return self._texts[number-1].get()[1:]

    def set(self, number, text):
        self._texts[number-1].set(f' {text}')
        if self.update: self._update()


#####################################################################################################
#################                           GUI FUNCTIONS                           #################
#####################################################################################################

def CenterWindow(window):
    window.update()
    X_POSITION = ( window.winfo_screenwidth() - window.winfo_width() ) // 2
    Y_POSITION = ( window.winfo_screenheight() - window.winfo_height() ) // 2
    window.geometry("+" + str(int(X_POSITION)) + "+" + str(int(Y_POSITION)))


def GetRoot(widget):
    root = widget.nametowidget(widget.winfo_toplevel())
    while not isinstance(root, tk.Tk):
        root = root.nametowidget(root.winfo_parent())
    return root


def GetApplication(widget):
    root = GetRoot(widget)
    for child in root.winfo_children():
        if isinstance(child, Application):
            return child


def ResourcePath(relative_path):
    import sys, os
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath('__main__')))
    return os.path.join(base_path, relative_path)


def RenderImage(filepath, downscale=None):
    from PIL import Image, ImageTk
    # First load in order to get dimensions of the image
    loaded = Image.open(ResourcePath(filepath))
    render = ImageTk.PhotoImage(loaded)
    width = render.width()
    height = render.height()
    # Second load in order to resize the original image
    # This was done because only ImageTk has width and height methods
    if downscale and ( type(downscale) == int or type(downscale) == float ):
        scaled_width =  int( width / downscale )
        scaled_height = int( height / downscale )
        loaded = loaded.resize((scaled_width, scaled_height), Image.ANTIALIAS)
    elif downscale and type(downscale) == tuple and len(downscale) == 2:
        width_scale = downscale[0]
        height_scale = downscale[1]
        scaled_width = int( width / width_scale )
        scaled_height = int( height / height_scale )
        loaded = loaded.resize((scaled_width, scaled_height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(loaded)
    return render


#####################################################################################################
#####################################################################################################
##############################  ______ _       _     _              _  ##############################
##############################  |  ___(_)     (_)   | |            | | ##############################
##############################  | |_   _ _ __  _ ___| |__   ___  __| | ##############################
##############################  |  _| | | '_ \| / __| '_ \ / _ \/ _` | ##############################
##############################  | |   | | | | | \__ \ | | |  __/ (_| | ##############################
##############################  \_|   |_|_| |_|_|___/_| |_|\___|\__,_| ##############################
##############################                                         ##############################
#####################################################################################################
#####################################################################################################