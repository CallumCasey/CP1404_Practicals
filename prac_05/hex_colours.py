COLOUR_NAMES = {"Darkviolet": "#9400d3", "Dimgray": "#696969", "Ghostwhite": "#f8f8ff", "Light": "#eedd82",
                "Linen": "#faf0e6"}

colour = input("Enter colour name: ").capitalize()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ").capitalize()
