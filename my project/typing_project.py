from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk
import ttkthemes

typ = ttkthemes.ThemedTk()
typ.get_themes()
typ.set_theme("radiance")


# typ.attributes('-fullscreen',True)
typ.geometry("1532x800+0+0")
typ.resizable(0,0)
typ.title("typing test")


def start_typing_test():
    import nw_typing_test_btn

def extra_mode():
    typ.destroy()
    import extra_mode
    


bg_image = Image.open("1_typing_projectt.jpg")
bg_image = bg_image.resize((1532,800))
bck_end_img = ImageTk.PhotoImage(bg_image)


lbl = Label(typ , image=bck_end_img)
lbl.place(x=0 , y=0)



# Label(typ,text="Test and Improve Your Typing Speed",font=("Urbanist",45),fg="white",).pack(pady=250)
# typ.wm_attributes('-transparentcolor', typ['bg'])


start_typing_test = ttk.Button(typ , text="Start Typing Test" , command=start_typing_test)
start_typing_test.place(x=600 , y=500)

extra_game = ttk.Button(typ , text="Extra Modes" , command=extra_mode)
extra_game.place(x=800 , y=500)





typ.mainloop()