

programa {
  funcao inicio() {
    //Calculando a M�dia 
   //Declara��o de vari�veis
   real nota1, nota2, nota3, nota4, media

  //Atribui��o das notas
   escreva("Calculando a m�dia final\n")
   escreva("Digite a nota do 1� Bimestre: ") 
   leia(nota1)
   escreva("Digite a nota 2� Bimestre: ")
   leia(nota2)
   escreva("Digite a nota 3� Bimestre: ")
   leia(nota3)
   escreva("Digite a nota 4� Bimestre: ")
   leia(nota4)
  
   //Calculando eExibindo resultado final 
    media = (nota1 + nota2 + nota3 + nota4)/4
   escreva("\nA m�dia final =  ", media)

   //Estrutura de decis�o
   se(media >=8){
    escreva("\nAluno aprovado.")
   } senao {
    escreva("\nAluno reprovado.")
   }

  }
}