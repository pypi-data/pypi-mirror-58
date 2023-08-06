/* globals Mindspace, socketURL */
const m = new Mindspace()
m.addCommand("alert", alert)
m.connect(socketURL)
m.sendCommand({name: "echo", args: ["This is a lovely alert box that magically appears."]})
