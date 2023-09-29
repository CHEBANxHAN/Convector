from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageGrab
from random import*

def go_to_list8():
    try:
        name = entry.get()
        nameX = int(entryX.get())
        nameY = int(entryY.get())
        img = Image.open(name)
        img = img.resize((nameX // 8, nameY))
        img = img.convert('L')
        data = list(img.getdata())
        d = 0
        conv = []
        for i in data:
            if i > 127:
                i = "0xff"
            else:
                i = "0x00"
            conv.append(i)
            d += 1
        data = [conv[offset:offset+nameX] for offset in range(0, nameX*nameY, nameX)]
        f = open(f"data{randint(0, 1000)}.txt", "w")
        for row in data:
            t = ', '.join('{:3}'.format(value) for value in row)
            f.write(f"{t}, ")
            tm.insert(END, t)
            tm.see(END)
            tm.update()
        f.close()
        txt = str(d)
        textn["text"] = f"{txt} elements"
        textn.update()
    except FileNotFoundError:
        textn["text"] = f"File not found"
        textn.update()

otv = True
def delete():
    global otv
    if otv: 
        textn["text"] = ""
        textn.update()
        tm.delete(0, END)
        tm.update()

root = Tk()
root.geometry("1000x500")
root.resizable(False, False)

tm = Listbox(root, font=("Microsoft Yahei", 5), width=100, height=25, bg="#555", fg="#111")
tm.pack()

textn = Label(root, text="", font=("Microsoft Yahei", 14))
textn.pack(side=RIGHT)

textf = Label(root, text="File name", font=("Microsoft Yahei", 14))
textf.pack(anchor=NW, padx=6, pady=6)
entry = Entry()
entry.pack(anchor=NW, padx=6, pady=6)

textx = Label(root, text="Width", font=("Microsoft Yahei", 14))
textx.pack(anchor=NW, padx=6, pady=6)
entryX = Entry()
entryX.pack(anchor=NW, padx=6, pady=6)

texty = Label(root, text="Height", font=("Microsoft Yahei", 14))
texty.pack(anchor=NW, padx=6, pady=6)
entryY = Entry()
entryY.pack(anchor=NW, padx=6, pady=6)

bt_sev = Button(root, text="Convect", padx="5", pady="3", command=go_to_list8)
bt_sev.pack(side=RIGHT)

bt_sev1 = Button(root, text="Delete", padx="5", pady="3", command=delete)
bt_sev1.pack(side=RIGHT)

root.mainloop()
