#include <iostream>
#include <math.h>

using namespace std;



int main() {

   float peso, altura, IMC;

   cout << "Qual seu peso?\n";
   cin >> peso;
   cout << "Qual sua altura?\n";
   cin >> altura;

   IMC = peso / (pow(altura, 2));

   cout << "Seu IMC e: " << IMC << endl;

   if (IMC <= 18.5)
   {
    cout << "Voce esta na faixa abaixo do peso" << endl;
   }
   else if (IMC < 25)
   {
    cout << "Voce esta na faixa de peso ideal" <<  endl;
   }
   else if (IMC < 30)
   {
    cout << "Voce esta na faixa de sobrepeso" <<  endl;
   }
   else if (IMC < 35)
   {
    cout << "Voce esta na faixa de obesidade grau I" <<  endl;   
   }
   else if (IMC < 40)
   {
    cout << "Voce esta na faixa de obesidade grau II" <<  endl;
   }
   else
   {
    cout << "Voce esta na faixa de obesidade grau III" <<  endl;
   }


    return 0;
}