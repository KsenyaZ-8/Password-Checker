import urwid


def is_very_long(password):
    return len(password)>12

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_letters(password):
    return any (char.isalpha() for char in password) 

def has_upper_letters(password):
    return any(char.isupper() for char in password) 

def has_lower_letters(password):
    return any(char.islower() for char in password) 

def has_symbols(password):
    return any(not char.isalpha() and not char.isdigit() for char in password) 

def doesnt_consist_of_symbols(password):
    return any(char.isalpha() or char.isdigit() for char in password) 

def on_ask_change(edit, new_edit_text):
    score = 0
    for test in password_strength_tests:
        if test(new_edit_text):
            score = score + 2 
    reply.set_text('Рейтинг этого пароля:%s' % score)


if __name__ == '__main__':
    password_strength_tests = [
      is_very_long,
      has_digit,
      has_letters,
      has_upper_letters,
      has_lower_letters,
      has_symbols,
      doesnt_consist_of_symbols
      ]

    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text('')
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()