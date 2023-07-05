from model import filmflix_db
from view import filmflix_view


class filmflix_controller:
    def __init__(self):
        self.model = filmflix_db()
        self.view = filmflix_view(self)

    def main(self):
        self.view.mainloop()

    def add_film(self):
        try:
            film_data = self.view.get_info("add_film_page")
            self.model.insert_film(film_data)
            self.view.clear_info("add_film_page")
            self.view.confirmation_message("add_film_page", film_data, True)
        except ValueError:
            data = ()
            self.view.confirmation_message("add_film_page", data, False)
            pass

    def search_filmID(self, page_name):
        data = ()
        if page_name == 'update_film_page':
            try:
                filmID = self.view.get_filmID(page_name)
                film_data = self.model.get_by_filmID(filmID)
                self.view.set_info('update_film_page', film_data)
                self.view.confirmation_message(
                    "update_film_page", data, "")
            except ValueError:
                self.view.confirmation_message(
                    "update_film_page", data, ValueError)
            except TypeError:
                self.view.confirmation_message(
                    "update_film_page", data, TypeError)

        elif page_name == 'delete_film_page':
            try:
                filmID = self.view.get_filmID(page_name)
                film_data = self.model.get_by_filmID(filmID)
                self.view.set_info('delete_film_page', film_data)
            except ValueError:
                self.view.confirmation_message(
                    'delete_film_page', data, ValueError)

    def update_film(self):
        data = ()
        try:
            film_data = self.view.get_info("update_film_page")
            self.model.update_film(film_data)
            self.view.clear_info("update_film_page")
            self.view.confirmation_message("update_film_page", film_data, True)
        except ValueError:
            self.view.confirmation_message(
                "update_film_page", data, ValueError)

    def delete_film(self):
        data = ()
        try:
            filmID = self.view.get_filmID("delete_film_page")
            self.model.delete_film(filmID)
            self.view.clear_info("delete_film_page")
            self.view.confirmation_message("delete_film_page", filmID, True)
        except ValueError:
            self.view.confirmation_message(
                "delete_film_page", data, ValueError)

    def update_selected_film(self, page_name):
        if page_name == 'all_films_page':
            film_data = self.view.get_anchor_data(page_name)
            self.view.show_frame('update_film_page')
            self.view.set_info('update_film_page', film_data)
        elif page_name == 'search_films_page':
            film_data = self.view.get_anchor_data(page_name)
            self.view.show_frame('update_film_page')
            self.view.set_info('update_film_page', film_data)

    def delete_selected_film(self, page_name):
        if page_name == 'all_films_page':
            anchor_filmID = self.view.get_anchor_filmID(page_name)
            self.model.delete_film(anchor_filmID)
            self.view.delete_selected_anchor(page_name)
        elif page_name == 'search_films_page':
            anchor_filmID = self.view.get_anchor_filmID(page_name)
            self.model.delete_film(anchor_filmID)
            self.view.delete_selected_anchor(page_name)

    def search_by(self, parameter):
        user_input = self.view.get_user_input('search_films_page')
        self.view.update_listbox('search_films_page',
                                 self.model.search_by(parameter, user_input))

    def get_all_films(self):
        all_films = self.model.get_all_films()
        self.view.update_listbox('all_films_page', all_films)


if __name__ == '__main__':
    filmflix = filmflix_controller()
    filmflix.main()
