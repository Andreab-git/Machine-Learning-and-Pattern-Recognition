##################################
#### Created by Andrea Bena' #####
##################################

# The competitors name and surname do not contain spaces
# The total number of record (lines) is not known
# There are always 5 evaluations for every competitor, and these numbers are separated by a space
import sys


class Competitor:
    def __init__(self, name, surname, country, scores):
        self.name = name
        self.surname = surname
        self.country = country
        self.scores = scores
        self.totalScore = sum(float(i) for i in self.scores[1:-1])


if __name__ == '__main__':
    bestCompetitors = []
    hCountryScore = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            name, surname, nationality, *scores = line.strip().split()
            comp = Competitor(name, surname, nationality, scores)
            if comp.country not in hCountryScore.keys():
                hCountryScore[comp.country] = round(comp.totalScore, 2)
            else:
                hCountryScore[comp.country] = hCountryScore[comp.country] + round(comp.totalScore, 2)
            if (x.totalScore < comp.totalScore for x in bestCompetitors):
                bestCompetitors.append(comp)
                bestCompetitors = sorted(bestCompetitors, key=lambda score: score.totalScore)[::-1][0:3]

    print('Final ranking:')
    for index, el in enumerate(bestCompetitors, start=1):
        print(f'{index}: {el.country} {el.name} {el.surname} -- Score: {el.totalScore}')

    print('\nBest Country:')
    bestCountry = max(hCountryScore, key=hCountryScore.get)
    print(f'{bestCountry} Total score: {hCountryScore[bestCountry]}')
