class Cachorro:
    def __init__(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = True
        self.feliz = True
        self.energia = 100
        
    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Comida: {self.comida}, Acordado: {self.acordado}, Feliz: {self.feliz}"
        
    def comer(self,quantidade):
        self.comida -= quantidade
        if self.acordado is True:
         print(f"{self.nome} está comendo e está muito feliz!!")
        else:
         print(f"{self.nome} está dormindo e não pode comer!!")
        
    def dormir (self):
        self.acordado = False
        print (f"{self.nome} está domindo agora.🤫💤")
        
    def acordar (self):
        self.acordado = True
        print(f"{self.nome} acordou!!🥱")
        
    def brincar (self):
        if self.acordado is True:
            if self.energia >= 20:
                print(f"{self.nome} está brincando e está muito feliz!!🥏!!")
            else:
                print(f"{self.nome} está sem energia e não pode brincar!!")
        else:
            print(f"{self.nome} está dormindo e não pode brincar!") 
        
        
    def ignorar (self):
        self.ignorar = True
        print(f"{self.nome} está sendo ignorado e por isso está triste!!")
        
    def latir (self):
        if self.acordado is True:
         print(f"{self.nome} está latindo!!")
        else:
         print(f"{self.nome} está dormindo e não pode latir") 
         

        
# Criando um objeto de classe cachorro
meu_cachorro=Cachorro ("Enzo", "Dachshund", 5)
        

#Interagindo com o objeto
meu_cachorro.comer(2)
meu_cachorro.brincar ()
meu_cachorro.ignorar()
meu_cachorro.latir()
meu_cachorro.dormir()
meu_cachorro.latir()
meu_cachorro.acordar()
meu_cachorro.latir()
