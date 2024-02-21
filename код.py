import tkinter
def generate(number_of_symbols=6):
  import random
  symbols = []
  for i in range(number_of_symbols):
      num = random.randint(1, 3)
      if num == 1:
          symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
      elif num == 2:
          symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
      elif num == 3:
          symbols.append(random.choice('0123456789'))
  password = ''.join(str(symb) for symb in symbols)
  text.delete('1.0', tkinter.END)
  text.insert('1.0', password)
number_of_symbols = 2
window = tkinter.Tk()
window.config(background="pale green")
window.geometry("900x700")
text=tkinter.Text(
    font=("Arial", 60,"bold"),
    height=1,
    width=number_of_symbols+1,
    bg="black",
    fg="violet",
    borderwidth=15)
text.pack(expand=1)
tkinter.Button(
    text="Generate",
    font=("arial",40,"bold"),
    bg="black",
    fg="white",
    borderwidth=0,
    command=lambda:generate(number_of_symbols)
).pack(expand=1)



window.mainloop()
