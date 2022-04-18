"""
Protein Sequencing Project
Name:
Roll Number:
"""

from tkinter import Label
import hw6_protein_tests as test

project = "Protein" # don't edit this

### WEEK 1 ###

'''
readFile(filename)
#1 [Check6-1]
Parameters: str
Returns: str
'''
def readFile(filename):
    text = open(filename, "r")
    out_line = ""
    for readline in text:
        line_strip = readline.rstrip('\n')
        out_line += line_strip
    #print(len(out_line))
    return out_line


'''
dnaToRna(dna, startIndex)
#2 [Check6-1]
Parameters: str ; int
Returns: list of strs
'''
def dnaToRna(dna, startIndex):
    lst= []
    for i in range(startIndex,len(dna),3):
        lst.append(dna[i:i+3])
        if dna[i:i+3]== "TAA" or dna[i:i+3]== "TAG" or dna[i:i+3]== "TGA":
            break
    #print(lst)
    out = [string.replace("T","U") for string in lst]
    #print(out)
    return out


'''
makeCodonDictionary(filename)
#3 [Check6-1]
Parameters: str
Returns: dict mapping strs to strs
'''
def makeCodonDictionary(filename):
    import json
    f = open('data\codon_table.json')
    dict = json.load(f)
    #print(dict)
    dict1 = {}
    for key, value in dict.items():
        for val in value:
            val = val.replace('T','U')
            #print(val)
            dict1[val] = key
    #print(dict1)
    return dict1


'''
generateProtein(codons, codonD)
#4 [Check6-1]
Parameters: list of strs ; dict mapping strs to strs
Returns: list of strs
'''
def generateProtein(codons, codonD):
    #print(codons)
    #print(codonD)
    le = len(codons)
    '''if codons[0] == "AUG" and codons[le] == "UAA":
        codons[0]'''
    for key, value in codonD.items():
            for i in range(0,le):
                codons[0] = "Start"
                if key == codons[i]:
                    codons[i] = value
    #print(codons)
    return codons


'''
synthesizeProteins(dnaFilename, codonFilename)
#5 [Check6-1]
Parameters: str ; str
Returns: 2D list of strs
'''
def synthesizeProteins(dnaFilename, codonFilename):
    count = 0 
    dna = readFile(dnaFilename) 
    d = makeCodonDictionary(codonFilename) 
    lst = []
    i = 0
    while i<(len(dna)): 
        #print(dna[i:i+3])
        if dna[i:i+3] == 'ATG': 
            rna = dnaToRna(dna, i) 
            protein = generateProtein(rna, d)
            lst.append(protein)
            i += 3*len(rna)
        else:
            i += 1
            count += 1
    #print(lst, count) 
    return lst


def runWeek1():
    print("Human DNA")
    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    print("Elephant DNA")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")


### WEEK 2 ###

'''
commonProteins(proteinList1, proteinList2)
#1 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs
Returns: 2D list of strs
'''
def commonProteins(proteinList1, proteinList2):
    lst = []
    len1 = len(proteinList1)
    len2 = len(proteinList2)
    if len1 > len2:
        for i in range(len1):
            if proteinList1[i] in proteinList2:
                if proteinList1[i] not in lst:
                    lst.append(proteinList1[i])
    if len2 > len1:
        for i in range(len2):
            if proteinList2[i] in proteinList1:
                if proteinList2[i] not in lst:
                    lst.append(proteinList2[i])
    #print(lst)
    return lst


'''
combineProteins(proteinList)
#2 [Check6-2]
Parameters: 2D list of strs
Returns: list of strs
'''
def combineProteins(proteinList):
    return


'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
def aminoAcidDictionary(aaList):
    return


'''
findAminoAcidDifferences(proteinList1, proteinList2, cutoff)
#4 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs ; float
Returns: 2D list of values
'''
def findAminoAcidDifferences(proteinList1, proteinList2, cutoff):
    return


'''
displayTextResults(commonalities, differences)
#5 [Check6-2]
Parameters: 2D list of strs ; 2D list of values
Returns: None
'''
import math
def displayTextResults(commonalities, differences):
    return


def runWeek2():
    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")

    commonalities = commonProteins(humanProteins, elephantProteins)
    differences = findAminoAcidDifferences(humanProteins, elephantProteins, 0.005)
    displayTextResults(commonalities, differences)


### WEEK 3 ###

'''
makeAminoAcidLabels(proteinList1, proteinList2)
#2 [Hw6]
Parameters: 2D list of strs ; 2D list of strs
Returns: list of strs
'''
def makeAminoAcidLabels(proteinList1, proteinList2):
    return


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):
    return


'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''
def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    return


'''
makeEdgeList(labels, biggestDiffs)
#5 [Hw6]
Parameters: list of strs ; 2D list of values
Returns: list of strs
'''
def makeEdgeList(labels, biggestDiffs):
    return


'''
runFullProgram()
#6 [Hw6]
Parameters: no parameters
Returns: None
'''
def runFullProgram():
    return


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    '''print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    runWeek1()'''
    test.testReadFile()
    test.testDnaToRna()
    test.testMakeCodonDictionary()
    test.testGenerateProtein()
    test.testSynthesizeProteins()

    ## Uncomment these for Week 2 ##
    
    '''print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    runWeek2()'''
    test.testCommonProteins()
    ## Uncomment these for Week 3 ##
    
    '''print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    runFullProgram()'''
