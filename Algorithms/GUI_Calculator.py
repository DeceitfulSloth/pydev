# GUI Calculator

from tkinter import *

def draw_button(key, col, line):
    bt = Button(window, text=key, command=lambda: press_button(key))
    bt.grid(column=col+1, row=line+1)
    return bt

def press_button(key):
    if key == 'C':
        disp['text'] = ''
    elif key == '<':
        disp['text'] = disp['text'][:-1]
    elif key == '=':
        try:
            disp['text'] = str(round(eval(disp['text']), 6))
        except:
            disp['text'] = ''
    else:
        disp['text'] += key

window = Tk()
window.title('Tkalc')
window.resizable(False, False)
window.geometry('200x150+200+200')


disp = Label(window, text='')
disp.grid(column=0, row=0, columnspan=10)

keys = '()C<789/456*123-.0=+'
bt_list = [draw_button(keys[n], n%4, n//4) for n in range(20)]

window.mainloop()
