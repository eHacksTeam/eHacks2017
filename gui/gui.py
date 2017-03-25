from appJar import gui

def press(name):
	print("run script to get tweet")

app = gui()
app.addLabel("title","Mean Tweet finder", 0, 1)  # Row 0,Column 0,Span 2
app.addLabel("tboxlabel", "Tweet URL:", 1, 0)
app.addEntry("box", 1, 1)
app.addButtons(["Analyze"], [press], 1, 2) # Row 3,Column 0,Span 2

app.go()