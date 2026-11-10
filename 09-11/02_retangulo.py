# Crie a classe Retangulo, inicializada com largura e altura, ambas positivas. Implemente calcular_area(), que devolve a multiplicação dessas medidas.

# Crie dois objetos e mostre suas áreas fora do método. Teste com medidas 4 e 3: área 12.

# Para explicar: qual é a diferença entre retornar a área e mostrá-la dentro do método?
# Se retornarmos o valor chamando o metodo do objeto, podemos usar esse valor para outra variavel, se utilizarmos apenas o print para mostrarmos o valor não vamos conseguirmos utilizar o valor para outra parte do codigo(vai retornar none)


class retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura


    def calcular_area(self):
        return self.altura * self.largura
retangulo1 = retangulo(4,3)
print(retangulo1.calcular_area())
    
        