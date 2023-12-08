# TODO: Add calibration mode
import tkinter as tk
import customtkinter
import csv

# default themes for the program
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

hca_storage_reader = csv.reader(open('hca_storage.csv', 'r'))
hca_dict = {}
for hca_storage_row in hca_storage_reader:
    k, v = hca_storage_row
    hca_dict[k] = v
print(hca_dict)


# - Create popup window for creating/selecting a profile and input of study/profile name
class ProfileWindow(customtkinter.CTkToplevel):

    switch_change_profile_state = None

    def __init__(self):
        super().__init__()
        HCAControl.placeholder_function()

        self.title("Study and Filename Setup")
        self.geometry("650x200")
        self.resizable(False, False)

        # -- create frame for "Study and Filename Setup" window
        self.frame_study = customtkinter.CTkFrame(self)
        self.frame_study.grid(row=5, column=3, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- create modules for "Study and Filename Setup" window
        self.label_study_name = customtkinter.CTkLabel(self.frame_study, text="Study Name:", anchor="w")
        self.entry_study_name = tk.StringVar()
        self.entry_study_name.set("UWT Sampling Plan")
        self.entry_study_name = customtkinter.CTkEntry(self.frame_study, width=500, state="disabled",
                                                       font=customtkinter.CTkFont(slant="italic"),
                                                       textvariable=self.entry_study_name)
        self.label_profile_name = customtkinter.CTkLabel(self.frame_study, text="Profile Name:", anchor="w")
        self.entry_profile_name = tk.StringVar()
        self.entry_profile_name.set(" UWT_HCA_WD00_S1_x=235_z=0")
        self.entry_profile_name = customtkinter.CTkEntry(self.frame_study, width=500, state="disabled",
                                                         font=customtkinter.CTkFont(slant="italic"),
                                                         textvariable=self.entry_profile_name)
        self.label_new_study_name = customtkinter.CTkLabel(self.frame_study, text="New Study Name:", anchor="w")
        self.entry_new_study_name = tk.StringVar()
        self.entry_new_study_name.set("UWT Sampling Plan")
        self.entry_new_study_name = customtkinter.CTkEntry(self.frame_study, width=500,
                                                           textvariable=self.entry_new_study_name)
        self.label_new_profile_name = customtkinter.CTkLabel(self.frame_study, text="New Profile Name:", anchor="w")
        self.entry_new_profile_name = tk.StringVar()
        self.entry_new_profile_name.set(" UWT_HCA_WD00_S1_x=235_z=0")
        self.entry_new_profile_name = customtkinter.CTkEntry(self.frame_study, width=500,
                                                             textvariable=self.entry_new_profile_name)
        # TODO: Switch does not work, throws error
        self.switch_change_profile_state = customtkinter.StringVar(value="on")
        self.switch_change_profile_name = customtkinter.CTkSwitch(self.frame_study,
                                                                  text="Change Study and Profile Name",
                                                                  command=HCAControl.switch_event_3,
                                                                  variable=self.switch_change_profile_state,
                                                                  onvalue="on", offvalue="off")
        # TODO: This button is executing immediately upon opening window, but also works properly when clicked
        self.button_accept_profile = customtkinter.CTkButton(self.frame_study, text='Accept', fg_color="OliveDrab4",
                                                             hover_color="dark olive green",
                                                             command=HCAControl.placeholder_function)

        self.label_study_name.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.entry_study_name.grid(row=0, column=1, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_profile_name.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.entry_profile_name.grid(row=1, column=1, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_study_name.grid(row=2, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_study_name.grid(row=2, column=1, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_profile_name.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_profile_name.grid(row=3, column=1, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.switch_change_profile_name.grid(row=4, column=0, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.button_accept_profile.grid(row=4, column=2, padx=0, pady=(10, 10), sticky="nsew")


class HCAControl(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # - configure gui
        # -- configure window
        self.title("hca_control")
        self.geometry(f"{1250}x{750}")
        self.resizable(True, True)

        # -- configure grid layout (3x3)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)
        self.grid_rowconfigure(2)

        self.profile_window = None

        # - left sidebar widgets
        # -- create frame for left sidebar widgets
        self.frame_sidebar = customtkinter.CTkFrame(self)
        self.frame_sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")
        # self.frame_sidebar.grid_rowconfigure(4, weight=1)

        # -- left sidebar labels
        self.label_logo = customtkinter.CTkLabel(self.frame_sidebar, text="HCA Controls",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_version = customtkinter.CTkLabel(self.frame_sidebar, text="Version 20231208 ",
                                                    font=customtkinter.CTkFont(slant="italic"))
        self.label_appearance = customtkinter.CTkLabel(self.frame_sidebar, text="Appearance Mode:", anchor="w")
        # self.scaling_label = customtkinter.CTkLabel(self.frame_sidebar, text="UI Scaling:", anchor="w")

        # -- left sidebar buttons
        self.button_zero = customtkinter.CTkButton(self.frame_sidebar, text='Zero', command=self.placeholder_function)
        self.button_span = customtkinter.CTkButton(self.frame_sidebar, text='Span', command=self.placeholder_function)
        self.button_background = customtkinter.CTkButton(self.frame_sidebar, text='Background',
                                                         command=self.placeholder_function)
        self.button_start_run = customtkinter.CTkButton(self.frame_sidebar, text='Start Sample Run',
                                                        fg_color="OliveDrab4", hover_color="dark olive green",
                                                        command=self.placeholder_function)
        self.button_process_data = customtkinter.CTkButton(self.frame_sidebar, text='Process Data',
                                                           command=self.placeholder_function)
        self.button_select_profile = customtkinter.CTkButton(self.frame_sidebar, text='Select Profile',
                                                             command=self.open_profile_window)
        self.button_quit_processing = customtkinter.CTkButton(self.frame_sidebar, text='Quit Processing',
                                                              hover_color="red4", fg_color="red3",
                                                              command=self.placeholder_function)

        # -- left sidebar menus
        self.menu_appearance = customtkinter.CTkOptionMenu(self.frame_sidebar, values=["Light", "Dark", "System"],
                                                           command=self.change_appearance_mode_event)

        # -- left sidebar widget positioning
        self.label_logo.grid(row=0, column=0, padx=20, pady=(20, 5))
        self.label_version.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="n")
        self.button_zero.grid(row=3, column=0, padx=20, pady=(0, 10))
        self.button_span.grid(row=4, column=0, padx=20, pady=(0, 10))
        self.button_background.grid(row=5, column=0, padx=20, pady=(0, 10))
        self.button_start_run.grid(row=6, column=0, padx=20, pady=(0, 10))
        self.button_process_data.grid(row=7, column=0, padx=20, pady=(0, 10))
        self.button_select_profile.grid(row=8, column=0, padx=20, pady=(0, 10))
        self.button_quit_processing.grid(row=9, column=0, padx=20, pady=(0, 10))
        self.label_appearance.grid(row=10, column=0, padx=20, pady=(0, 0), sticky="s")
        self.menu_appearance.grid(row=11, column=0, padx=20, pady=(0, 5), sticky="n")

        # - HCA positions
        # -- create frame for HCA positions
        self.frame_position = customtkinter.CTkFrame(self)
        self.frame_position.grid(row=0, column=1, columnspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- HCA positions labels
        self.label_c1_axis = customtkinter.CTkLabel(self.frame_position, text="C1 Axis", anchor="w")
        self.label_c2_axis = customtkinter.CTkLabel(self.frame_position, text="C2 Axis", anchor="w")
        self.label_c1_hca = customtkinter.CTkLabel(self.frame_position, text="C1 HCA", anchor="w")
        self.label_c2_hca = customtkinter.CTkLabel(self.frame_position, text="C2 HCA", anchor="w")
        self.label_c1_new = customtkinter.CTkLabel(self.frame_position, text="C1 New", anchor="w")
        self.label_c2_new = customtkinter.CTkLabel(self.frame_position, text="C2 New", anchor="w")
        self.label_profile_axis = customtkinter.CTkLabel(self.frame_position, text="Profile Axis", anchor="w")
        self.label_height = customtkinter.CTkLabel(self.frame_position, text="H (mm)", anchor="w")
        self.label_init_pos = customtkinter.CTkLabel(self.frame_position, text="New Init. Pos.", anchor="w")
        self.label_hca_offset = customtkinter.CTkLabel(self.frame_position, text="HCA Offset", anchor="w")
        self.label_hca_position = customtkinter.CTkLabel(self.frame_position, text="HCA Position", anchor="w")
        self.label_new_position = customtkinter.CTkLabel(self.frame_position, text="New Position", anchor="w")

        # -- HCA positions entry defaults
        self.entry_c1_axis = tk.IntVar()
        self.entry_c1_axis.set(0)
        self.entry_c2_axis = tk.IntVar()
        self.entry_c2_axis.set(0)
        self.entry_c1_hca = tk.IntVar()
        self.entry_c1_hca.set(0)
        self.entry_c2_hca = tk.IntVar()
        self.entry_c2_hca.set(0)
        self.entry_c1_new = tk.IntVar()
        self.entry_c1_new.set(0)
        self.entry_c2_new = tk.IntVar()
        self.entry_c2_new.set(0)
        self.entry_profile_axis = tk.IntVar()
        self.entry_profile_axis.set(0)
        self.entry_height = tk.IntVar()
        self.entry_height.set(0)
        self.entry_init_pos = tk.IntVar()
        self.entry_init_pos.set(0)
        self.entry_offset_1 = tk.IntVar()
        self.entry_offset_1.set(0)
        self.entry_offset_2 = tk.IntVar()
        self.entry_offset_2.set(0)
        self.entry_offset_3 = tk.IntVar()
        self.entry_offset_3.set(0)
        self.entry_offset_4 = tk.IntVar()
        self.entry_offset_4.set(0)
        self.entry_offset_5 = tk.IntVar()
        self.entry_offset_5.set(0)
        self.entry_position_1 = tk.IntVar()
        self.entry_position_1.set(0)
        self.entry_position_2 = tk.IntVar()
        self.entry_position_2.set(0)
        self.entry_position_3 = tk.IntVar()
        self.entry_position_3.set(0)
        self.entry_position_4 = tk.IntVar()
        self.entry_position_4.set(0)
        self.entry_position_5 = tk.IntVar()
        self.entry_position_5.set(0)
        self.entry_position_6 = tk.IntVar()
        self.entry_position_6.set(0)
        self.entry_new_position_1 = tk.IntVar()
        self.entry_new_position_1.set(0)
        self.entry_new_position_2 = tk.IntVar()
        self.entry_new_position_2.set(0)
        self.entry_new_position_3 = tk.IntVar()
        self.entry_new_position_3.set(0)
        self.entry_new_position_4 = tk.IntVar()
        self.entry_new_position_4.set(0)
        self.entry_new_position_5 = tk.IntVar()
        self.entry_new_position_5.set(0)
        self.entry_new_position_6 = tk.IntVar()
        self.entry_new_position_6.set(0)

        # -- HCA positions entries
        self.entry_c1_axis = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c1_axis)
        self.entry_c2_axis = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c2_axis)
        self.entry_c1_hca = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c1_hca)
        self.entry_c2_hca = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c2_hca)
        self.entry_c1_new = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c1_new)
        self.entry_c2_new = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_c2_new)
        self.entry_profile_axis = customtkinter.CTkEntry(self.frame_position, width=50,
                                                         textvariable=self.entry_profile_axis)
        self.entry_height = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_height)
        self.entry_init_pos = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_init_pos)
        self.entry_offset_1 = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_offset_1)
        self.entry_offset_2 = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_offset_2)
        self.entry_offset_3 = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_offset_3)
        self.entry_offset_4 = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_offset_4)
        self.entry_offset_5 = customtkinter.CTkEntry(self.frame_position, width=50, textvariable=self.entry_offset_5)
        self.entry_position_1 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_1)
        self.entry_position_2 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_2)
        self.entry_position_3 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_3)
        self.entry_position_4 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_4)
        self.entry_position_5 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_5)
        self.entry_position_6 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                       textvariable=self.entry_position_6)
        self.entry_new_position_1 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_1)
        self.entry_new_position_2 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_2)
        self.entry_new_position_3 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_3)
        self.entry_new_position_4 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_4)
        self.entry_new_position_5 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_5)
        self.entry_new_position_6 = customtkinter.CTkEntry(self.frame_position, width=50,
                                                           textvariable=self.entry_new_position_6)

        # -- HCA positions buttons and switches
        self.switch_new_position_state = customtkinter.StringVar(value="on")
        self.switch_new_position = customtkinter.CTkSwitch(self.frame_position, text="Use New Position",
                                                           command=self.switch_event,
                                                           variable=self.switch_new_position_state,
                                                           onvalue="on", offvalue="off")

        # -- HCA widgets positioning
        self.label_c1_axis.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_c2_axis.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_profile_axis.grid(row=0, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_offset.grid(row=0, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_position.grid(row=0, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_position.grid(row=0, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c1_axis.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c2_axis.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_profile_axis.grid(row=1, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_offset_1.grid(row=1, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_1.grid(row=1, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_1.grid(row=1, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_c1_hca.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_c2_hca.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_height.grid(row=2, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_offset_2.grid(row=2, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_2.grid(row=2, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_2.grid(row=2, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c1_hca.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c2_hca.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_height.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_offset_3.grid(row=3, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_3.grid(row=3, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_3.grid(row=3, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_c1_new.grid(row=4, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_c2_new.grid(row=4, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_init_pos.grid(row=4, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_offset_4.grid(row=4, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_4.grid(row=4, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_4.grid(row=4, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c1_new.grid(row=5, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_c2_new.grid(row=5, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_init_pos.grid(row=5, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_offset_5.grid(row=5, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_5.grid(row=5, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_5.grid(row=5, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.switch_new_position.grid(row=6, column=0, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_position_6.grid(row=6, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_position_6.grid(row=6, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - HCA ranges
        # -- create frame for HCA ranges
        self.frame_ranges = customtkinter.CTkFrame(self)
        self.frame_ranges.grid(row=0, column=3, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- HCA range entry defaults
        global hca_dict
        self.entry_range_1_stored = tk.IntVar()
        self.entry_range_1_stored.set(hca_dict['range_1'])
        self.entry_range_2_stored = tk.IntVar()
        self.entry_range_2_stored.set(hca_dict['range_2'])
        self.entry_range_3_stored = tk.IntVar()
        self.entry_range_3_stored.set(hca_dict['range_3'])
        self.entry_range_4_stored = tk.IntVar()
        self.entry_range_4_stored.set(hca_dict['range_4'])
        self.entry_range_5_stored = tk.IntVar()
        self.entry_range_5_stored.set(hca_dict['range_5'])
        self.entry_range_6_stored = tk.IntVar()
        self.entry_range_6_stored.set(hca_dict['range_6'])

        # -- HCA ranges labels
        self.label_new_ranges = customtkinter.CTkLabel(self.frame_ranges, text="New Ranges", anchor="w")
        self.label_ranges = customtkinter.CTkLabel(self.frame_ranges, text="Ranges", anchor="w")
        self.label_auto_range = customtkinter.CTkLabel(self.frame_ranges, text="Auto Adj. Range", anchor="w")

        # -- HCA ranges entry defaults
        self.entry_new_range_1 = tk.IntVar()
        self.entry_new_range_1.set(0)
        self.entry_new_range_2 = tk.IntVar()
        self.entry_new_range_2.set(0)
        self.entry_new_range_3 = tk.IntVar()
        self.entry_new_range_3.set(0)
        self.entry_new_range_4 = tk.IntVar()
        self.entry_new_range_4.set(0)
        self.entry_new_range_5 = tk.IntVar()
        self.entry_new_range_5.set(0)
        self.entry_new_range_6 = tk.IntVar()
        self.entry_new_range_6.set(0)
        self.entry_range_1 = tk.IntVar()
        self.entry_range_1.set(0)
        self.entry_range_2 = tk.IntVar()
        self.entry_range_2.set(0)
        self.entry_range_3 = tk.IntVar()
        self.entry_range_3.set(0)
        self.entry_range_4 = tk.IntVar()
        self.entry_range_4.set(0)
        self.entry_range_5 = tk.IntVar()
        self.entry_range_5.set(0)
        self.entry_range_6 = tk.IntVar()
        self.entry_range_6.set(0)

        # -- HCA positions entries
        self.entry_new_range_1 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_1)
        self.entry_new_range_2 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_2)
        self.entry_new_range_3 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_3)
        self.entry_new_range_4 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_4)
        self.entry_new_range_5 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_5)
        self.entry_new_range_6 = customtkinter.CTkEntry(self.frame_ranges, width=50,
                                                        textvariable=self.entry_new_range_6)
        self.entry_range_1 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_1_stored)
        self.entry_range_2 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_2_stored)
        self.entry_range_3 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_3_stored)
        self.entry_range_4 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_4_stored)
        self.entry_range_5 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_5_stored)
        self.entry_range_6 = customtkinter.CTkEntry(self.frame_ranges, width=50, textvariable=self.entry_range_6_stored)

        # -- HCA positions buttons and switches
        self.button_set_ranges = customtkinter.CTkButton(self.frame_ranges, text='Set New Ranges',
                                                         command=self.set_ranges)
        self.button_set_for_zero = customtkinter.CTkButton(self.frame_ranges, text='Set for Zero',
                                                           command=self.set_ranges_for_zero)
        self.button_set_for_span = customtkinter.CTkButton(self.frame_ranges, text='Set for Span',
                                                           command=self.set_ranges_for_span)
        self.switch_auto_range_state = customtkinter.StringVar(value="on")
        self.switch_auto_range = customtkinter.CTkSwitch(self.frame_ranges, text="", command=self.switch_event_2,
                                                         variable=self.switch_auto_range_state,
                                                         onvalue="on", offvalue="off")

        # -- HCA widgets positioning
        self.label_new_ranges.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_ranges.grid(row=0, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.button_set_ranges.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_1.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_1.grid(row=1, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.button_set_for_zero.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_2.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_2.grid(row=2, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.button_set_for_span.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_3.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_3.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_auto_range.grid(row=4, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_4.grid(row=4, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_4.grid(row=4, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.switch_auto_range.grid(row=5, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_5.grid(row=5, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_5.grid(row=5, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_range_6.grid(row=6, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_range_6.grid(row=6, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - HCA concentrations
        # -- create frame for HCA concentrations
        self.frame_concentrations = customtkinter.CTkFrame(self)
        self.frame_concentrations.grid(row=1, column=1, columnspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- HCA concentrations labels
        self.label_hca_zero_conc = customtkinter.CTkLabel(self.frame_concentrations, text="HCA Zero Conc. (g/m3)",
                                                          anchor="w")
        self.label_new_zero_conc = customtkinter.CTkLabel(self.frame_concentrations, text="New Zero Conc. (g/m3)",
                                                          anchor="w")
        self.label_zero_channel_range = customtkinter.CTkLabel(self.frame_concentrations,
                                                               text="Zero Range by Channel (%)", anchor="w")
        self.label_hca_span_conc = customtkinter.CTkLabel(self.frame_concentrations, text="HCA Span Conc. (g/m3)",
                                                          anchor="w")
        self.label_new_span_conc = customtkinter.CTkLabel(self.frame_concentrations, text="New Span Conc. (g/m3)",
                                                          anchor="w")
        self.label_span_channel_range = customtkinter.CTkLabel(self.frame_concentrations,
                                                               text="Span Range by Channel (%)", anchor="w")
        self.label_bkg_range = customtkinter.CTkLabel(self.frame_concentrations, text="Background Range (%)",
                                                      anchor="w")
        self.label_raw_conc = customtkinter.CTkLabel(self.frame_concentrations, text="Sample Raw Conc. (g/m3)",
                                                     anchor="w")

        # -- HCA concentrations entry defaults
        self.entry_hca_zero_conc = tk.IntVar()
        self.entry_hca_zero_conc.set(0)
        self.entry_new_zero_conc = tk.IntVar()
        self.entry_new_zero_conc.set(0)
        self.entry_hca_zero_ch_1 = tk.IntVar()
        self.entry_hca_zero_ch_1.set(0)
        self.entry_hca_zero_ch_2 = tk.IntVar()
        self.entry_hca_zero_ch_2.set(0)
        self.entry_hca_zero_ch_3 = tk.IntVar()
        self.entry_hca_zero_ch_3.set(0)
        self.entry_hca_zero_ch_4 = tk.IntVar()
        self.entry_hca_zero_ch_4.set(0)
        self.entry_hca_zero_ch_5 = tk.IntVar()
        self.entry_hca_zero_ch_5.set(0)
        self.entry_hca_zero_ch_6 = tk.IntVar()
        self.entry_hca_zero_ch_6.set(0)
        self.entry_hca_span_conc = tk.IntVar()
        self.entry_hca_span_conc.set(0)
        self.entry_new_span_conc = tk.IntVar()
        self.entry_new_span_conc.set(0)
        self.entry_hca_span_ch_1 = tk.IntVar()
        self.entry_hca_span_ch_1.set(0)
        self.entry_hca_span_ch_2 = tk.IntVar()
        self.entry_hca_span_ch_2.set(0)
        self.entry_hca_span_ch_3 = tk.IntVar()
        self.entry_hca_span_ch_3.set(0)
        self.entry_hca_span_ch_4 = tk.IntVar()
        self.entry_hca_span_ch_4.set(0)
        self.entry_hca_span_ch_5 = tk.IntVar()
        self.entry_hca_span_ch_5.set(0)
        self.entry_hca_span_ch_6 = tk.IntVar()
        self.entry_hca_span_ch_6.set(0)
        self.entry_hca_bkg_ch_1 = tk.IntVar()
        self.entry_hca_bkg_ch_1.set(0)
        self.entry_hca_bkg_ch_2 = tk.IntVar()
        self.entry_hca_bkg_ch_2.set(0)
        self.entry_hca_bkg_ch_3 = tk.IntVar()
        self.entry_hca_bkg_ch_3.set(0)
        self.entry_hca_bkg_ch_4 = tk.IntVar()
        self.entry_hca_bkg_ch_4.set(0)
        self.entry_hca_bkg_ch_5 = tk.IntVar()
        self.entry_hca_bkg_ch_5.set(0)
        self.entry_hca_bkg_ch_6 = tk.IntVar()
        self.entry_hca_bkg_ch_6.set(0)
        self.entry_raw_conc_ch_1 = tk.IntVar()
        self.entry_raw_conc_ch_1.set(0)
        self.entry_raw_conc_ch_2 = tk.IntVar()
        self.entry_raw_conc_ch_2.set(0)
        self.entry_raw_conc_ch_3 = tk.IntVar()
        self.entry_raw_conc_ch_3.set(0)
        self.entry_raw_conc_ch_4 = tk.IntVar()
        self.entry_raw_conc_ch_4.set(0)
        self.entry_raw_conc_ch_5 = tk.IntVar()
        self.entry_raw_conc_ch_5.set(0)
        self.entry_raw_conc_ch_6 = tk.IntVar()
        self.entry_raw_conc_ch_6.set(0)

        # -- HCA positions entries
        self.entry_hca_zero_conc = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_conc)
        self.entry_new_zero_conc = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_new_zero_conc)
        self.entry_hca_zero_ch_1 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_1)
        self.entry_hca_zero_ch_2 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_2)
        self.entry_hca_zero_ch_3 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_3)
        self.entry_hca_zero_ch_4 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_4)
        self.entry_hca_zero_ch_5 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_5)
        self.entry_hca_zero_ch_6 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_zero_ch_6)
        self.entry_hca_span_conc = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_conc)
        self.entry_new_span_conc = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_new_span_conc)
        self.entry_hca_span_ch_1 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_1)
        self.entry_hca_span_ch_2 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_2)
        self.entry_hca_span_ch_3 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_3)
        self.entry_hca_span_ch_4 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_4)
        self.entry_hca_span_ch_5 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_5)
        self.entry_hca_span_ch_6 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_hca_span_ch_6)
        self.entry_hca_bkg_ch_1 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_1)
        self.entry_hca_bkg_ch_2 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_2)
        self.entry_hca_bkg_ch_3 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_3)
        self.entry_hca_bkg_ch_4 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_4)
        self.entry_hca_bkg_ch_5 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_5)
        self.entry_hca_bkg_ch_6 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                         textvariable=self.entry_hca_bkg_ch_6)
        self.entry_raw_conc_ch_1 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_1)
        self.entry_raw_conc_ch_2 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_2)
        self.entry_raw_conc_ch_3 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_3)
        self.entry_raw_conc_ch_4 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_4)
        self.entry_raw_conc_ch_5 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_5)
        self.entry_raw_conc_ch_6 = customtkinter.CTkEntry(self.frame_concentrations, width=50,
                                                          textvariable=self.entry_raw_conc_ch_6)

        # -- HCA widgets positioning
        self.label_hca_zero_conc.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_conc.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_zero_conc.grid(row=0, column=3, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_zero_conc.grid(row=0, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_zero_channel_range.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_1.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_2.grid(row=1, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_3.grid(row=1, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_4.grid(row=1, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_5.grid(row=1, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_zero_ch_6.grid(row=1, column=6, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_span_conc.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_conc.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_span_conc.grid(row=2, column=3, columnspan=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_span_conc.grid(row=2, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_span_channel_range.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_1.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_2.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_3.grid(row=3, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_4.grid(row=3, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_5.grid(row=3, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_span_ch_6.grid(row=3, column=6, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_bkg_range.grid(row=4, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_1.grid(row=4, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_2.grid(row=4, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_3.grid(row=4, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_4.grid(row=4, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_5.grid(row=4, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_bkg_ch_6.grid(row=4, column=6, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_raw_conc.grid(row=5, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_1.grid(row=5, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_2.grid(row=5, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_3.grid(row=5, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_4.grid(row=5, column=4, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_5.grid(row=5, column=5, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_raw_conc_ch_6.grid(row=5, column=6, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - HCA bounds
        # -- create frame for HCA out of bounds counts
        self.frame_bounds = customtkinter.CTkFrame(self)
        self.frame_bounds.grid(row=1, column=3, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- HCA bounds labels
        self.label_bounds_low = customtkinter.CTkLabel(self.frame_bounds, text="Out Low (#)", anchor="center")
        self.label_bounds_high = customtkinter.CTkLabel(self.frame_bounds, text="Out High (#)", anchor="center")

        # -- HCA bounds entry defaults
        self.entry_bound_low_1 = tk.IntVar()
        self.entry_bound_low_1.set(0)
        self.entry_bound_low_2 = tk.IntVar()
        self.entry_bound_low_2.set(0)
        self.entry_bound_low_3 = tk.IntVar()
        self.entry_bound_low_3.set(0)
        self.entry_bound_low_4 = tk.IntVar()
        self.entry_bound_low_4.set(0)
        self.entry_bound_low_5 = tk.IntVar()
        self.entry_bound_low_5.set(0)
        self.entry_bound_low_6 = tk.IntVar()
        self.entry_bound_low_6.set(0)
        self.entry_bound_high_1 = tk.IntVar()
        self.entry_bound_high_1.set(0)
        self.entry_bound_high_2 = tk.IntVar()
        self.entry_bound_high_2.set(0)
        self.entry_bound_high_3 = tk.IntVar()
        self.entry_bound_high_3.set(0)
        self.entry_bound_high_4 = tk.IntVar()
        self.entry_bound_high_4.set(0)
        self.entry_bound_high_5 = tk.IntVar()
        self.entry_bound_high_5.set(0)
        self.entry_bound_high_6 = tk.IntVar()
        self.entry_bound_high_6.set(0)

        # -- HCA bounds entries
        self.entry_bound_low_1 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_1)
        self.entry_bound_low_2 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_2)
        self.entry_bound_low_3 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_3)
        self.entry_bound_low_4 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_4)
        self.entry_bound_low_5 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_5)
        self.entry_bound_low_6 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                        textvariable=self.entry_bound_low_6)
        self.entry_bound_high_1 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_1)
        self.entry_bound_high_2 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_2)
        self.entry_bound_high_3 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_3)
        self.entry_bound_high_4 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_4)
        self.entry_bound_high_5 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_5)
        self.entry_bound_high_6 = customtkinter.CTkEntry(self.frame_bounds, width=50,
                                                         textvariable=self.entry_bound_high_6)

        # -- HCA bounds positioning
        self.label_bounds_low.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="ew")
        self.label_bounds_high.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="ew")
        self.entry_bound_low_1.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_1.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_low_2.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_2.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_low_3.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_3.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_low_4.grid(row=4, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_4.grid(row=4, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_low_5.grid(row=5, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_5.grid(row=5, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_low_6.grid(row=6, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_bound_high_6.grid(row=6, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - HCA file paths
        # -- create frame for HCA file paths
        self.frame_paths = customtkinter.CTkFrame(self)
        self.frame_paths.grid(row=2, column=1, columnspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")

        # -- HCA paths labels
        self.label_hca_streamed = customtkinter.CTkLabel(self.frame_paths, text="HCA Streamed File", anchor="w")
        self.label_new_streamed = customtkinter.CTkLabel(self.frame_paths, text="New Streamed File", anchor="w")
        self.label_hca_merged = customtkinter.CTkLabel(self.frame_paths, text="HCA Merged File", anchor="w")
        self.label_new_merged = customtkinter.CTkLabel(self.frame_paths, text="New Merged File", anchor="w")

        # -- HCA paths defaults
        self.entry_hca_streamed = tk.StringVar()
        self.entry_hca_streamed.set("location 1")
        self.entry_new_streamed = tk.StringVar()
        self.entry_new_streamed.set("location 2")
        self.entry_hca_merged = tk.StringVar()
        self.entry_hca_merged.set("location 3")
        self.entry_new_merged = tk.StringVar()
        self.entry_new_merged.set("location 4")

        # -- HCA paths entries
        self.entry_hca_streamed = customtkinter.CTkEntry(self.frame_paths, width=425, state="disabled",
                                                         textvariable=self.entry_hca_streamed)
        self.entry_new_streamed = customtkinter.CTkEntry(self.frame_paths, width=425,
                                                         textvariable=self.entry_new_streamed)
        self.entry_hca_merged = customtkinter.CTkEntry(self.frame_paths, width=425, state="disabled",
                                                       textvariable=self.entry_hca_merged)
        self.entry_new_merged = customtkinter.CTkEntry(self.frame_paths, width=425, textvariable=self.entry_new_merged)

        # -- HCA bounds positioning
        self.label_hca_streamed.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_streamed.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_streamed.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_streamed.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_merged.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_merged.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_merged.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_merged.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - HCA sample config
        # -- create frame for HCA sample configurations
        self.frame_config = customtkinter.CTkFrame(self)
        self.frame_config.grid(row=2, column=3, padx=(5, 0), pady=(5, 0), sticky="nsew")
        self.tabview_config = customtkinter.CTkTabview(self)
        self.tabview_config.grid(row=2, column=3, padx=(5, 5), pady=(5, 0), sticky="nsew")
        self.tabview_config.add("Run Config")
        self.tabview_config.add("Tunnel Config")

        # -- HCA config labels
        self.label_hca_run_seconds = customtkinter.CTkLabel(self.tabview_config.tab("Run Config"),
                                                            text="HCA Sample Run (s)", anchor="w")
        self.label_new_run_seconds = customtkinter.CTkLabel(self.tabview_config.tab("Run Config"),
                                                            text="New Sample Run (s)", anchor="w")
        self.label_default_zspan_seconds = customtkinter.CTkLabel(self.tabview_config.tab("Run Config"),
                                                                  text="Default ZSPAN (s)", anchor="w")
        self.label_new_zspan_seconds = customtkinter.CTkLabel(self.tabview_config.tab("Run Config"),
                                                              text="New ZSPAN (s)", anchor="w")
        self.label_hca_length_1 = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                         text="HCA Length Scale 1 (mm)", anchor="w")
        self.label_new_length_1 = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                         text="New Length Scale 1 (mm)", anchor="w")
        self.label_hca_length_2 = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                         text="HCA Length Scale 2 (mm)", anchor="w")
        self.label_new_length_2 = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                         text="New Length Scale 2 (mm)", anchor="w")
        self.label_norm_wind_speed = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                            text="Norm Wind Speed (m/s)", anchor="w")
        self.label_new_wind_speed = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                           text="New Wind Speed (m/s)", anchor="w")
        self.label_hca_source_rate = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                            text="HCA Source Rate (g/m3)", anchor="w")
        self.label_new_source_rate = customtkinter.CTkLabel(self.tabview_config.tab("Tunnel Config"),
                                                            text="New Source Rate (g/m3)", anchor="w")

        # -- HCA config defaults
        self.entry_hca_run_seconds = tk.IntVar()
        self.entry_hca_run_seconds.set(0)
        self.entry_new_run_seconds = tk.IntVar()
        self.entry_new_run_seconds.set(0)
        self.entry_default_zspan_seconds = tk.IntVar()
        self.entry_default_zspan_seconds.set(0)
        self.entry_new_zspan_seconds = tk.IntVar()
        self.entry_new_zspan_seconds.set(0)
        self.entry_hca_length_1 = tk.IntVar()
        self.entry_hca_length_1.set(0)
        self.entry_new_length_1 = tk.IntVar()
        self.entry_new_length_1.set(0)
        self.entry_hca_length_2 = tk.IntVar()
        self.entry_hca_length_2.set(0)
        self.entry_new_length_2 = tk.IntVar()
        self.entry_new_length_2.set(0)
        self.entry_norm_wind_speed = tk.IntVar()
        self.entry_norm_wind_speed.set(0)
        self.entry_new_wind_speed = tk.IntVar()
        self.entry_new_wind_speed.set(0)
        self.entry_hca_source_rate = tk.IntVar()
        self.entry_hca_source_rate.set(0)
        self.entry_new_source_rate = tk.IntVar()
        self.entry_new_source_rate.set(0)

        # -- HCA config entries
        self.entry_hca_run_seconds = customtkinter.CTkEntry(self.tabview_config.tab("Run Config"), width=50,
                                                            textvariable=self.entry_hca_run_seconds)
        self.entry_new_run_seconds = customtkinter.CTkEntry(self.tabview_config.tab("Run Config"), width=50,
                                                            textvariable=self.entry_new_run_seconds)
        self.entry_default_zspan_seconds = customtkinter.CTkEntry(self.tabview_config.tab("Run Config"), width=50,
                                                                  textvariable=self.entry_default_zspan_seconds)
        self.entry_new_zspan_seconds = customtkinter.CTkEntry(self.tabview_config.tab("Run Config"), width=50,
                                                              textvariable=self.entry_new_zspan_seconds)
        self.entry_hca_length_1 = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                         textvariable=self.entry_hca_length_1)
        self.entry_new_length_1 = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                         textvariable=self.entry_new_length_1)
        self.entry_hca_length_2 = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                         textvariable=self.entry_hca_length_2)
        self.entry_new_length_2 = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                         textvariable=self.entry_new_length_2)
        self.entry_norm_wind_speed = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                            textvariable=self.entry_norm_wind_speed)
        self.entry_new_wind_speed = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                           textvariable=self.entry_new_wind_speed)
        self.entry_hca_source_rate = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                            textvariable=self.entry_hca_source_rate)
        self.entry_new_source_rate = customtkinter.CTkEntry(self.tabview_config.tab("Tunnel Config"), width=50,
                                                            textvariable=self.entry_new_source_rate)

        # -- HCA config positioning
        self.label_hca_run_seconds.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_run_seconds.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_run_seconds.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_run_seconds.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_default_zspan_seconds.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_default_zspan_seconds.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_zspan_seconds.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_zspan_seconds.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_length_1.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_length_1.grid(row=0, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_length_1.grid(row=0, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_length_1.grid(row=0, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_length_2.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_length_2.grid(row=1, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_length_2.grid(row=1, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_length_2.grid(row=1, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_norm_wind_speed.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_norm_wind_speed.grid(row=2, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_wind_speed.grid(row=2, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_wind_speed.grid(row=2, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_hca_source_rate.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_hca_source_rate.grid(row=3, column=1, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.label_new_source_rate.grid(row=3, column=2, padx=(15, 0), pady=(10, 0), sticky="nsew")
        self.entry_new_source_rate.grid(row=3, column=3, padx=(15, 0), pady=(10, 0), sticky="nsew")

        # - program theme default values
        self.menu_appearance.set("System")
        # self.menu_scaling.set("100%")

    # - change overall appearance of program to light, dark, or system
    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # - change overall scaling of program
    @staticmethod
    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # - opens select profile window
    def open_profile_window(self):
        if self.profile_window is None or not self.profile_window.winfo_exists():
            self.profile_window = ProfileWindow()  # create window if its None or destroyed
            # self.button_select_profile.configure(text="Logging!")
        else:
            self.profile_window.focus()  # if window exists focus it

# TODO: make this function dynamic for input variable
    def switch_event(self):
        print("Switch toggled, current value:", self.switch_new_position_state.get())

    def switch_event_2(self):
        print("Switch toggled, current value:", self.switch_auto_range_state.get())
        
    def switch_event_3(self):
        print("Switch toggled, current value:", ProfileWindow.switch_change_profile_state.get())

    # - set current ranges to specified ranges
    def set_ranges(self):
        global hca_dict
        self.entry_range_1_stored.set(self.entry_new_range_1.get())
        self.entry_range_2_stored.set(self.entry_new_range_2.get())
        self.entry_range_3_stored.set(self.entry_new_range_3.get())
        self.entry_range_4_stored.set(self.entry_new_range_4.get())
        self.entry_range_5_stored.set(self.entry_new_range_5.get())
        self.entry_range_6_stored.set(self.entry_new_range_6.get())
        hca_dict |= {'range_1': self.entry_range_1.get()}
        hca_dict |= {'range_2': self.entry_range_2.get()}
        hca_dict |= {'range_3': self.entry_range_3.get()}
        hca_dict |= {'range_4': self.entry_range_4.get()}
        hca_dict |= {'range_5': self.entry_range_5.get()}
        hca_dict |= {'range_6': self.entry_range_6.get()}
        self.csv_generate()

    # - set current ranges to specified ranges
    def set_ranges_for_zero(self):
        global hca_dict
        self.entry_range_1_stored.set(1)
        self.entry_range_2_stored.set(1)
        self.entry_range_3_stored.set(1)
        self.entry_range_4_stored.set(1)
        self.entry_range_5_stored.set(1)
        self.entry_range_6_stored.set(1)

    # - set current ranges to specified ranges
    def set_ranges_for_span(self):
        global hca_dict
        self.entry_range_1_stored.set(7)
        self.entry_range_2_stored.set(7)
        self.entry_range_3_stored.set(7)
        self.entry_range_4_stored.set(7)
        self.entry_range_5_stored.set(7)
        self.entry_range_6_stored.set(7)

    # -- csv file that stores hca values such as current range
    @staticmethod
    def csv_generate():
        with open('hca_storage.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in hca_dict.items():
                writer.writerow([key, value])

    # -- recalls saved limits from csv
    def csv_recall(self):
        global hca_dict
        with open("hca_storage.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(','.join(row))
        # self.print_to_log(hca_dict)

    # - placeholder function for temp purposes
    @staticmethod
    def placeholder_function():
        print("Button works!")


if __name__ == "__main__":
    app = HCAControl()
    app.mainloop()
