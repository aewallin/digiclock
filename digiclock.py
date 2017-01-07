# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
# https://www.daniweb.com/software-development/python/code/216785/tkinter-digital-clock-python
# http://en.sharejs.com/python/19617

# Anders E. Wallin, 2015-04-24
# GPLv3 license.
#
# added: UTC, localtime, date, MJD, DOY, week
from Tkinter import *
import time
import jdutil # https://gist.github.com/jiffyclub/1294443

root = Tk()
root.attributes("-fullscreen", True) 
# this should make Esc exit fullscrreen, but doesn't seem to work..
#root.bind('<Escape>',root.attributes("-fullscreen", False))
root.configure(background='black')

#root.geometry("1280x1024") # set explicitly window size
time1 = ''
clock_lt = Label(root, font=('arial', 230, 'bold'), fg='red',bg='black')
clock_lt.pack()

date_iso = Label(root, font=('arial', 75, 'bold'), fg='red',bg='black')
date_iso.pack()

date_etc = Label(root, font=('arial', 40, 'bold'), fg='red',bg='black')
date_etc.pack()

clock_utc = Label(root, font=('arial', 230, 'bold'),fg='red', bg='black')
clock_utc.pack()

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S') # local
    time_utc = time.strftime('%H:%M:%S', time.gmtime()) # utc
    # MJD
    date_iso_txt = time.strftime('%Y-%m-%d', time.gmtime()) + "    %.5f" % jdutil.mjd_now()
    # day, DOY, week
    date_etc_txt = "%s   DOY: %s  Week: %s" % (time.strftime('%A'), time.strftime('%j'), time.strftime('%W'))

    if time2 != time1: # if time string has changed, update it
        time1 = time2
        clock_lt.config(text=time2)
        clock_utc.config(text=time_utc)
        date_iso.config(text=date_iso_txt)
        date_etc.config(text=date_etc_txt)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock_lt.after(20, tick)

tick()
root.mainloop()
