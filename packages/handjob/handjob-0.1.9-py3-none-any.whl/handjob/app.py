# !/usr/bin/env python3
# !/usr/bin/env python2

import os
from tkinter import *
from tkinter import filedialog

import cv2
from PIL import ImageTk, Image


class Record:
    file_path: str = ''
    label: str = ''

    def __init__(self, file_path, label):
        super().__init__()
        self.file_path = file_path
        self.label = label


class BasicGUI:
    index: int = 0
    files: [str] = []
    records: [] = []

    input_dir: str = ''
    output_dir: str = ''

    first_load: bool = True
    image: any
    canvas: Canvas
    canvas_image: any
    entry: Text

    def __init__(self, master):
        self.master = master
        self.master.title('Handwriting Labeling Job')
        self.master.bind('<KeyRelease>', self.key_up)

        # create frame and key listener
        self.frame = Frame(master, bg='green')
        self.frame.pack(expand=True, fill=BOTH)
        self.frame.pack()

        # create label
        self.label_record = Label(self.frame, text='Total records: 0')
        self.label_record.pack()

        # create entry for folder input
        self.entry_folder = Entry(self.frame, width='600', font=('Verdana', 15))
        self.entry_folder.insert(0, 'Images directory path...')
        self.entry_folder.bind("<1>", self.browse_folder_input)
        self.entry_folder.pack()

        # create entry for output label.txt
        self.entry_output_folder = Entry(self.frame, width='600', font=('Verdana', 15))
        self.entry_output_folder.insert(0, 'Path to label file...')
        self.entry_output_folder.bind("<1>", self.browse_folder_output)
        self.entry_output_folder.pack()

        # store absolute path option
        self.checker = IntVar()
        self.checker.set(0)
        self.checkbox = Checkbutton(self.frame, variable=self.checker, onvalue=1, offvalue=0,
                                    text='Store absolute path')
        self.checkbox.pack()

    def browse_folder_input(self, event):
        folder = filedialog.askdirectory()
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, folder)
        self.load_files()

    def browse_folder_output(self, event):
        self.output_dir = filedialog.askdirectory()
        self.entry_output_folder.delete(0, END)
        self.entry_output_folder.insert(0, self.output_dir)

        # reload records
        self.read_output_file()
        self.set_default_label()

    def load_canvas(self):

        # get first image
        image, width, height = self.set_image()

        self.image = image

        # create canvas
        self.canvas = Canvas(self.frame, width=width, height=height)
        self.canvas.pack()

        self.canvas_image = self.canvas.create_image(
            0, 0, anchor=NW, image=image)

        # create input
        self.entry = Text(self.frame, height=40, width=600, font=("Arial", 25))
        self.entry.pack(ipady=10)

        return width, height

    def load_files(self):
        self.input_dir = self.entry_folder.get()
        self.output_dir = self.entry_output_folder.get()
        self.files = []

        allowed_ext = ['.jpg', '.jpeg', '.png']

        self.files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(self.input_dir) for f in filenames if
                      os.path.splitext(f)[1] in allowed_ext]

        # reload canvas
        if self.first_load and len(self.files) != 0:
            width, height = self.load_canvas()
            self.first_load = False
            self.update_frame_size(width, height)

        # set value of first entry if any (must load after canvas)
        self.set_default_label()

    def get_output_filename(self):
        out_file_name = os.path.basename(os.path.normpath(self.input_dir))
        out_file = os.path.join(self.output_dir, out_file_name + '.txt')
        return out_file

    def key_up(self, event):

        if event.keycode == 113 or event.keycode == 114:
            if event.keycode == 113:  # arrow left
                self.prev_image()

            if event.keycode == 114:  # arrow right
                self.next_image()

        if event.keycode == 36 and len(self.files):  # enter
            self.write_file()
            self.next_image()
            self.set_label_record()

        if event.keycode == 9:  # esc
            self.master.destroy()

    def prev_image(self):
        self.index = self.index - 1
        if self.index < 0:
            self.index = len(self.files) - 1
        self.load_navigate_image()

    def next_image(self):
        self.index = self.index + 1
        if self.index > len(self.files) - 1:
            self.index = 0
        self.load_navigate_image()

    def write_file(self):
        label = self.entry.get("1.0", "end-1c")
        label = label.replace('\n', '')

        image_path = self.files[self.index]

        index = self.find_record(image_path)

        if index == -1:
            self.records.append(Record(image_path, label))
        else:
            self.records[index] = Record(image_path, label)

        # dump to files
        self.dump_to_file()

    def load_navigate_image(self):
        if len(self.files) == 0:
            return

        image, width, height = self.set_image()

        self.update_frame_size(width, height)

        self.image = image
        self.canvas.itemconfig(self.canvas_image, image=self.image)

        # set old label
        self.set_default_label()

    def set_default_label(self):

        if len(self.files) == 0:
            return

        image_path = self.files[self.index]
        index = self.find_record(image_path)

        label = ''

        if index != -1:
            record = self.records[index]
            label = record.label
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', label)

    def dump_to_file(self):
        out_file = self.get_output_filename()
        file = open(out_file, 'w')

        content = ''
        for record in self.records:
            relative_path = os.path.relpath(record.file_path, self.output_dir)
            image_path = record.file_path if self.checker.get() == 1 else relative_path
            content = content + '{}\t{}\n'.format(image_path, record.label)

        file.write(content)
        file.close()

    def update_frame_size(self, width, height):
        self.master.geometry('{}x{}'.format(width, height + 45 * 3))
        self.canvas.config(width=width, height=height)
        self.entry.config(width=width)

    def set_image(self):

        image_path = self.files[self.index]

        # resize image
        image = cv2.imread(image_path)

        h, w, c = image.shape
        fixed_height = h + 60 if h < 600 else 600
        image = BasicGUI.resize(image, height=fixed_height)

        if fixed_height == 600:
            image = cv2.putText(image, image_path, (20, 20), 0, 0.5, (255, 255, 255))

        # turn to correct color space
        b, g, r = cv2.split(image)
        image = cv2.merge((r, g, b))

        # convert to tk image
        h, w, c = image.shape
        # fixed_width = 600 if fixed_height < 600 else w

        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        return image, w, h

    @staticmethod
    def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
        (h, w) = image.shape[:2]
        if width is None and height is None:
            return image

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)

    # parse label files and check for duplicate file path for update
    def read_output_file(self):
        file_path = self.get_output_filename()

        if len(self.files) == 0 or not os.path.exists(file_path):
            return

        file = open(file_path, 'r')
        content = file.read()

        lines = content.split('\n')
        records = list(map(lambda line: line.split('\t'), lines))
        records = list(filter(lambda record: len(record) == 2, records))

        # convert relative path to absolute path
        os.chdir(self.output_dir)
        records = list(map(lambda record: [os.path.abspath(record[0]), record[1]], records))

        print('Records in label file: ')
        print('\n'.join(list(map(lambda record: record[0], records))))

        records = list(map(lambda record: Record(record[0], record[1]), records))

        self.records = records

        self.set_label_record()

    def set_label_record(self):
        label_content = '{} records / {} images'.format(len(self.records), len(self.files))
        self.label_record.config(text=label_content)

    def find_record(self, file_path) -> int:
        for idx, val in enumerate(self.records):
            if val.file_path != file_path:
                continue
            return idx
        return -1


class Executable:

    @staticmethod
    def run():
        root = Tk()
        root.geometry('500x700')

        gui = BasicGUI(root)
        root.mainloop()


Executable.run()
