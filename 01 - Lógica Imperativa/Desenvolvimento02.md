# 📜 Desenvolvimento 02 

## 🎯 Descrição do Projeto 

Em uma sala de aula, <b>há vinte e cinco alunos</b>. Entre eles, existem os grupos dos que gostam de Português (P) e os que gostam de Matemática (M). Eles estão organizados na sala de forma alternada, conforme apresentado a seguir:

|   |   |   |   |   |
|---|---|---|---|---|
| P | P | M | P | M |
| M | P | M | M | P |
| M | M | M | P | M |
| M | P | P | M | P |
| P | M | M | P | M |

Chegaram mais <b>onze alunos</b> nessa turma e o professor organizou a turma da seguinte maneira:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
| P | P | M | P | M | P |
| M | P | M | M | P | M |
| M | M | M | P | M | P |
| M | P | P | M | P | P |
| P | M | M | P | M | M |
| M | P | P | P | M | P | 

No entanto, o professor se ausentou da sala por cinco minutos e, ao voltar, percebeu que um aluno que gosta de uma das disciplinas havia trocado de lugar com alguém que prefere a outra pois a configuração ficou dessa maneira:

|   |   |   |   |   |   |
|---|---|---|---|---|---|
| P | P | M | P | M | P |
| M | P | M | M | P | M |
| M | M | M | P | M | P |
| M | P | `M` | M | P | P |
| P | M | M | P | `P` | M |
| M | P | P | P | M | P | 

Sabendo que o professor tem dificuldade de memorizar, informe como ele descobriu a cadeira em que houve a troca de alunos e qual a disciplina de cada um. 

## 🛠️ Resolução

Ele descobriu pois ao retornar para a sala de aula ele percebeu que uma coluna tinha uma fileira com 5 alunos sequenciados com a prova de matematica `M`, sendo que ele tinha colocado um máximo de 3 sequencias da mesma prova.