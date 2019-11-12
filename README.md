# Dog_Hero
Projeto dedicado ao processo seletivo da Dog Hero para Summer Job.
O objetivo desse projeto é fazer o ranqueamento de anfitrões da plataforma, tentando estimar a probabilidade dele fechar uma reserva.

A ideia desse projeto é particularmente bem simples, contabilizar as probabilidades de fechar uma reserva a partir dos dados dos anfitriões, por exemplo, qual a probabilidade de fechar uma reserva tendo um espaço pequeno, qual a probabilidade de eu fechar uma reserva cobrando 35$ a noite. Depois de feito esse mapeamento, os anfitriões entrarão com seus dados na plataforma e serão ranqueados a partir da soma das probabilidades do mapeamento, caso o anfitrião possua algum atributo não mapeado, ele busca o atribuito mais próximo e assume esse valor. Quando ele conseguir ou não fechar uma reserva ele pode retroalimentar o modelo.

Esse modelo parece bem promissor pois a base de dados disponibilizada tem alta relevância estatística, além disso, o modelo é atualizado constantemente, ou seja, ele consegue absorver mais dados e ao longo do tempo se modificar o rumo que os dados estão tomando.

Antes dessa ideia foi testado a solução usando redes neurais, porém o tempo que ela gasta é muito alto devido a quantidade de dados então parece ser impraticável na vida real por conta das várias atualizações que a plataforma sofre e a necessidade de uma busca rápida e dinâmica. Inclusive o código toy dela está nesse mesmo repositório, inclusive rodando, porém por conta do tempo, não insisti nessa alternativa por medo de não dar resultados frutíferos.

Infelizmente a estratégia proposta também não deu resultados frutíferos. Mas a próxima etapa depois de classificar os anfitriões pela avaliação proposta era ordenar todos eles por essa nota, em caso de empate desempatar com o maior valor que foi somado na nota.

Estão disponibilizados o rascunho do código que é o lendo dados que demora cerca de 2 horas para executar em um computador i5 com 4 gb de RAM, ubuntu 16.04, python 3.

Para testar o programa apenas baixe esse repositório e execute pyhton3 lendo_dados.py na linha de comando dentro da pasta raiz.
A próxima etapa seria se o arquivo de saída estivesse completo, ordenar ele com o programa merge.py que é uma implementação do merge sort e exibir o ranking dos melhores anfitrões.
