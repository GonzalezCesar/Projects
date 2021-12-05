from tkinter import *
import pyshorteners
import clipboard 


window = Tk()

#set deafault window size (Establecer el tamaño de ventana predeterminado)
window.geometry("400x200")

#
window.resizable(False, False)

window.title("URL Shortener")

# url entry (entrada de url)
url_input = Entry(window, font=("Helvetica","16"))
url_input.grid(row=1, column=2, pady=6)

#label shortened url (etiqueta url abreviada)
str_url = StringVar(window)

shortened_url = Label(window, textvariable=str_url, font=("Helvetica","16"), fg="#fff", bg="#1abc9c")
shortened_url.grid(row=3, column=2, pady=6)


# copy short url function (copiar funcion de url corta)
def copy_short_url():
    try:
      clipboard.copy(str_url.get())
      print("Url copied succesfully !!")
    except:
        str_url.set("Something wrong try again !!")


# Copy short url button (Copiar el boton de url corta)
copy_btn = Button(window, text="Copy", bg="#34495e", fg="#fff", font=("Helvetica","12"), command=copy_short_url)
copy_btn.grid(row=3, column=3, pady=6, padx=10)


#short url fuction (funcion de url corta)
def short_url():
    try:
        s = pyshorteners.Shortener()
        url = url_input.get()
        final_result = s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0, END) # entrada clara
    except:
        str_url.set("Enter url please !! ")


#click button to short url (Boton para acortar la url)
btn = Button(window, text="Short Url", padx=8, pady=4, bg="#2ecc71", fg="#fff", font=("Helvetica","16"), activebackground="#16a085", command=short_url)
btn.grid(row=2, column=2, pady=6)





window.mainloop()