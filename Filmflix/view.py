import tkinter as tk
from tkinter import ttk


class filmflix_view(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("FilmFlix")
        self.geometry('550x500')
        self.minsize(550, 500)
        self.maxsize(550, 500)
        self.controller = controller

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (home_page, add_film_page, update_film_page, delete_film_page, all_films_page, search_films_page):
            page_name = F.__name__
            frame = F(parent=container, frame_controller=self,
                      controller=self.controller)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("home_page")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def get_info(self, page_name):
        frame = self.frames[page_name]
        info = frame.get_film_info()
        return info

    def set_info(self, page_name, data):
        frame = self.frames[page_name]
        frame.set_film_info(data)

    def clear_info(self, page_name):
        frame = self.frames[page_name]
        frame.clear_entries()

    def confirmation_message(self, page_name, data, success):
        frame = self.frames[page_name]
        frame.confirmation_message(data, success)

    def get_filmID(self, page_name):
        frame = self.frames[page_name]
        filmID = frame.get_filmID()
        return filmID

    def get_user_input(self, page_name):
        frame = self.frames[page_name]
        user_input = frame.get_user_input()
        return user_input

    def update_listbox(self, page_name, searched_films):
        frame = self.frames[page_name]
        frame.insert_to_listbox(searched_films)

    def delete_selected_anchor(self, page_name):
        frame = self.frames[page_name]
        frame.delete_anchor()

    def get_anchor_filmID(self, page_name):
        frame = self.frames[page_name]
        anchor = frame.get_anchor()
        return anchor[0]

    def get_anchor_data(self, page_name):
        frame = self.frames[page_name]
        anchor = frame.get_anchor()
        return anchor


class home_page(ttk.Frame):

    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        self.filmflix_lbl = ttk.Label(
            self, text='FilmFlix', font=('Arial', 48), foreground="blue").pack(pady=(150, 20))

        # Buttons and their commands
        button_frame = ttk.Frame(self)
        button_frame.pack(expand=True, fill='y')

        def open_add_film():
            frame_controller.show_frame('add_film_page')
            frame_controller.clear_info('add_film_page')

        add_film_page_btn = ttk.Button(
            button_frame, text='Add Film', command=open_add_film)
        add_film_page_btn.grid(row=0, column=0, padx=5)

        def open_update_film():
            frame_controller.show_frame('update_film_page')
            frame_controller.clear_info('update_film_page')

        update_film_page_btn = ttk.Button(
            button_frame, text='Update Film', command=open_update_film)
        update_film_page_btn.grid(row=0, column=1, padx=5)

        def open_delete_film():
            frame_controller.show_frame('delete_film_page')
            frame_controller.clear_info('delete_film_page')

        delete_film_page_btn = ttk.Button(
            button_frame, text='Delete Film', command=open_delete_film)
        delete_film_page_btn.grid(row=0, column=2, padx=5)

        def open_all_films():
            frame_controller.show_frame('all_films_page')
            controller.get_all_films()

        all_films_page_btn = ttk.Button(
            button_frame, text='All Films', command=open_all_films)
        all_films_page_btn.grid(row=0, column=3, padx=5)

        def open_search_films():
            frame_controller.show_frame('search_films_page')
            frame_controller.clear_info('search_films_page')

        search_films_page_btn = ttk.Button(
            button_frame, text='Search Films', command=open_search_films)
        search_films_page_btn.grid(row=0, column=4, padx=5)

        exit_btn = ttk.Button(button_frame, text="Exit", command=exit)
        exit_btn.grid(row=0, column=5, padx=5)


class add_film_page(ttk.Frame):
    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        def open_home():
            frame_controller.show_frame('home_page')

        home_page_btn = ttk.Button(
            self, text='Home', command=open_home).pack()

        self.title_field = entry_field(self, "Title:")
        self.year_released_field = entry_field(self, "Year Released:")
        self.duration_field = entry_field(self, "Duration:")
        self.genre_field = entry_field(self, "Genre:")
        self.rating_field = rating_radiobtns(self)

        btn_frame = ttk.Frame(self)
        btn_frame.pack()

        clear_entries_btn = ttk.Button(
            btn_frame, text='Clear', command=lambda: self.clear_entries()).pack(side=tk.LEFT, pady=5)

        add_film_btn = ttk.Button(
            btn_frame, text='Add Film', command=lambda: controller.add_film()).pack(side=tk.LEFT, padx=5)

    def get_film_info(self):
        info = (self.title_field.get_entry(),
                int(self.year_released_field.get_entry()),
                self.rating_field.clicked(),
                int(self.duration_field.get_entry()),
                self.genre_field.get_entry()
                )
        return info

    def clear_entries(self):
        self.title_field.clear_entry()
        self.year_released_field.clear_entry()
        self.duration_field.clear_entry()
        self.genre_field.clear_entry()
        self.rating_field.clear_button()

    def confirmation_message(self, data, success):
        try:
            self.confirm_label.destroy()
        except:
            pass

        if success == True:
            self.confirm_label = ttk.Label(
                self, text=f'{data} has been added to the table.')
            self.confirm_label.pack()

        else:
            self.confirm_label = ttk.Label(
                self, text='Please only enter intergers in the Year Released and Duration boxes.', background="white", foreground="red")
            self.confirm_label.pack()


class update_film_page(ttk.Frame):
    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        def open_home():
            frame_controller.show_frame('home_page')

        home_page_btn = ttk.Button(
            self, text='Home', command=open_home).pack()

        self.filmID_field = entry_field(self, "Search FilmID:")

        search_filmID_btn = ttk.Button(
            self.filmID_field, text='Search', command=lambda: controller.search_filmID('update_film_page')).pack(side=tk.LEFT)

        current_filmID_frame = ttk.Frame(self)
        current_filmID_frame.pack()

        self.current_filmID = tk.StringVar()
        self.current_filmID.set("")
        self.current_filmID_lbl1 = ttk.Label(
            current_filmID_frame, text="Current FilmID:")
        self.current_filmID_lbl2 = ttk.Label(
            current_filmID_frame, text="", background="white", borderwidth=2, relief="solid", width=40)
        self.current_filmID_lbl1.pack(side=tk.LEFT)
        self.current_filmID_lbl2.pack(side=tk.LEFT, padx=5, pady=5)

        self.title_field = entry_field(self, "Title:")
        self.year_released_field = entry_field(self, "Year Released:")
        self.duration_field = entry_field(self, "Duration:")
        self.genre_field = entry_field(self, "Genre:")
        self.rating_field = rating_radiobtns(self)

        btn_frame = ttk.Frame(self)
        btn_frame.pack()

        clear_entries_btn = ttk.Button(
            btn_frame, text='Clear', command=lambda: self.clear_entries()).pack(side=tk.LEFT, pady=5)

        update_film_btn = ttk.Button(
            btn_frame, text='Update Film', command=lambda: controller.update_film()).pack(side=tk.LEFT, padx=5)

    def get_filmID(self):
        filmID = int(self.filmID_field.get_entry())
        return filmID

    def get_film_info(self):
        info = (self.title_field.get_entry(),
                int(self.year_released_field.get_entry()),
                self.rating_field.clicked(),
                int(self.duration_field.get_entry()),
                self.genre_field.get_entry(),
                int(self.current_filmID_lbl2.cget("text"))
                )
        return info

    def set_film_info(self, data):
        self.current_filmID_lbl2.config(text=data[0])
        self.title_field.insert_data(data[1])
        self.year_released_field.insert_data(data[2])
        self.rating_field.set_button(data[3])
        self.duration_field.insert_data(data[4])
        self.genre_field.insert_data(data[5])

    def clear_entries(self):
        self.filmID_field.clear_entry()
        self.current_filmID_lbl2.config(text="")
        self.title_field.clear_entry()
        self.year_released_field.clear_entry()
        self.duration_field.clear_entry()
        self.genre_field.clear_entry()
        self.rating_field.clear_button()

    def confirmation_message(self, data, success):
        try:
            self.confirm_label.destroy()
        except:
            pass

        if success == True:
            self.confirm_label = ttk.Label(
                self, text=f'FilmID: {data[5]} has been updated to {data[0:5]}.')
            self.confirm_label.pack()

        elif success == ValueError:
            self.confirm_label = ttk.Label(
                self, text='The FilmID, Year Released and Duration boxes are either empty or contain non-integer values.', background="white", foreground="red")
            self.confirm_label.pack()

        elif success == TypeError:
            self.confirm_label = ttk.Label(
                self, text='FilmID entered does not exist', background="white", foreground="red")
            self.confirm_label.pack()


class delete_film_page(ttk.Frame):
    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        def open_home():
            frame_controller.show_frame('home_page')

        home_page_btn = ttk.Button(
            self, text='Home', command=open_home).pack()

        self.filmID_field = entry_field(self, "FilmID:")

        btn_frame = ttk.Frame(self)
        btn_frame.pack()

        search_filmID_btn = ttk.Button(
            btn_frame, text='Search FilmID', command=lambda: controller.search_filmID('delete_film_page')).pack(side=tk.LEFT, pady=5)

        delete_film_btn = ttk.Button(
            btn_frame, text='Delete Film', command=lambda: controller.delete_film()).pack(side=tk.LEFT, padx=5)

    def get_filmID(self):
        filmID = int(self.filmID_field.get_entry())
        try:
            self.confirm_label.destroy()
        except:
            pass

        try:
            self.film_label.destroy()
        except AttributeError:
            pass
        return filmID

    def set_film_info(self, data):
        self.film_label = ttk.Label(
            self, text=f'Current FilmID data: {data}', background="white")
        self.film_label.pack()

    def clear_entries(self):
        self.filmID_field.clear_entry()
        try:
            self.film_label.destroy()
        except AttributeError:
            pass

    def confirmation_message(self, data, success):
        try:
            self.confirm_label.destroy()
        except:
            pass

        if success == True:
            self.confirm_label = ttk.Label(
                self, text=f'FilmID: {data} has been deleted.')
            self.confirm_label.pack()

        elif success == ValueError:
            self.confirm_label = ttk.Label(
                self, text='The FilmID box is either empty or contains non-integer values.', background="white", foreground="red")
            self.confirm_label.pack()


class all_films_page(ttk.Frame):
    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        def open_home():
            frame_controller.show_frame('home_page')

        home_page_btn = ttk.Button(
            self, text='Home', command=open_home).pack()

        # Film Listbox
        listbox_frame = ttk.Frame(self)
        listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient='vertical')

        self.film_listbox = tk.Listbox(
            listbox_frame, width=80, yscrollcommand=listbox_scrollbar.set)

        listbox_scrollbar.config(command=self.film_listbox.yview)
        listbox_scrollbar.pack(side='right', fill='y')
        listbox_frame.pack()

        self.film_listbox.pack(pady=15)

        btn_frame = ttk.Frame(self)
        btn_frame.pack()

        delete_selected_film_btn = ttk.Button(
            btn_frame, text='Delete Selected Film', command=lambda: controller.delete_selected_film('all_films_page')).pack(side=tk.LEFT, pady=5)

        update_selected_film_btn = ttk.Button(
            btn_frame, text='Update Selected Film', command=lambda: controller.update_selected_film('all_films_page')).pack(side=tk.LEFT, padx=5)

    def delete_anchor(self):
        self.film_listbox.delete(tk.ANCHOR)

    def get_anchor(self):
        return self.film_listbox.get(tk.ANCHOR)

    def insert_to_listbox(self, searched_films):
        self.film_listbox.delete(0, tk.END)
        for film in searched_films:
            self.film_listbox.insert(tk.END, film)


class search_films_page(ttk.Frame):
    def __init__(self, parent, frame_controller, controller):
        super().__init__(parent)

        def open_home():
            frame_controller.show_frame('home_page')

        home_page_btn = ttk.Button(
            self, text='Home', command=open_home).pack()

        # Dropdown Menu - change frame
        def selected_frame():
            if self.selected.get() == "By Genre":
                by_year.pack_forget()
                by_rating.pack_forget()
                by_genre.pack()
                self.by_genre_field.clear_entry()

            elif self.selected.get() == "By Year Released":
                by_rating.pack_forget()
                by_genre.pack_forget()
                by_year.pack()
                self.by_yearReleased_field.clear_entry()
            elif self.selected.get() == "By Rating":
                by_year.pack_forget()
                by_genre.pack_forget()
                by_rating.pack()
                self.by_rating_field.clear_button()

        options = [
            "By Genre",
            "By Year Released",
            "By Rating"
        ]

        self.selected = tk.StringVar()
        self.selected.set("Search by...")

        dropdown_box = ttk.OptionMenu(
            self, self.selected, "Search by...", *options)
        dropdown_box.pack()

        dropdown_btn = ttk.Button(
            self, text='Select', command=selected_frame).pack()

        selection_frame = ttk.Frame(self)
        selection_frame.pack()

        # By Genre Frame

        by_genre = ttk.Frame(selection_frame, width=100)
        self.by_genre_field = entry_field(by_genre, 'Genre:')
        search_genre_btn = ttk.Button(
            by_genre, text='Search', command=lambda: controller.search_by('genre')).pack()

        # By Year Frame

        by_year = ttk.Frame(selection_frame)
        self.by_yearReleased_field = entry_field(by_year, 'Year Released:')
        search_yearReleased_btn = ttk.Button(
            by_year, text='Search', command=lambda: controller.search_by('yearReleased')).pack()

        # By Rating Frame

        by_rating = ttk.Frame(selection_frame)
        self.by_rating_field = rating_radiobtns(by_rating)
        search_rating_btn = ttk.Button(
            by_rating, text='Search', command=lambda: controller.search_by('rating')).pack()

        # Film Listbox
        listbox_frame = ttk.Frame(self)
        listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient='vertical')

        self.film_listbox = tk.Listbox(
            listbox_frame, width=80, yscrollcommand=listbox_scrollbar.set)

        listbox_scrollbar.config(command=self.film_listbox.yview)
        listbox_scrollbar.pack(side='right', fill='y')
        listbox_frame.pack()

        self.film_listbox.pack(pady=15)

        btn_frame = ttk.Frame(self)
        btn_frame.pack()

        delete_selected_film_btn = ttk.Button(
            btn_frame, text='Delete Selected Film', command=lambda: controller.delete_selected_film('search_films_page')).pack(side=tk.LEFT, pady=5)

        update_selected_film_btn = ttk.Button(
            btn_frame, text='Update Selected Film', command=lambda: controller.update_selected_film('search_films_page')).pack(side=tk.LEFT, padx=5)

    def get_user_input(self):
        if self.selected.get() == "By Genre":
            return self.by_genre_field.get_entry()
        elif self.selected.get() == "By Year Released":
            return self.by_yearReleased_field.get_entry()
        elif self.selected.get() == "By Rating":
            return self.by_rating_field.clicked()

    def insert_to_listbox(self, searched_films):
        self.film_listbox.delete(0, tk.END)
        for film in searched_films:
            self.film_listbox.insert(tk.END, film)

    def delete_anchor(self):
        self.film_listbox.delete(tk.ANCHOR)

    def get_anchor(self):
        return self.film_listbox.get(tk.ANCHOR)

    def clear_entries(self):
        self.film_listbox.delete(0, tk.END)
        self.by_genre_field.clear_entry()
        self.by_yearReleased_field.clear_entry()
        self.by_rating_field.clear_button()


class entry_field(ttk.Frame):
    def __init__(self, parent, entry_lbl):
        super().__init__(parent)

        entry_lbl = ttk.Label(self, text=entry_lbl)
        self.entry_box = ttk.Entry(self, width=40)

        entry_lbl.pack(side=tk.LEFT)
        self.entry_box.pack(side=tk.LEFT, padx=5, pady=5)

        self.pack()

    def get_entry(self):
        info = self.entry_box.get()
        return info

    def insert_data(self, data):
        self.entry_box.delete(0, tk.END)
        self.entry_box.insert(0, data)

    def clear_entry(self):
        self.entry_box.delete(0, tk.END)


class rating_radiobtns(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.rating = tk.StringVar()

        rating_lbl = ttk.Label(self, text='Rating:').pack(side=tk.LEFT)
        radiobtn_G = ttk.Radiobutton(
            self, text="G (General Audience)", variable=self.rating, value="G", command=lambda: self.clicked()).pack(side=tk.LEFT, padx=5)
        radiobtn_PG = ttk.Radiobutton(
            self, text="PG (Parental Guidance)", variable=self.rating, value="PG", command=lambda: self.clicked()).pack(side=tk.LEFT, padx=5)
        radiobtn_R = ttk.Radiobutton(
            self, text="R (Restricted)", variable=self.rating, value="R", command=lambda: self.clicked()).pack(side=tk.LEFT, padx=5)

        self.pack()

    def clicked(self):
        return self.rating.get()

    def set_button(self, data):
        self.rating.set(data)

    def clear_button(self):
        self.rating.set("")
