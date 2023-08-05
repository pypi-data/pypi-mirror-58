"""
menyou - An easy-to-use console-based menu module.
"""
from os import system, name
import sys
import pyfiglet

class Opshin(object):
    """
    A menu option.
    """

    def __init__(self, name: str, payload: callable, disabled=False) -> None:
        """
        Initializes a menu option

        :param name: The name of the menu option (will be displayed).
        :param payload: A function to execute, or a submenu to navigate to.
        :param disabled: When set to True, the menu option will not be selectable.
        :return: None.
        """
        self.name = name
        self.payload = payload
        self.disabled = disabled


class Menyou(object):
    """
    Menu class defines functions for displaying menus and handling user input. For the most part, menu does not handle
    any of the 'business logic'. It is for presentation of menus and prompts to the user.
    """

    def __init__(self, title: str, subtitle: str, opts: list, prompt_str: str) -> None:
        """
        Initializes a menu. After the title and subtitle are displayed, a list of menu options is formed
        from the Opshin objects in the opts list. The Opshin objects provide the menu option name and
        payload (a function to execute, or a link to another menu). The Opshin object's disabled flag can be set True
        to prevent menu option from being selected. The _prev and _prev_idx are used to point to the 'previous' menu.
        This provides the data for a Menyou object to return to the previous menu.

        :param title: Menu title (string).
        :param subtitle: Menu subtitle (string).
        :param opts: A list of menu options.
        :param prompt_str: Prompt to user (i.e. 'Please choose an option').
        :return: None.
        """
        self.title = title
        self.subtitle = subtitle
        self.opts = opts
        self.prompt_str = prompt_str

        self._prev = None
        self._prev_idx = None

    def get_disabled_indexes(self) -> list:
        """
        :return: A list of menu choice indexes that are disabled.
        """
        return [idx for idx, opt in enumerate(self.opts) if opt.disabled is True]

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, value: 'Menu') -> None:
        """
        Stores the previous Menu object and its index number.

        :param value: The previous Menu object.
        :return: None.
        """
        self._prev = value
        self._prev_idx = len(self.opts)

    def __str__(self) -> str:
        """
        Returns a string representation of a Menu instance (i.e. displays the menu to the user).

        :return: A string representation of a Menu instance.
        """
        # Menu title and subtitle
        menu_str = pyfiglet.figlet_format(self.title)
        menu_str += f'\n{self.subtitle}\n'
        menu_str += '-' * len(self.subtitle) + '\n'

        # Append the menu options
        for i, opt in enumerate(self.opts, 1):
            if opt.disabled:
                menu_str += f'-- {opt.name} --\n'
            else:
                menu_str += f'{i}. {opt.name}\n'

        # Append a 'return to previous menu option' if there was a previous menu
        if self._prev:
            menu_str += str(self._prev_idx + 1) + '. Return\n'

        return menu_str

    def prompt(self) -> None:
        """
        Prompts the user to enter a choice from the displayed menu. Loops until user enters a valid menu option. The
        verbiage of the prompt is provided by the prompt_str attribute.

        :return: None.
        """
        choice = None
        try:
            # Convert choice to integer and make it zero-based
            choice = int(input(self.prompt_str)) - 1
        except ValueError:
            self.choice_invalid()

        # Execute choice, display previous menu, or invalid choice
        if choice in range(len(self.opts)) and choice not in self.get_disabled_indexes():
            self.execute(choice)
        elif self._prev and choice == self._prev_idx:
            self._prev.display_menu()
        else:
            self.choice_invalid()

    def choice_invalid(self) -> None:
        """
        Displays a message to the user if they enter an invalid menu choice. Pauses for an 'any key' press, and then
        displays the last menu.

        :return: None.
        """
        input('Invalid choice.  Press any key to continue... ')
        self.display_menu()

    @staticmethod
    def payload_director(fn) -> callable:
        """
        Returns a function that contains the logic to execute a payload. The default behaviour is to simply execute
        the payload function directly. An example of a non-default behaviour would be to prompt the user for some
        information and then pass that information to the payload function (i.e. prompt the user for a start and end
        date before calling a payload like get_data_for_date_range(start, end).

        :param fn: The function(payload) to execute.
        :return: The return value(s) of the executed function, or None, depending on the requirements.
        """
        def inner():
            # As per the documentation, you can define an if/elsif/else control structure
            # here if you want to do something more complex than execute the parameterless payload function.
            fn()
        return inner

    def execute(self, choice: int) -> None:
        """
        Executes the Menu option chosen by the user. The 'payload' to be executed could be a function or another Menu.
        If the payload is a Menu (i.e. a submenu to 'navigate' to) then display_menu is called on that Menu object.
        display_menu can be called in a way that sets a return path to the current menu (by supplying update_prev=True),
        or, by omitting this argument, the current menu can be re-displayed without changing the return path.

        :param choice: An integer representing the Menu option to execute.
        :return: None.
        """
        payload = self.opts[choice].payload
        if isinstance(payload, Menyou):
            # The payload is a Menu, so update_prev tells the new menu to save a return path
            # to the current menu
            payload.display_menu(prev=self, update_prev=True)
        else:
            # The payload is a function to execute. payload_director returns a closure that knows how to
            # handle different functions by their name
            payload = self.payload_director(payload)
            payload()
            # Give user a chance to read the output
            input('Press any key to continue...')
            # Re-display the menu and keep the current return path
            self.display_menu()

    def display_menu(self, prev: 'Menu' = None, update_prev: bool = False) -> None:
        """
        Clears the screen and displays the menu. If update_prev is set to True, stores a return path to the 'previous'
        menu. update_prev=True causes the new menu to display a final menu option, allowing navigation to the
        previously displayed menu.  Omitting update_prev will leave the current return path in place, useful for when
        you want to redisplay the 'current' menu without changing its previous menu.

        :param prev: The Menu instance that called this one.
        :param update_prev: A boolean that determines whether the return path to the previous Menu should be updated
        before displaying the Menu.
        :return: None.
        """
        # Setup a return path to the previous menu
        if prev and update_prev:
            self.prev = prev

        self.clear()
        print(self)
        self.prompt()

    @staticmethod
    def clear() -> int:
        """
        Clears the screen. Should work in Windows or Linux.

        :return: int exit code 0.
        """
        if name == 'nt':
            return system('cls')
        else:
            return system('clear')


    @staticmethod
    def exit() -> int:
        """
        Exits the program. Should work in Windows or Linux.

        :return: int exit code 0.
        """
        return sys.exit()