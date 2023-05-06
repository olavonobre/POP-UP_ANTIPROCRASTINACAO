import tkinter as tk
import time
import random

frases = [
    "A procrastinação é o ladrão do tempo.",
    "Não adie para amanhã o que você pode fazer hoje.",
    "Lembre-se: hoje é o amanhã que você tanto temeu ontem.",
    "Aja agora e não se arrependa depois."
    "O sucesso é construído com pequenos passos, não com grandes decisões.",
    "Você não precisa ser perfeito, apenas precisa começar.",
    "A única maneira de fazer um ótimo trabalho é amar o que você faz.",
    "Você é o único obstáculo entre você e seus sonhos.",
    "Enfrente suas tarefas de frente e veja as suas conquistas.",
    "Não deixe o seu medo de falhar impedi-lo de agir.",
    "Mantenha a motivação e o positivismo todos os dias.",
    "A chave do sucesso está em fazer escolhas melhores todos os dias.",
    "A maior conquista é a conquista de si mesmo.",
    "Todas as grandes coisas começam com uma única ação.",
    "Não há momento como o presente para começar.",
    "A persistência é a chave para o sucesso.",
    "Todo grande sucesso começa com pequenos passos.",
    "Aproveitar o agora é a melhor coisa para o seu futuro.",
    "A ação é o antídoto para o medo.",
    "Não espere o momento perfeito, faça o momento agora.",
    "Seja fiel a seu compromisso consigo mesmo.",
    "Não espere que outros o motivem - é você quem deve se motivar.",
    "Nada é impossível se você estiver disposto a trabalhar por isso.",
    "Não abra mão dos seus sonhos só porque leva tempo para realizá-los.",
    "Faça hoje o que você vai se orgulhar amanhã.",
    "Nunca pare de crescer! Nunca pare de agir!",
    "O momento certo para agir é o agora.",
    "O único dia que você não pode mudar é o ontem.",
    "Não lamente pelo que não pode fazer, concentre-se no que pode fazer.",
    "Você está um passo a mais perto do sucesso a cada ação que toma.",

]
frases_aleatorias = random.choices(frases)
# print(frase_aleatoria)
def programafinalizado():
    janela = tk.Tk()
    fonte = ("Arial", 16)
    programa = tk.Label(janela, text=frases_aleatorias, font=fonte)
    janela.after(5000, janela.destroy)
    programa.pack()
    janela.mainloop()

while True: 
    programafinalizado()
    time.sleep(10)

