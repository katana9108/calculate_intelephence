print('Bienvenue sur votre calculatrice intelligente'.upper())
pseudo = input("Laissez moi mettre un pseudo sur votre visage \u2764 ?: ")
print("multplication : (m), addition : (a), soustraction : (s), division : (d)")
response = input(f"Que voulez vous faire comme calcul {pseudo} ? :".capitalize())
end= False


def multiply():
    a = int(input("Entrez le prmeier nombre : ".capitalize()))
    b = int(input("Entrez le second nombre : ".capitalize()))
    print(f"Les réusltat de la mutiplication de {a} avec {b}  est : {a*b} {pseudo} \u2764 ")

def addition():
    a = int(input("Entrez le premier Nombre : ".capitalize()))
    b = int(input("Entrez le second nombre : ".capitalize()))
    print(f"Le résultat de la somme entre {a} avec {b} est : {a+b} {pseudo} \u2764 ")

def division():
    a= int(input("Entrez le premier nombre : ".capitalize()))
    b= int(input("Entrez le second nombre : ".capitalize()))
    print(f"Le résultat de la division entre {a} avec {b} est : {a//b} {pseudo} \u2764 ")

def soustraction():
    a=int(input("Entrez le premier nombre : ".capitalize()))
    b=int(input("Entrez le second nombre : ".capitalize()))
    print(f"Le résultat de la soustraction entre {a} avec {b} est : {a-b} {pseudo} \u2764 ")



if response=="m":
    multiply()
elif response=="a":
    addition()
elif response=="s":
    soustraction()
elif response=="d":
    division()
else:
    print("réponse non valide !".capitalize())
    end= True
