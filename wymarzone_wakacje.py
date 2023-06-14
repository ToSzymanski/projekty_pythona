#treść komunikatówdfs
prompt_wakacje = "Jezeli miałbys odwiedzic jedno miejsce na wakacje, gdzie by to było?"
prompt_name = "Jak masz na imię?"
#utworzenie słownika na odpowiedzi
wyniki_ankiety = {}

#zbieranie odpowiedzi
flag = True
while flag:
    answer_name = input(prompt_name)
    answer_wakacje = input(prompt_wakacje)
    wyniki_ankiety[answer_name] = answer_wakacje

    #ustalenie czy ktoś jeszcze chce wziąć udział w ankiecie
    repeat = input('Czy ktoś jeszcze chce wziąc udział w ankiecie? (TAK/NIE)')
    if repeat == "NIE":
        flag = False

#wyniki ankiety
print("===WYNIKI ANKIETY===")
for answer_name, answer_wakacje in wyniki_ankiety.items():
    print(f'{answer_name} chce jechać na wakacje w {answer_wakacje}')


