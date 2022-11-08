texto = """
O que é python e como começar nessa linguagem!
PAULO SILVEIRA:
Python é uma linguagem de programação cada vez mais na moda e não é de agora, né, Guilherme?

GUILHERME SILVEIRA:
É, já tem alguns anos que vem crescendo a adoção de python no mercado e, o que é muito legal também, é que antes da gente utilizar no mercado, é muito fácil de você utilizar dentro de casa em coisas suas do dia a dia, para se acostumar, caso você ainda não esteja programando.

PAULO SILVEIRA:
Pois é, porque muita gente vai para o python por causa da web e os frameworks famosos da web como Django ou Flask, ou por causa do Data Science, por causa do socket learning, ou panda ou numpy. Mas se você está interessado no Python, a grande sacada é que pode usar como uma linguagem de script e aprender de uma maneira muito mais tranquila, ao invés de já cair nesse mundo de um monte de bibliotecas.

Em vez de você cair no Python já com essas bibliotecas pesadas e super interessantes que podem assustar um pouco no começo, você pode usar ele para trabalhar em casa, com scripts, não é mesmo? Para resolver alguns problemas pequenininhos de arquivo. É muito bacana mesmo!

GUILHERME SILVEIRA:
Claro, o exemplo clássico é: você tem vários arquivos num diretório e precisa fazer algumas coisas com eles. Você tem várias fotos, vários arquivos, por qualquer motivo e, não só quer mover eles, mas renomear todos e fazer alguma tarefa com as imagens.

Então é super fácil fazer esse tipo de trabalho com python. Vai acabar utilizando alguma biblioteca, vai utilizar o pillow, por exemplo, para trabalhar com edição de imagem, reduzir ela, mas é super simples, sabe? Para cada arquivo dentro de um diretório, abre a imagem, refaz o resize, salva o arquivo, acabou. 5 ou 6 linhas de código você tem isso feito para você. É muito fácil de começar a automatizar certas tarefas que precisa no dia a dia.

PAULO SILVEIRA:
Então, se você está sempre usando Node JS ou JavaScript para esses scripts, tem a oportunidade de começar com Python e aprender essa linguagem que realmente nasceu no século passado, no milênio passado e que tem ganhado muita adoção.
"""

from collections import Counter

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    print(total_de_caracteres)

    proporcoes = [(letra, frequencia/total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao*100))

analisa_frequencia_de_letras(texto)