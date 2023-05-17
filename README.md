
<table>

<tr>

</td>

  

<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="80%"></a>

</td>

</tr>

</table>

  

<font  size="20"><center>

# Simulação de robôs móveis com Gazebo

</center></font>

  

# **Sumário**

  

- [Autores](#autores)


- [Visão Geral do Projeto](#visão-geral-do-projeto)


- [Objetivos](#objetivos)


- [Desenvolvimento](#desenvolvimento)
  

- [Referências](#referências)


# Autores

  

Kil Matheus Gomes Teixeira

  

# Visão Geral do Projeto


# Objetivos

Crie um pacote em ROS capaz de interagir com uma simulação feita no Gazebo de modo que a plataforma simulada do turtlebot3 seja capaz de mover-se de maneira controlada.

## Requisitos

Segundo o card do AdaLove do prof. Rodrigo Mangoni Nicola, os requisitos são descritos como seguintes:

Padrão de qualidade:  
  
Para esta atividade, espera-se a capacidade demonstrável de interagir com um ambiente de simulação de robôs, gerando um movimento controlado na plataforma turtlebot3. A entrega deve ser um vídeo demonstrando o funcionamento do projeto, um texto conciso descrevendo como foi feita a implementação e o link para o repositório público no Github onde foi feita a implementação.
1.  Setup adequado do ambiente de simulação; (peso 1)
2.  Interação adequada com os tópicos relacionados ao robô simulado; (peso 2)
3.  Demonstração de movimento controlado de acordo com uma rota pré-estabelecida; (peso 3)
4.  Explicação coerente e concisa da implementação (min 250 caracteres e máximo 1500); (peso 2)
5.  Congruência entre o que foi escrito e o código disposto no repositório do Github; (peso 2)


## Desenvolvimento

Para o desenvolvimento, foi utilizado os materiais disponíveis no Autoestudo do AdaLove pelo o professor de programação Nicola, e tambem um tutorial feito por um aluno do Inteli João Carazzato, onde os mesmos estarão linkados em referências nesse documento.

Para iniciarmos a nossa aplicação, precisamos abri o app 'Terminal' do Windows, e selecionarmos o ambiente do Ubuntu.

<center>
<img  src="img\sec_ambiente.png"  alt="Seleção do Ambiente Ubuntu"  />
</center>

**<font  size=2> Figura 1 — Selecionando Ambiente Ubuntu, Autoria Própria </font>**

<center>
<img  src="img\ambiente_1.png"  alt="Ambiente Ubuntu"  />
</center>

**<font  size=2> Figura 2 — Ambiente Ubuntu, Autoria Própria </font>**

Após abrirmos o terminal, após todas as instalações já terem sido feitas, colocamos os seguintes comandos:

Primeiramente, precisamos chegar no diretório correto para poder executar o ambiente de desenvolvimento:
<b>cd ros2_ws/src</b>

Para inicializar o ambiente:
<b>source  install/setup.bash</b>

Como o terminal só consegue roda um tarefa por vez, abrimos um segundo para poder rodar a aplicação do Gazebo já instalada:

<center>
<img  src="img\ubuntu_gazebo.png"  alt="Terminal Gazebo"  />
</center>

**<font  size=2> Figura 3 — Rodando o Gazebo no terminal, Autoria Própria </font>**

Para configurar o ambiente corretamente, primeiramente abrimos a aplicação e vamos procurar as instalações do Gazebo Turtle, a fim de importar os objetos para dentro da aplicação.

Primeiro precisamos acessar o "Insert"
<center>
<img  src="img\gazebo.png"  alt="Gazebo"  />
</center>

**<font  size=2> Figura 4 — Gazebo, Autoria Própria </font>**

Depois acessamos o "Add Path", na qual vai abrir um janela para selecionar um diretório e selecionamos "gazebo_models" e "Choose"

<center>
<img  src="img\caminho_gazebo.png"  alt="Caminho para o Turtle"  />
</center>

**<font  size=2> Figura 5 — Caminho para o Turtle, Autoria Própria </font>**

E após indicar o diretório, agora podemos instanciar um objeto no mundo.

<center>
<img  src="img\objeto_gazebo.png"  alt="Objeto Gazebo"  />
</center>

**<font  size=2> Figura 6 — Objeto Gazebo, Autoria Própria </font>**

Depois de ter feito todos esses passos, podemos rodar a nossa solução.
No primeiro terminar aberto, vamos compilar o nosso código desenvolvido para a aplicação consumir posteriormente, fazendo o robô se movimentar. Vamos rodar o seguinte comando:
<b>colcon build</b>

Código desenvolvido para a compilação:

<center>
<img  src="img\gazebo_python.png"  alt="Código Python"  />
</center>

**<font  size=2> Figura 7 — Código Python, Autoria Própria </font>**

A explicação do código em resumo, ele utiliza uma lista global para armazenar os valores das coordenadas que serão inseridas quando o programa requisitar manualmente, ou até mesmo  guardadas no próprio código. A classe 'TurtleController' ele herda o 'Node' do Ros, e com isso, nos conseguimos utilizar o Publisher e o Subscribe para enviar e receber informações para o Turtle na simulação Gazebo, que respectivamente são as funções 'publisher_callback' e 'listener_callback'. 
O programa vai fazer três perguntas, uma 'Deseja iniciar a trajetória? (y/n):', caso sim, ele vai perguntar qual coordenada você deseja ir e a outra se vai existir alguma angulação, digitando esse dados, ele vai primeiramente girar (se o valor for diferente de 0) e depois percorrer a trajetória desejada, mas caso não, o ciclo se fecha, ele não se move em nenhum eixo, e depois pergunta novamente se deseja ir para alguma trajetória.
Esse valores serão guardados em uma array global, e conforme o programa percorre, ele sempre verifica o tamanho da lista, quando ela chegar no fim, o valor do index vai ser retornado a 0. O programa tambem tem uma tolerância de acerto, já que na realidade o robô nunca vai conseguir acertar a posição exata, em essa tolerância ajuda ele a trabalhar com uma melhor eficiência.
No final, na tela ele printa os valores da coordenada atual e os valores da da trajetória que ainda falta.

Após compilar, rodamos o código com o seguinte comando:
<b>ros2 run pacote_kil turtle</b>

*Nota: Este comando é prioritário, para conseguir rodar em outros ambientes, é necessário seguir os tutoriais indicados no inicio desse tópico.

Logo abaixo segue o link para conferir o funcionamento da atividade.
https://drive.google.com/file/d/1ahf4PzQbdIrR_YYBxv602Qay3wbCXSs5/view?usp=sharing


## Referências

TEIXEIRA. Kil Matheus Gomes. Robô Digital. Repositório Github. Disponível em: [[https://github.com/Kil-Matheus/Simulacao-robo-movel---Gazebo](https://github.com/Kil-Matheus/Simulacao-robo-movel---Gazebo). Acesso em: 16 maio. 2023.

NICOLA,  Rodrigo Mangoni (2023). Encontro 01 - Introdução à robótica móvel.pdf . Instituto de Tecnologia e Liderança - INTELI. Disponível em: https://github.com/Murilo-ZC/Questoes-Trabalhos-Inteli-M6/tree/main/ponderada2. Acesso em: 16 maio 2023. 

CARAZZATO, João. Consulta de Material, feito junto com o Rodrigo Mangoni Nicola. Disponível em [https://github.com/joaocarazzato/m6-ec-encontro4-Nicola#implementando-um-subscriber-em-ros](https://github.com/joaocarazzato/m6-ec-encontro4-Nicola#implementando-um-subscriber-em-ros) Acesso em: 16 maio 2023

# Agradecimentos

Agradecimentos especiais a:

 Rodrigo Mangoni Nicola pelo seu grande conhecimento em programação que sempre nos ajuda em todos os desenvolvimentos.

João Carazzato por sua ajuda em conjunto com o Nicola para o desenvolvimento de um material extra.

João Rodrigues por sua ajuda no entendimento do funcionamento dos nós no código.