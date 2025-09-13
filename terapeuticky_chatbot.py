import random

slovnik_reakci = { 
	1:"Pověz mi o tom více...",
	2:"Co tím přesně myslíš?",
	3:"Je tu ještě něco co máš na srdci?",
	4:"Opravdu?",
	5:"Jaký je tvůj názor?",
	6:"Chtěl by si mi ještě něco sdělit?"
}
slovnik_akci = {
	1:"Co tě sem dnes přivádí?",
	2:"Co tě trápí?",
	3:"Co máš a srdci?"
	}


def uvitani():
	nahodna_akce = random.randint(1, len(slovnik_akci))

	uvitaci_hlaska = "Ahoj jsem tvůj terapeutický chatbot. Budu se tě ptát na otázky. Když už nebudeš chtít pokračovat, napiš N.\n"

	vyzva =(slovnik_akci[nahodna_akce])
	print(uvitaci_hlaska)
	print(vyzva)	





def ptat_se():
	nahodna_odpoved = random.randint(1, len(slovnik_reakci))
	odpoved = input()
	if odpoved == "N":	
		print("Díky za pokec")
		return 0
	else:
		print(slovnik_reakci[nahodna_odpoved])
	ptat_se()


uvitani()
ptat_se()

		
		



		

