programa {
  funcao inicio() {
     //Algoritmo para calcular a m�dia entre 4 notas.
    //O usu�rio digitar� as 4 notas e ao final
    //o algoritmo exibir� a m�dia final.

    //Declara��o de vari�veis
    real nota1, nota2, nota3, nota4, media

    //Atribui��o das vari�veis
    escreva("Digite a nota do 1� bim: ")
    leia(nota1)
    escreva("Digite a nota do 2� bim: ")
    leia(nota2)
    escreva("Digite a nota do 3� bim: ")
    leia(nota3)
    escreva("Digite a nota do 4� bim: ")
    leia(nota4)

    media = (nota1 + nota2 + nota3 + nota4) / 4
    escreva("A m�dia final = ", media)
  }
}
