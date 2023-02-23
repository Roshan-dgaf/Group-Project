from tkinter import *
from time import sleep
import random
import threading

# function
totaltime=60
time=0
wrongwords=0
elapsedtimeinminutes=0
def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime=totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        typing_test.update()

    textarea.config(state=DISABLED)

def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph=textarea.get(1.0,END).split()
        totalwords=len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list=label_paragraph['text'].split()

    for pair in list(zip(para_word_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes=time/60
    wpm=(totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm=totalwords/elapsedtimeinminutes


def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


# GUI
typing_test = Tk()
typing_test.title("start typing test")
typing_test.geometry("1450x670+50+80")
 # typing_test.attributes("-transparentcolor" , "white")
typing_test.resizable(0,0)
typing_test.config(bg="grey80")
typing_test.overrideredirect(1) # to hide window(minimize , maximize , close)


paragraph_frame=Frame(typing_test , bg="grey80" , width=1450 , height=200)
paragraph_frame.place(x=0 , y=0)
    


paragraph_list = ["""The quick brown fox jumps over the lazy dog. A quick movement of the enemy will jeopardize six gun boats. The sun was shining on the sea, shining with all his might. He did his very best to make the billows smooth and bright and this was odd because it was the middle of the night.""" , 
    
    """Improving your typing speed and accuracy requires regular practice and patience. Start by setting aside time each day to practice typing on a variety of websites or typing software. As you type, focus on keeping your hands in the correct position on the home row keys and using all your fingers, not just a few. Try to type without looking at the keyboard and keep your eyes on the screen to increase your speed and accuracy. It's also helpful to learn the correct finger placement for each key and to use proper posture and a comfortable chair to prevent strain on your hands and arms. """ ,
    
      """Thi paragragh conatins phrazes and werds that are difficult to tpye becuase it has confsuing speling and grammer. For exmple, "Thi" insted of "This" and "tpye" insted of "type." It may be chanllenging for sme peple to read, but with praktice and atention to detail, impoving spelling and grammer can be achived."""]

random.shuffle(paragraph_list)


label_paragraph = Label(paragraph_frame , text=paragraph_list[0] , fg="black" , bg="grey80" ,wraplength=1400 , font="aeriel 18 bold")
label_paragraph.place(x=30 , y=30)

textarea_frame = Frame(typing_test , bg="grey80" , width=1000 , height=400)
textarea_frame.place(x=200 ,y=250)

textarea = Text(textarea_frame , bg="white" , fg="black" , width=76 , height=400 ,borderwidth=7 , font="aerial 18 bold" , wrap="word" , relief=GROOVE , state=DISABLED)
textarea.place(x=0 , y=0)

frame_output = Frame(typing_test , bg="white" , width=1450 , height=50)
frame_output.place(x=0 , y=200)

elapsed_time_label = Label(frame_output , bg="white" , fg="red" , text="Elasped Time : " , font="tahoma 12 bold")
elapsed_time_label.place(x=10 ,y=8)
elapsed_timer_label = Label(frame_output , bg="white" , fg="red" , text="0" , font="tahoma 12 bold")
elapsed_timer_label.place(x=150 , y=8)

remaining_time_label = Label(frame_output , bg="white" , fg="red" , text="Remaining Time : " , font="tahoma 12 bold")
remaining_time_label.place(x=280 , y=8)

remaining_timer_label = Label(frame_output , bg="white" , fg="red" , text="60" , font="tahoma 12 bold")
remaining_timer_label.place(x=450 , y=8)

wpm_label = Label(frame_output , bg="white" , fg="red" , text="WPM : " , font="tahoma 12 bold")
wpm_label.place(x=630 , y=8)

wpm_count_label = Label(frame_output , bg="white" , fg="red" , text="0" , font="tahoma 12 bold")
wpm_count_label.place(x=700 , y=8)

totalwords_label = Label(frame_output , bg="white" , fg="red" , text="Total Words : " , font="tahoma 12 bold")
totalwords_label.place(x=800 , y=8)

totalwords_count_label = Label(frame_output , bg="white" , fg="red" , text="0" , font="tahoma 12 bold")
totalwords_count_label.place(x=930 , y=8)

wrongwords_label = Label(frame_output , bg="white" , fg="red" , text="Wrong Words : " , font="tahoma 12 bold")
wrongwords_label.place(x=1050 , y=8)

wrongwords_count_label = Label(frame_output , bg="white" , fg="red" , text="0" , font="tahoma 12 bold")
wrongwords_count_label.place(x=1200 , y=8)

button_frame = Frame(typing_test , bg="grey80" , width=230 , height=400 , borderwidth=5)
button_frame.place(x=1210 , y=250)

startButton = Button(button_frame, text="<< Start >>" , width=10 , height=2  , fg="white" , bg="green" , border=10 , font="monospace 10 bold" , command=start)
startButton.place(x=50 , y=120)

exitButton = Button(button_frame , text=">> Exit <<" , width=10 , height=2 , command=typing_test.destroy , fg="white" , bg="red" , border=10 , font="monospace 10 bold")
exitButton.place(x=50 , y=200)


button_frame_left = Frame(typing_test , bg="#1429A9" , width=180 , height=400 , borderwidth=5)
button_frame_left.place(x=10 , y=250)

button_frame_left_label = Label(button_frame_left , text="Start Typing Here --->" , font="algerian 20 bold" , wraplength=100 , bg="#1429A9" , fg="white")
button_frame_left_label.place(x=20 , y=120)






typing_test.mainloop()