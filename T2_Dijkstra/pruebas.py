from grafo import Grafo, Arista
import timeit
import json

#Ejemplos de aristas de grafo
aristas_ejemplo = set([
    Arista(('A', 'B'), 1),
    Arista(('A', 'D'), 3),
    Arista(('A', 'C'), 2),
    Arista(('B', 'C'), 4),
    Arista(('C', 'D'), 5),
])

aristas_g1 = [
    Arista(("A","B"),2),
    Arista(("A","C"),4),
    Arista(("A","D"),1),
    Arista(("B","D"),3),
    Arista(("B","E"),1),
    Arista(("B","F"),7),
    Arista(("C","E"),5),
    Arista(("C","G"),2),
    Arista(("C","H"),3),
    Arista(("D","F"),5),
    Arista(("D","H"),6),
    Arista(("E","G"),2),
    Arista(("E","I"),4),
    Arista(("F","J"),7),
    Arista(("F","K"),8),
    Arista(("G","L"),1),
    Arista(("G","M"),3),
    Arista(("H","I"),2),
    Arista(("H","N"),6),
    Arista(("I","J"),3),
    Arista(("I","O"),4),
    Arista(("J","K"),1),
    Arista(("J","P"),6),
    Arista(("K","Q"),4),
    Arista(("K","R"),3),
    Arista(("L","S"),6),
    Arista(("L","T"),7),
    Arista(("M","U"),1),
    Arista(("M","V"),4),
    Arista(("N","O"),2),
    Arista(("N","W"),4),
    Arista(("O","P"),1),
    Arista(("O","X"),5),
    Arista(("P","Q"),3),
    Arista(("P","Y"),2),
    Arista(("Q","Z"),6),
    Arista(("Q","A1"),2),
    Arista(("R","B1"),4),
    Arista(("R","C1"),5),
    Arista(("S","D1"),6),
    Arista(("S","E1"),7),
    Arista(("T","F1"),2),
    Arista(("T","G1"),3),
    Arista(("U","H1"),5),
    Arista(("U","I1"),2),
    Arista(("V","J1"),3),
    Arista(("V","K1"),5),
    Arista(("W","L1"),6),
    Arista(("W","M1"),1),
    Arista(("X","N1"),2),
    Arista(("X","O1"),4),
    Arista(("Y","P1"),7),
    Arista(("Y","Q1"),6),
    Arista(("Z","R1"),3),
    Arista(("Z","S1"),2),
]
aristas_g2 = [
    Arista(("A","C"),7),
    Arista(("B","D"),8),
    Arista(("C","E"),6),
    Arista(("D","E"),2),
    Arista(("D","F"),4),
    Arista(("D","G"),10),
    Arista(("D","H"),12),
    Arista(("E","I"),4),
    Arista(("E","J"),7),
    Arista(("F","K"),3),
    Arista(("F","L"),6),
    Arista(("F","M"),8),
    Arista(("G","N"),9),
    Arista(("H","O"),11),
    Arista(("I","P"),2),
    Arista(("I","Q"),9),
    Arista(("I","R"),12),
    Arista(("J","S"),8),
    Arista(("J","T"),13),
    Arista(("J","U"),15),
    Arista(("K","V"),4),
    Arista(("K","W"),11),
    Arista(("K","X"),14),
    Arista(("L","Y"),3),
    Arista(("L","Z"),8),
    Arista(("L","AA"),11),
    Arista(("M","AB"),7),
    Arista(("M","AC"),11),
    Arista(("M","AD"),14),
    Arista(("N","AE"),12),
    Arista(("N","AF"),16),
    Arista(("N","AG"),18),
    Arista(("O","AH"),13),
    Arista(("O","AI"),15),
    Arista(("O","AJ"),19),
    Arista(("P","AK"),5),
    Arista(("P","AL"),8),
    Arista(("P","AM"),12),
    Arista(("Q","AN"),11),
    Arista(("Q","AO"),13),
    Arista(("Q","AP"),16),
    Arista(("R","AQ"),15),
    Arista(("R","AR"),17),
    Arista(("R","AS"),20),
    Arista(("S","AT"),9),
    Arista(("S","AU"),12),
    Arista(("S","AV"),16),
    Arista(("T","AW"),18),
    Arista(("T","AX"),20),
    Arista(("T","AY"),22),
    Arista(("U","AZ"),13),
    Arista(("U","BA"),15),
    Arista(("U","BB"),18),
    Arista(("V","BC"),11),
    Arista(("V","BD"),13),
    Arista(("V","BE"),15),
    Arista(("W","BF"),17),
    Arista(("W","BG"),19),
    Arista(("W","BH"),22),
    Arista(("X","BI"),14),
    Arista(("X","BJ"),16),
    Arista(("X","BK"),19),
    Arista(("Y","BL"),12),
    Arista(("Y","BM"),15),
    Arista(("Y","BN"),18),
    Arista(("Z","BO"),13),
    Arista(("Z","BP"),16),
    Arista(("Z","BQ"),20),
    Arista(("AA","BR"),11),
    Arista(("AA","BS"),14),
    Arista(("AB","BT"),13),
    Arista(("AB","BU"),15),
    Arista(("AB","BV"),18),
    Arista(("AC","BW"),19),
    Arista(("AC","BX"),22),
    Arista(("AC","BY"),25),
    Arista(("AD","BZ"),20),
    Arista(("AD","CA"),23),
    Arista(("AD","CB"),26),
    Arista(("AE","CC"),17),
    Arista(("AE","CD"),20),
    Arista(("AE","CE"),22),
    Arista(("AF","CF"),15),
    Arista(("AF","CG"),18),
    Arista(("AF","CH"),21),
    Arista(("AG","CI"),14),
    Arista(("AG","CJ"),17),
    Arista(("AG","CK"),20),
    Arista(("AH","CL"),13),
    Arista(("AH","CM"),16),
    Arista(("AH","CN"),19),
    Arista(("AI","CO"),12),
    Arista(("AI","CP"),15),
    Arista(("AI","CQ"),18),
    Arista(("AJ","CR"),11),
    Arista(("AJ","CS"),14),
    Arista(("AJ","CT"),17),
    Arista(("AK","CU"),10),
    Arista(("AK","CV"),13),
    Arista(("AK","CW"),16),
    Arista(("AL","CX"),9),
    Arista(("AL","CY"),12),
    Arista(("AL","CZ"),15),
    Arista(("AM","DA"),8),
    Arista(("AM","DB"),11),
    Arista(("AM","DC"),14),
    Arista(("AN","DD"),7),
    Arista(("AN","DE"),10),
    Arista(("AN","DF"),13),
    Arista(("AO","DG"),6),
    Arista(("AO","DH"),9),
    Arista(("AO","DI"),12),
    Arista(("AP","DJ"),5),
    Arista(("AP","DK"),8),
    Arista(("AP","DL"),11),
    Arista(("AQ","DM"),4),
    Arista(("AQ","DN"),7),
    Arista(("AQ","DO"),10),
    Arista(("AR","DP"),3),
    Arista(("AR","DQ"),6),
    Arista(("AR","DR"),9),
    Arista(("AS","DS"),2),
    Arista(("AS","DT"),5),
    Arista(("AS","DU"),8),
    Arista(("AT","DV"),3),
    Arista(("AT","DW"),6),
    Arista(("AT","DX"),9),
    Arista(("AU","DY"),4),
    Arista(("AU","DZ"),7),
    Arista(("AU","EA"),10),
    Arista(("AV","EB"),5),
    Arista(("AV","EC"),8),
    Arista(("AV","ED"),11),
    Arista(("AW","EE"),6),
    Arista(("AW","EF"),9),
    Arista(("AW","EG"),12),
    Arista(("AX","EH"),7),
    Arista(("AX","EI"),10),
    Arista(("AX","EJ"),13),
    Arista(("AY","EK"),8),
    Arista(("AY","EL"),11),
    Arista(("AY","EM"),14),
    Arista(("AZ","EN"),9),
    Arista(("AZ","EO"),12),
    Arista(("AZ","EP"),15),
    Arista(("BA","EQ"),10)
]
aristas_g3 = [
    Arista(("A","B"),6),
    Arista(("A","C"),9),
    Arista(("B","D"),8),
    Arista(("C","E"),6),
    Arista(("D","E"),2),
    Arista(("D","F"),4),
    Arista(("D","G"),20),
    Arista(("D","H"),12),
    Arista(("E","I"),4),
    Arista(("E","J"),7),
    Arista(("F","K"),8),
    Arista(("F","L"),6),
    Arista(("F","M"),8),
    Arista(("G","N"),9),
    Arista(("H","O"),11),
    Arista(("I","P"),2),
    Arista(("I","Q"),14),
    Arista(("I","R"),12),
    Arista(("J","S"),8),
    Arista(("J","T"),13),
    Arista(("J","U"),15),
    Arista(("K","V"),4),
    Arista(("K","W"),11),
    Arista(("K","X"),14),
    Arista(("L","Y"),3),
    Arista(("L","Z"),8),
    Arista(("L","AA"),11),
    Arista(("M","AB"),7),
    Arista(("M","AC"),11),
    Arista(("M","AD"),14),
    Arista(("N","AE"),12),
    Arista(("N","AF"),16),
    Arista(("N","AG"),18),
    Arista(("O","AH"),13),
    Arista(("O","AI"),15),
    Arista(("O","AJ"),19),
    Arista(("P","AK"),5),
    Arista(("P","AL"),8),
    Arista(("P","AM"),12),
    Arista(("Q","AN"),11),
    Arista(("Q","AO"),13),
    Arista(("Q","AP"),16),
    Arista(("R","AQ"),15),
    Arista(("R","AR"),17),
    Arista(("R","AS"),20),
    Arista(("S","AT"),9),
    Arista(("S","AU"),12),
    Arista(("S","AV"),16),
    Arista(("T","AW"),18),
    Arista(("T","AX"),20),
    Arista(("T","AY"),22),
    Arista(("U","AZ"),13),
    Arista(("U","BA"),15),
    Arista(("U","BB"),18),
    Arista(("V","BC"),11),
    Arista(("V","BD"),13),
    Arista(("V","BE"),15),
    Arista(("W","BF"),17),
    Arista(("W","BG"),19),
    Arista(("W","BH"),22),
    Arista(("X","BI"),14),
    Arista(("X","BJ"),16),
    Arista(("X","BK"),19),
    Arista(("Y","BL"),12),
    Arista(("Y","BM"),15),
    Arista(("Y","BN"),18),
    Arista(("Z","BO"),12),
    Arista(("Z","BP"),16),
    Arista(("Z","BQ"),20),
    Arista(("AA","BR"),11),
    Arista(("AA","BS"),14),
    Arista(("AB","BT"),13),
    Arista(("AB","BU"),15),
    Arista(("AB","BV"),18),
    Arista(("AC","BW"),19),
    Arista(("AC","BX"),22),
    Arista(("AC","BY"),25),
    Arista(("AD","BZ"),20),
    Arista(("AD","CA"),23),
    Arista(("AD","CB"),26),
    Arista(("AE","CC"),17),
    Arista(("AE","CD"),20),
    Arista(("AE","CE"),22),
    Arista(("AF","CF"),15),
    Arista(("AF","CG"),18),
    Arista(("AF","CH"),21),
    Arista(("AG","CI"),14),
    Arista(("AG","CJ"),17),
    Arista(("AG","CK"),20),
    Arista(("AH","CL"),13),
    Arista(("AH","CM"),20),
    Arista(("AH","CN"),19),
    Arista(("AI","CO"),12),
    Arista(("AI","CP"),15),
    Arista(("AI","CQ"),18),
    Arista(("AJ","CR"),11),
    Arista(("AJ","CS"),14),
    Arista(("AJ","CT"),17),
    Arista(("AK","CU"),10),
    Arista(("AK","CV"),13),
    Arista(("AK","CW"),16),
    Arista(("AL","CX"),9),
    Arista(("AL","CY"),12),
    Arista(("AL","CZ"),15),
    Arista(("AM","DA"),8),
    Arista(("AM","DB"),11),
    Arista(("AM","DC"),14),
    Arista(("AN","DD"),7),
    Arista(("AN","DE"),10),
    Arista(("AN","DF"),13),
    Arista(("AO","DG"),6),
    Arista(("AO","DH"),9),
    Arista(("AO","DI"),12),
    Arista(("AP","DJ"),5),
    Arista(("AP","DK"),8),
    Arista(("AP","DL"),11),
    Arista(("AQ","DM"),4),
    Arista(("AQ","DN"),4),
    Arista(("AQ","DO"),10),
    Arista(("AR","DP"),3),
    Arista(("AR","DQ"),6),
    Arista(("AR","DR"),9),
    Arista(("AS","DS"),3),
    Arista(("AS","DT"),5),
    Arista(("AS","DU"),8),
    Arista(("AT","DV"),3),
    Arista(("AT","DW"),6),
    Arista(("AT","DX"),9),
    Arista(("AU","DY"),4),
    Arista(("AU","DZ"),25),
    Arista(("AU","EA"),10),
    Arista(("AV","EB"),5),
    Arista(("AV","EC"),8),
    Arista(("AV","ED"),11),
    Arista(("AW","EE"),6),
    Arista(("AW","EF"),9),
    Arista(("AW","EG"),16),
    Arista(("AX","EH"),7),
    Arista(("AX","EI"),10),
    Arista(("AX","EJ"),13),
    Arista(("AY","EK"),8),
    Arista(("AY","EL"),11),
    Arista(("AY","EM"),14),
    Arista(("AZ","EN"),7),
    Arista(("AZ","EO"),12),
    Arista(("AZ","EP"),1),
    Arista(("BA","EQ"),14),
]

#Crea grafos
lista_grafos = [Grafo(aristas_g1), Grafo(aristas_g2), Grafo(aristas_g3)]
#Mide tiempo de ejecución
tiempo_ejecucion = {}
for i, grafo in enumerate(lista_grafos):
    for nodo in grafo.get_nodos():
        t_0 = timeit.default_timer()
        distancias_a = grafo.dijkstra(nodo)
        t_1 = timeit.default_timer()
        if i not in tiempo_ejecucion:
            tiempo_ejecucion[i] = {}
        tiempo_ejecucion[i][nodo] = round((t_1 - t_0) * 1000, 3)

with open("./T2_Dijkstra/resultados.json", "w") as archivo_registro:
    json.dump(tiempo_ejecucion,archivo_registro,indent=1)
