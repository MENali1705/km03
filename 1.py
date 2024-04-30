a = {
    "car": "mercedes",
    "model": "w124",
    "image": "https://www.bing.com/images/search?view=detailV2&ccid=n6aT7ymx&id=728CBEF011E7A455D862FA021681FFB386FE1C9F&thid=OIP.n6aT7ymxkdM0YQjoKKFwbwHaE6&mediaurl=https%3a%2f%2fmbworld.org%2fforums%2fattachments%2fe-class-w124%2f372363d1501268445-1991-w124-300d-turbo-diesel-modernising-family-used-over-next-10-years-dsc_6924_zpsiji4wzte.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.9fa693ef29b191d3346108e828a1706f%3frik%3dnxz%252bhrP%252fgRYC%252bg%26pid%3dImgRaw%26r%3d0&exph=2848&expw=4288&q=w124&simid=608046818676397434&FORM=IRPRST&ck=C87567E927FD522D116AC1AA532FDE20&selectedIndex=1&itb=0&ajaxhist=0&ajaxserp=0",
    "price": "3400"
}

b = {
    "car":"GMC",
    "model": "siera",
    "image":"https://www.bing.com/images/search?view=detailV2&ccid=dxxA0Ix9&id=4B95D46C879EF8160025A0658D0FA848D2467C13&thid=OIP.dxxA0Ix9lkY9LzCnG794zAHaE7&mediaurl=https%3a%2f%2fcdn.carbuzz.com%2fgallery-images%2f1600%2f825000%2f100%2f825175.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.771c40d08c7d96463d2f30a71bbf78cc%3frik%3dE3xG0kioD41loA%26pid%3dImgRaw%26r%3d0&exph=1066&expw=1600&q=gmc+models&simid=608000098027513824&FORM=IRPRST&ck=E8CD9C2D73165D335CBB5E72E0DB3CE7&selectedIndex=6&itb=0&ajaxhist=0&ajaxserp=0",
    "price": "4000",
    "is-Published": True
}

#dict

print(b)





list_1 = [
    {"name": "Kanat", "last_name": "Erbolov", "age": 20},
    {"name": "Askar", "last_name": "Paivich", "age": 15},
    {"name": "Ali", "last_name": "Ryskeldi", "age": 45}
]

total_age = 0
for person in list_1:
    total_age += person["age"]
    
count = len(list_1)


average_age = total_age / count

print("Average age:",average_age)


a = { "name": "Ali", "surname": "Ryskeldi"}
b = a["surname"]
a["middle_name"] = "Farabivich"
print("a = ",a)