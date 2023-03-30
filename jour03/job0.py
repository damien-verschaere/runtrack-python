phrase = input("Entrez une phrase: ")
virgule= phrase+","
ecriture=open("output.txt","a")
ecriture.write(virgule)
ecriture.close()