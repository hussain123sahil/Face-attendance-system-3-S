import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x840")
        self.root.title("Face Attendance System")

        # Paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.student_file_path = os.path.join(current_dir, "student.py")
        image_dir = os.path.join(current_dir, "college_images")

        # Define constants
        button_width = 150
        button_height = 150
        button_padx = 50
        button_pady = 50
        label_height = 55

        # Background image
        bg_img = Image.open(os.path.join(image_dir, "face.jpg"))
        bg_img = bg_img.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg3)
        bg_label.place(x=0, y=label_height, width=1310, height=710)

        title_lbl = Label(bg_label, text="Face Recognition Attendance System Software", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=-130, y=0, width=1530, height=label_height)

        # Buttons
        button_images = [
            "student_icon.png",
            "student_icon.png",
            "student_icon.png",
            "student_icon.png",
            "student_icon.png",
            "student_icon.png",
            "student_icon.png",
            "student_icon.png"
        ]
        button_texts = [
            "Student Details",
            "Face Detector",
            "Attendance",
            "Help Desk",
            "Train Data",
            "Photos",
            "Developers",
            "Exit"
        ]
        button_commands = [
            self.open_student_details,
            self.face_detector,
            self.attendance,
            self.help_desk,
            self.train_data,
            self.photos,
            self.developers,
            root.quit
        ]
        for i, (image, text, command) in enumerate(zip(button_images, button_texts, button_commands)):
            img = Image.open(os.path.join(image_dir, image))
            img = img.resize((button_width, button_height), Image.ANTIALIAS)
            photo_img = ImageTk.PhotoImage(img)

            row = i // 4
            col = i % 4

            b = Button(bg_label, image=photo_img, cursor="hand2", command=command)
            b.image = photo_img  # To prevent garbage collection
            b.place(x=200 + col * (button_width + button_padx), y=100 + row * (button_height + button_pady), width=button_width, height=button_height)

            b1_1 = Button(bg_label, text=text, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white", command=command)
            b1_1.place(x=200 + col * (button_width + button_padx), y=100 + row * (button_height + button_pady) + button_height, width=button_width, height=40)

    def open_student_details(self):
        os.system(f'python {self.student_file_path}')

    def face_detector(self):
        pass

    def attendance(self):
        pass

    def help_desk(self):
        pass

    def train_data(self):
        pass

    def photos(self):
        pass

    def developers(self):
        pass


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
