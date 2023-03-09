#Додатковий функціонал до певної задачі
import  webbrowser

def checkpoint(func):    #блок №4-13 це декораторм
    def wrapper(url):
        if "." in url:

         func(url)
        else:
         print("Ввел хуйню")
    return  wrapper

@checkpoint
def open_url(url):
    webbrowser.open(url)

open_url("https://itprogercom")