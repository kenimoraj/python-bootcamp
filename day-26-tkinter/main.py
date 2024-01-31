import tkinter

FONT = ("Calibri", 20, "bold")

def calculate_km():
    km = float(entry.get())*1.609
    result.config(text=km)


window = tkinter.Tk()
window.title("Miles To Kilometers Calculator")

entry = tkinter.Entry(font=FONT)
entry.grid(row=0, column=1)

miles = tkinter.Label(text="miles", font=FONT)
miles.grid(row=0, column=2)

is_equal = tkinter.Label(text="is equal to", font=FONT)
is_equal.grid(row=1, column=0)

result = tkinter.Label(text="0", font=FONT)
result.grid(row=1, column=1)

km = tkinter.Label(text="km", font=FONT)
km.grid(row=1, column=2)

calculate = tkinter.Button(text="Calculate", font=FONT, command=calculate_km)

calculate.grid(row=2, column=1)


window.config(padx=100,pady=200)
window.mainloop()
