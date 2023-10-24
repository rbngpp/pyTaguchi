from pyTaguchi.taguchi import Taguchi

var1 = {"name": "Variable n.1", "values": [30, 35, 40]}

var2 = {"name": "Variable n.2", "values": [20, 30, 40]}

var3 = {"name": "Variable n.3", "values": [10, 27, 50]}

var4 = {"name": "Variable n.4", "values": [0.2, 0.5, 0.7]}

tg = Taguchi()
tg.add(var1)
tg.add(var2)
tg.add(var3)
tg.add(var4)
tg.run(randomize=True,plot=True)
