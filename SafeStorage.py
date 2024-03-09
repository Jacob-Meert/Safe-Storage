import tkinter as tk
import WindowMethod as wind



def home():
    def entrychangeE():
        if extension.get() == '':
            error('Error: no key file extension')
        elif store.get() == '':
            error('Error: no text file extension')
        else:
            entry(extension.get(), store.get())
    
    def entrychangeR():
        if extension.get() == '':
            error('Error: no file extension')
        elif store.get() == '':
            error('Error: no text file extension')
        else:
            access(extension.get(), store.get())

    home = tk.Tk()
    #design
    home.title("Homepage")
    home.geometry("800x700")
    home.configure(bg = 'gray20')

    pagechangeE = tk.Button(text = "Add entry", width = 20, height = 3, background = "white", highlightbackground="#ADD8E6", fg = "black",command= entrychangeE)
    pagechangeE.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    pagechangeR= tk.Button(text = "Interact with Data", width = 20, height = 3, background = "white", highlightbackground="#ADD8E6", fg = "black",command= entrychangeR)
    pagechangeR.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    hometitle = tk.Label(text = "Safe Storage App", font=("ariel",60,"bold"), fg = "#1a94d6", bg = "gray20")
    hometitle.place(relx = 0.5, rely = 0.25, anchor=tk.CENTER)

    extension = tk.Entry(home, bg = "white", fg = "black", highlightbackground="#ADD8E6", width = 15)
    extension.place(relx = 0.3, rely = 0.02, anchor = tk.CENTER)

    extension_label = tk.Label(home, text = 'Key Storage Path:', font=("ariel",15,"bold"), fg = "#1a94d6", bg = "gray20")
    extension_label.place(relx = 0.11, rely = 0.02, anchor = tk.CENTER)

    store = tk.Entry(home, bg = "white", fg = "black", highlightbackground="#ADD8E6", width = 15)
    store.place(relx = 0.3, rely = 0.065, anchor = tk.CENTER)

    store_label = tk.Label(home, text = 'Text Storage Path:', font=("ariel",15,"bold"), fg = "#1a94d6", bg = "gray20")
    store_label.place(relx = 0.11, rely = 0.065, anchor = tk.CENTER)
    home.mainloop()

def access(keyextension, textextension):

    def errorCall(call):
        if call == 'search':
            if infoentry.get() not in wind.getFiles(textextension):
                error('Error: File not found')
            else:
                title = infoentry.get()
                last = wind.retrieve(title, keyextension, textextension)
                if last == 'Error1':
                    error('Error: Key-File pairing not found')
                elif last == 'Error2':
                    error('Error: Key file lost')
                else:
                    results(last, title)
        elif call == 'delete':
            if infoentry.get() not in wind.getFiles(textextension):
                error('Error: File not found')
            else:
                warn('Warning: Deleted files are not recoverable', call, infoentry.get(), keyextension, textextension)
        elif call == 'delete all':
            warn('Warning: You are about to permenantly delete all of your saved files', call, infoentry.get(), keyextension, textextension)

    data = tk.Tk()
    data.title("Data Interaction")
    data.geometry("800x700")
    data.configure(bg = 'gray20')

    rightFrame = tk.Frame(data, bg = "gray20")
    rightFrame.pack(fill=tk.BOTH, expand = True)

    listbox = tk.Listbox(data, selectmode=tk.SINGLE, highlightbackground="#ADD8E6", highlightthickness=3)
    files = wind.getFiles(textextension)
    for f in files:
        listbox.insert(tk.END, f)
    listbox.place(relx = 0.7, rely = 0.5, anchor = tk.CENTER)

    infoentry = tk.Entry(data, bg = 'white', fg = 'black', width = 20, highlightbackground="#ADD8E6")
    infoentry.place(relx = 0.3, rely = 0.5, anchor = tk.CENTER)

    filea = tk.Label(data, text = 'File to interact with:', font=("ariel",20,"bold"), fg = "#1a94d6", bg = "gray20")
    filea.place(relx = 0.3, rely = .4, anchor = tk.CENTER)

    fileavail = tk.Label(data, text = 'Files available to you:', font=("ariel",20,"bold"), fg = "#1a94d6", bg = "gray20")
    fileavail.place(relx = 0.7, rely = .3, anchor = tk.CENTER)

    submit = tk.Button(data, text = "search", width = 20, height = 3, background = "white", highlightbackground="#ADD8E6", fg = "black", command= lambda: errorCall('search'))
    submit.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

    delete = tk.Button(data, text = "delete file", width = 20, height = 3, background = "white", highlightbackground="#ADD8E6", fg = "black", command= lambda: errorCall('delete'))
    delete.place(relx=0.5, rely=0.83, anchor=tk.CENTER)

    deleteall = tk.Button(data, text = "Wipe files", width = 20, height = 3, background = "white", highlightbackground="red", fg = "black", command= lambda: errorCall('delete all'))
    deleteall.place(relx=0.5, rely=0.93, anchor=tk.CENTER)

    data.mainloop()

def entry(keyextension, textextension):

    root = tk.Tk()
    def errorCall(call):
        if call == 'filename':
            result = wind.save(text.get("1.0", "end-1c"),titleSave.get(), keyextension, textextension)
            if result == 'Error1':
                error("Error: No title entered")
            if result == 'Error2':
                error("Error: Path not found")
    #design
    root.title("Data Entry")
    root.geometry("800x700")
    root.configure(bg = 'gray20')

    leftFrame = tk.Frame(root, bg = "gray20")
    leftFrame.pack(fill=tk.BOTH, expand = True)

    text = tk.Text(root, fg = "black", bg = "white", highlightbackground="#ADD8E6")
    text.place(relx=0.5, rely=0.51, anchor=tk.CENTER)

    title = tk.Label(root, text = "Type Your Entry", font=("ariel",60,"bold"), fg = "#1a94d6", bg = "gray20")
    title.place(relx=0.5, rely=0.13, anchor=tk.CENTER)

    titleSave = tk.Entry(root, bg = "white", fg = "black", highlightbackground="#ADD8E6")
    titleSave.place(relx=0.5, rely=0.24, anchor=tk.CENTER)

    submit = tk.Button(root, text = "submit", width = 20, height = 3, background = "white", highlightbackground="#ADD8E6", fg = "black", command= lambda: errorCall('filename'))
    submit.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


    label_T = tk.Label(root, text = "Title:", font=("ariel",15,"bold"), fg = "#1a94d6", bg = "gray20")
    label_T.place(relx=0.33 , rely=0.24, anchor=tk.CENTER)

    root.mainloop()

def warn(warning, action, filename, keypath, textpath):
    def close():
        warnwindow.destroy()
    def distinguish():
        if action == 'delete':
            wind.deleteFile(filename, textpath)
            warnwindow.destroy()
        elif action == 'delete all':
            wind.clearFiles(keypath, textpath)
            warnwindow.destroy()
    warnwindow = tk.Tk()
    warnwindow.title("Warning")
    if action == 'delete':
        warnwindow.geometry('600x300')
    else:
        warnwindow.geometry('1000x300')
    warnwindow.configure(bg = 'gray20')

    actual = tk.Label(warnwindow, text = warning,  fg = "#1a94d6", bg = "gray20", font = ('ariel', 30))
    actual.place(relx = 0.5, rely = 0.32, anchor = tk.CENTER)

    consistent = tk.Label(warnwindow, text = "Are you sure you want to proceed?",  fg = "#1a94d6", bg = "gray20", font = ('ariel', 15))
    consistent.place(relx = 0.5, rely = 0.45, anchor = tk.CENTER)

    confirm = tk.Button(warnwindow, text = 'YES', width = 10, height = 2, background = "white", highlightbackground="#ADD8E6", fg = "black", command = distinguish)
    confirm.place(relx = 0.35, rely = 0.68, anchor = tk.CENTER)

    deny = tk.Button(warnwindow, text = 'CANCEL', width = 10, height = 2, background = "white", highlightbackground="#ADD8E6", fg = "black", command = close)
    deny.place(relx = 0.65, rely = 0.68, anchor = tk.CENTER)

    warnwindow.mainloop()

def results(txt, title):
    result = tk.Tk()
    result.title(f'Results: {title}')
    txtw = tk.Text(result, bg = 'white', fg = 'black')
    txtw.pack(fill = tk.BOTH, expand = True)
    txtw.insert(tk.END, txt)
    result.mainloop()


def error(errormarker):
    errorframe = tk.Tk()
    errorframe.title("Error")
    errorframe.configure(bg = 'gray20')
    tk.Label(errorframe, text = errormarker, bg = "white", fg = "black", font=("ariel", 30)).pack()
    errorframe.mainloop()

home()


