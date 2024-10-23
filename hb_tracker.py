
import tkinter as tk

KEKKA = [
"You’re not doing good, Please get back on track.",
"You’re at the Starter Level",
"毎日少しずつがんばりましょう!",
"がんばって、あきらめないでください",
"Neutral Habit、あと少しがんばってください",
"お疲れ様です！、これから健康が良くなる",
"Good Habit! もうちょっとがんばって!!",
"Very Good Habit! あと少しだけプロになる",
"Goal!! おめでとうございます。You’re at the Pro Level"
]
ITEM = [
"Eating Healthily",
"No Sweets",
"8 cups of Water",
"Bed by 10PM",
"Wake by 6PM",
"Walk 20 min",
"Read a book",
"Yoga 20 mins"
]
def click_btn():
    pts = 0
    for i in range(8):
        if bvar[i].get() == True:
            pts += 1
    nekodo = int(100*pts/8)
    text.delete("1.0", tk.END) # 全消し
    #1.0は1行目、0文字目からつまり先頭から
    text.insert("1.0", '＜今日のスコア＞\nあなたのHabit Scoreは{}%です。\n{}'.format(nekodo,KEKKA[pts]))

root = tk.Tk()
root.title("Calculate Your Habit Score")
root.resizable(False, False)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
img = tk.PhotoImage(file="background5.png")
canvas.create_image(400, 300, image=img)
button = tk.Button(text="Habit Tracker", font=("Times New Roman", 19), bg="lightgreen", command=click_btn)
button.place(x=430, y=530)
text = tk.Text(width=35, height=5, font=("Times New Roman", 16))
text.place(x=310, y=390)

bvar = [None]*8
cbtn = [None]*8

for i in range(8):
    bvar[i] = tk.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tk.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="white")
    if i<4:
        cbtn[i].place(x=50+200*i, y=140+i)
    else:
        cbtn[i].place(x=-750+200*i, y=300+i)
root.mainloop()
