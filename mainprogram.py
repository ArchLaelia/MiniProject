import tkinter as tk
import mainfun


class Base:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.printButton = tk.Button(frame, text="Search from folder",
                                     command=self.printMessage)
        self.printButton.pack(side="left")

        self.quitButton = tk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side="left")

    def printMessage(self):
        frame1 = tk.Toplevel()

        tk.Label(frame1, text="Länk address").grid(row=0)

        self.link = tk.Entry(frame1)
        self.link.grid(row=0, column=1)

        self.searchButton = tk.Button(frame1, text="Sök",
                                      command=self.GetFile)
        self.searchButton.grid(row=1)

    def GetFile(self):
        files = mainfun.FindFiles(self.link.get())
        for file in files:
            print(file)


root = tk.Tk()
b = Base(root)

root.mainloop()
