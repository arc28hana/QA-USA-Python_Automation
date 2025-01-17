class Button:
    width = 200
    height = 50

    def __init__(self, color, text):
        self.button_color = color
        self.button_text = text


button_1 = Button('yellow', 'Buy')
button_2 = Button('red', 'Delete')

print(button_1.width)
print(button_1.button_color)
print(button_2.width)
print(button_2.button_color)