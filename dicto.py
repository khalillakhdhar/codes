p1={"nom":"Lakhdhar", "prenom":"Khalil", "age":33,"profession":"enseignant"}
p2={"nom":"Lakhdhar", "prenom":"Adel", "age":40,"profession":"médecin"}
print(p1)
personnes=[]
personnes.append(p1)
personnes.append(p2)
for p in personnes:
    print(p["profession"])