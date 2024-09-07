## Python + Firabase
## Estudo de Python criando um script para o jogo Ravendawn
  Este projeto contém um conjunto de códigos relacionados à estudar
  python voltado a desenvolver um script com pequenas funcionalidades
  reconhecendo conteúdos do sistema e da tela para total funcionamento.

# Tecnologias utilizadas
  - Python;
  - Firebase

# Bibliotecas python utilizadas
  - Win32gui;
  - PyAutoGui;
  - Asyncio;
  - Keybord;
  - Pyrebase;
  - Sys;
  - Pyperclip
  - Tkinter

**Observação**: Neste README não estão detalhados os módlos e códigos em questão.
Somente será explicado e demonstrado o software em si e suas funcionalidades.

## Tela inicial
![](https://i.imgur.com/JmAfPzM.png)

Nesta tela será feito a autenticação da conta referente ao banco de dados em nuvem do
Firebase. A criação de conta não seria disponível devido ao "Admin" ser o responsável pelo
controle das mesmas. Quando o admin fornecer os dados para efetuar a autenticação, 
a mesma estará disponível.

## Tela principal do software
![](https://i.imgur.com/kWKRWGJ.png)

Ao efetuar login, está tela será carregada sendo a principal do sistema, onde o mesmo se comporta
em formato asincrono, para ser responsivo a medida da necessidade do momento do usuário.
O campo "Nome do personagem" deve ser exatamente igual ao usuário em jogo devido ao mesmo ser 
responsável por localizar a aplicação em execução no windows.
Após o mesmo ser reconhecido, o Status de "Não reconhecido" será atualizado para "Reconhecido"
como demonstrado na imagem abaixo.

![](https://i.imgur.com/Vv7iJwl.png)

O radiobutton possui algumas opções. Cada uma responsável por alguma atividade funcional do software.
Independente de ser selecionada ou não, só será efetivada caso seja clicado "F1" no teclado, como também
"F2" para pausar a execução de determinada funcionalidade, além de "F3" para sair do software.
Caso alguma funcionalidade do radiobutton seja selecionada, sendo diferente da de index 0 ("Nada"), então
o status será novamente atualizado sinalizando a funcionalidade em execução, como demonstrado na imagem 
abaixo.

![](https://i.imgur.com/NUyVZHM.png)

Caso seja executada uma funcionalidade diferente do ineex 0 ("Nada") e a mesma seja pausada (utilizando "F2"),
então o status será atualizado para "Interrompido" conforme a imagem abaixo.

![](https://i.imgur.com/G5j04bA.png)

Para elucidar, segue uma breve explicação de cada funcionalidade:
- "Nada": Não possui funcionalidade, sendo o ponto neutro do sistema;
- "Auto Walk": Capta a última direção utilizada pelo usuário, e executa ela continuamente;
- "Auto Craft": Localiza/Reconhece posições específicas na tela para realizar a execução intermitente de
                "crafts" no jogo;
- "Auto Chat": Ele realiza um Spam de mensagens na caixa de mensagens no jogo, no que seria voltado mais para
               o mercado do jogo.

Para a funcionalidade de "Auto Chat", será aberta uma modal com uma solicitação de input de texto onde a mesma
serve para "salvar" o texto emitido automaticamente pelo usuário, como demonstrado na imagem abaixo.

![](https://i.imgur.com/IRPJFgn.png)


Segue abaixo um vídeo de demonstração do mesmo:
https://www.youtube.com/watch?v=NxjWqfrR24E



**OBS** Este script foi criado com o intuito de automatizar atividades pessoais básicas e no formato de estudo.
