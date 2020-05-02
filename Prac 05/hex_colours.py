NAME_TO_CODE = {'aliceblue': '#f0f8ff', 'black': '#000000', 'darkgreen': '#006400', 'gray': '#bebebe', 'greenyellow': '#adff2f',
                'lavender': '#e6e6fa', 'lightpink': '#ffb6c1', 'lightgray': 'd3d3d3', 'linen': '#faf0e6', 'magenta': '#ff00ff'}
print(NAME_TO_CODE)
print("")
color_name = input("Enter color name: ").lower()
while color_name != "":
    if color_name in NAME_TO_CODE:
        print(color_name.title(), "is", NAME_TO_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()
