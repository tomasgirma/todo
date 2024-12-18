import PySimpleGUI as gui

layout = gui.Text("Type in a to-do list")
input_box = gui.InputText(tooltip="Enter ToDo")

window = gui.Window("My ToDo App", layout=[[layout, input_box]])

window.read()