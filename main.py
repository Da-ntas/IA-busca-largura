import buscaLargura
from no import *
from buscaLargura import *

b = No("b")
f = No("f")
d = No("d")
a = No("a")
c = No("c")
e = No("e")
j = No("j")
k = No("k")
g = No("g")
h = No("h")
i = No("i")
l = No("l")

b.set_adjacentes([a, d, e])
f.set_adjacentes([c, e])
d.set_adjacentes([g])
a.set_adjacentes([h, i])
c.set_adjacentes([])
e.set_adjacentes([j, k])
j.set_adjacentes([])
k.set_adjacentes([])
g.set_adjacentes([])
h.set_adjacentes([])
i.set_adjacentes([l])
l.set_adjacentes([])

busca = BuscaLargura()

busca.executar(b)

print(busca.percorrer_caminho(l))






