import random
import sys

print("*"*33)
print("*" + " "*3 + "Aide le Président Manchot" + " "*3 + "*")  # Change the Title Place Holder
print("*"*33)

INTRODUCTION = "BEEP, BEEP, BEEP,\n" \
               "La fusée du Président Manchot est à court de puissance et atterrit sur la terre.\n"\
               "Votre mission est d'aider le Président Manchot à recharger la fusée et à le ramener à Pluton.\n"\
               "Trouver le bon mot avec les lettres données pour recharger la fusée.\n"\


print(INTRODUCTION)
name = ''
yes_no = input("Es-tu prêt? [OUI] [NON] \n")

if yes_no.lower() == 'non':
    print("Plus tard")
    sys.exit()
else:
    name = input("Ton nom est: ")
    print(f'{name.title()}, allons-y \n')


#word lists
list1 = ["el", "menrtso", "démliela", "ej", "neesids", "neubr", "buae", "rgdna", "ndro"]
list1_ans=["le", "monstre", "médaille", "je", "dessine", "brune", "beau", "grand", "rond"]
list2 = ["ste", "slleeb", "esllfi", "mse", "nsagder", "lslbei", "eosdrn", "istptee", "csnttneeo"]
list2_ans = ["tes", "belles", "filles", "mes", "grandes", "billes", "rondes", "petites", "contentes"]
list3 = ["ej", "fsia", "ud", "uedx", "olév", "nso", "ia", "tfia", "seisdn", "srito", "seisdsn", "olsév"]
list3_ans = ["je", "fais", "du", "deux", "vélo", "son", "ai", "fait", "dessin", "trois", "dessins", "vélos"]
list4 = ["eima", "nmo", "iaem", "samei", "olcée", "ima", "éovl", "scléoe", "sle", "dnsa"]
list4_ans = ["aime", "mon", "aime", "amies", "école", "ami", "vélo", "écoles", "les", "dans"]
list5 = ["slleeb", "nto", "agdnre", "samei", "npiee", "ia", "csnttneeo", "esllfi", "eosdrn", "istptee"]
list5_ans=["belles", "ton", "grande", "amies", "peine", "ai", "contentes", "filles", "drones", "petites"]
list6 = ["li", "atif", "ruaste", "sçlneo", "csa", "sersgo", "thaetc", "sse", "çrnaog", "duhac", "auetab"]
list6_ans=["il", "fait", "sauter", "leçons", "sac", "groses", "chatte", "ses", "garçon", "chaud", "bateau"]


pick_a_list = random.randint(1, 6)
all_word_list = (list1, list2, list3, list4, list5, list6)
all_word_list_ans = (list1_ans, list2_ans, list3_ans, list4_ans, list5_ans, list6_ans)
selected_list = all_word_list[pick_a_list-1]
random.shuffle(selected_list)
selected_list_ans = all_word_list_ans[pick_a_list-1]

scores = 0


def check_answer(answer):
    global scores
    if answer in selected_list_ans:
        scores += 1
    elif answer not in selected_list_ans and scores == 0:
        scores = 0
    else:
        scores -= 1


def rocket_power():
    full_power = len(selected_list)
    each_ans = 100 / full_power
    current_power = scores * each_ans
    print(f'{int(current_power)}%')
    #print(scores)


def rocket_final_check():
    global scores
    try:
        if scores >= 7:
            print("Rocket est prêt.\nMission accomplie")
            print(f'Président Manchot: Mercie beaucoup pour votre aide {name.title()}\nAu revoir')
        else:
            print("La fusée a besoin de plus de puissance")
            print(f'Président Manchot: Ne quittez pas {name.title()}, réessayez plus tard')
    except ZeroDivisionError:
        print("La fusée a besoin de plus de puissance")


for words in selected_list:
    print(words)
    ans = input("Le bon mot est: ")
    check_answer(ans)
    rocket_power()

rocket_final_check()


#print(pick_a_list)
#print(selected_list)
#print(list1, list2, list3, list4, list5, list6)
#print(list1_ans, list2_ans, list3_ans, list4_ans, list5_ans, list6_ans)