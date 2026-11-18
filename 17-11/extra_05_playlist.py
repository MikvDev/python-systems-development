class PLaylist:
        def __init__(self, nome):
            self.nome = nome
            self.musicas = []

        def adicionar(self, titulo):
            if titulo == "" or titulo in self.musicas:
                return False
            
            else:
                self.musicas.append(titulo)
                return True
        def quantidade_musicas(self):
            return len(self.musicas)

p2 = PLaylist("Viagem")
p1 = PLaylist("Estudo")

print(p1.adicionar("Chuva"))
print(p1.adicionar("Piano"))
print(p1.adicionar("Chuva"))
print(p1.adicionar(""))

p2.adicionar("Estrada")

print(p1.nome, p1.musicas, p1.quantidade_musicas())
print(p2.nome, p2.musicas, p2.quantidade_musicas())


for musica in p1.musicas:
        print(musica)

# Para explicar: o que poderia acontecer se musicas = [] fosse declarada diretamente no corpo da classe?
# Todas os objetos teriam as mesmas musicas, acabaria com o sentido de ter playlists com musicas diferentes.