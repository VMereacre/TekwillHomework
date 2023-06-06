"""
Nota trecătoare la un test.
Presupunem că pentru a avea o notă trecătoare la un test,
elevii trebuie să obţină minim 15 puncte.
Scrieţi un program care citeşte de la tastatură punctajul obţinut de un elev şi
afişează dacă elevul are o notă trecătoare sau va trebui să mai susţină încă o dată testul.
"""
nota = int(input("Introduce punctajul obtinut la test : "))
if nota >= 15:
    print("Felicitari! Ai nota trecatoare.")
else:
    print("Ne pare rau, va trebui sa mai sustii inca o data testul.")