
import tkinter
import datetime
import winsound
def alarmCountdown(count):
    

    alarmHour = int(input("hour: "))
    alarmMinute = int(input("minute: "))
    amPm = str(input("am or pm: "))
    label['text'] = "Hours: " + str(alarmHour) + "Minutes: " + str(alarmMinute) + "am or pm: " + str(amPm)

    if (amPm == "pm"):
        alarmHour = alarmHour + 12

    while True:
        if(alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
            continue
        else:
            for x in range(5):
                winsound.Beep(1000,1000)
            label['text'] = "Time is up!"
            break

def updateButton():
    hour,minute = hoursE.get(), minuteE.get()
    if hour.isdigit() and minute.isdigit():
        time = int(hour)*3600 + int(minute)*60
        alarmCountdown(time)


top = tkinter.Tk()
top.title("alarm clock")
top.geometry("250x150")
hoursT = tkinter.Label(top, text = "Hours")
hoursE = tkinter.Entry(top)

minuteT = tkinter.Label(top, text = "Minutes")
minuteE = tkinter.Entry(top)

PmAmT = tkinter.Label(top, text = "am or pm?")
PmAmE = tkinter.Entry(top)

hoursT.grid(row = 1, column = 1)
hoursE.grid(row = 1, column = 2)

minuteT.grid(row = 2, column = 1)
minuteE.grid(row = 2, column = 2)

PmAmT.grid(row = 3, column = 1)
PmAmE.grid(row = 3, column = 2)

label = tkinter.Label(top)
label.grid(row = 5, column = 2)

button = tkinter.Button(top, text = "Start clocking", command = updateButton)
button.grid(row = 4, column = 2)

top.mainloop()
 
