import tkinter
from tkinter import IntVar
import customtkinter
import dataCollection

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    n = 0

    def __init__(self):
        super().__init__()
        self.title("Media Controller Using Hand Gestures")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Customize",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="TrainData", command=self.Traindata)
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Datacollection",
                                                        command=self.Collectdata)
        self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Test", command=self.test)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.update_main_frame()

    

    def update_main_frame(self):
        if App.n == 0:
            self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew" )
            self.main_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Start",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Start", command=self.Collectdata,width=200,height=90,font=customtkinter.CTkFont(size=30, weight="bold"),fg_color="green",text_color="white")
            self.start_button.grid(row=1, column=1, padx=290, pady=190)
        elif App.n == 1:
            self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.main_frame.grid(row=0, column=1, rowspan=6, sticky="nsew")
            self.main_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Data Collection",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=4, columnspan=10, padx=50, pady=(20, 10), sticky="w")

            # Back to start button
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)

            self.radiobutton_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.radiobutton_frame.grid(row=0, column=1, rowspan=10, padx=20, pady=0,sticky="nsew")
            # self.radio_var = tkinter.IntVar(value=0)
            self.radio_var = tkinter.StringVar(value="Play")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Collect Data", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            
            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.radiobutton_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)

            self.radio_button_1 = customtkinter.CTkRadioButton(self.radiobutton_frame, variable=self.radio_var, value="Play", text="Play", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Pause", text="Pause", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_2.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")

            self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="FastForward", text="FastForward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_3.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
            
            self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Backward", text="Backward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_4.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")

            self.save_button = customtkinter.CTkButton(self.radiobutton_frame, text="Collect and Save", command=self.save)
            self.save_button.grid(row=6, column=0, padx=10, pady=25)

        elif App.n == 2:
            self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.main_frame.grid(row=0, column=1, rowspan=6, sticky="nsew")
            self.main_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Train Data",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)
        elif App.n == 3:
            self.main_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.main_frame.grid(row=0, column=1, rowspan=6, sticky="nsew")
            self.main_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Test",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)

    
    def start_page(self):
        App.n = 0
        self.update_main_frame()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Welcome to Hand Gesture Media Controller", title="CTkInputDialog")
        print("Welcome to Hand Gesture Media Controller")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def Traindata(self):
        App.n = 2
        self.update_main_frame()
    
    def Collectdata(self):
        App.n = 1
        self.update_main_frame()

    def test(self):
        App.n = 3
        self.update_main_frame()

    def save(self):
        dataCollection.datacollection(self.radio_var.get())
        print(self.radio_var.get(),"Media Collected")
        App.n = 1
        self.update_main_frame()


if __name__ == "__main__":
    app = App()
    app.mainloop()
