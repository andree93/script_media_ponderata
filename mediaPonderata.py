import csv

def readFromFile(filename):

    with open(filename) as f:
        csvreader = csv.reader(f)
        array_dati = [ row for row in csvreader ]
    return array_dati


def calcoloMedia():

    righe_csv = readFromFile("voti.csv")
    sommaVoti = 0
    sommaCFU = 0
    numeroVoti = 0
    sommaProdottiVotoCfu = 0


    for riga in righe_csv:
        esame = riga[0]
        voto = int(riga[1])
        CFU = int(riga[2])
        
        sommaVoti += voto
        sommaCFU  += CFU
        numeroVoti += 1
        sommaProdottiVotoCfu = sommaProdottiVotoCfu + (voto*CFU)

        print(f'Esame: {esame} - voto:  {voto} - CFU: {CFU}')

    mediaAritmetica = sommaVoti / numeroVoti
    mediaPonderata = sommaProdottiVotoCfu / sommaCFU


    print(f"La media aritmetica è {mediaAritmetica}\n")
    print(f"La media  ponderata è {mediaPonderata}")
    

if __name__ == "__main__":
    calcoloMedia()
    