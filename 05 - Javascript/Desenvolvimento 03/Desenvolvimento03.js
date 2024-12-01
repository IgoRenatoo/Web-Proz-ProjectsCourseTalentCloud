/* === Exercício de Loop em Javascrip === */

/*
NOTE: Classificar cada número com base nas condições:
* X é par e menor que 50
* X é menor que 50
* X é maior que 50
*/

const numerosDaSorte = [37, 14, 26, 5, 94, 87]

for (let i = 0; i < numerosDaSorte.length; i++) {
  if (numerosDaSorte[i] % 2 === 0 && numerosDaSorte[i] < 50) {
    console.log(`O array de posição ${i}, ${numerosDaSorte[i]} é par e menor que 50`)
  }
  else if (numerosDaSorte[i] < 50) {
    console.log(`O array de posição ${i}, ${numerosDaSorte[i]} é menor que 50`)
  }
  else {
    console.log(`O array de posição ${i}, ${numerosDaSorte[i]} é maior que 50`)
  }
}
