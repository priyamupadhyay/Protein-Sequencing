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
    lst = []
    for i in range(len(proteinList)):
        for j in range(len(proteinList[i])):
            lst.append(proteinList[i][j])
    #print(lst)
    return lst


'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
def aminoAcidDictionary(aaList):
    dict = {}
    for item in aaList:
        if (item in dict):
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


'''
findAminoAcidDifferences(proteinList1, proteinList2, cutoff)
#4 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs ; float
Returns: 2D list of values
'''
def findAminoAcidDifferences(proteinList1, proteinList2, cutoff):
    d = []
    dict1, dict2 = aminoAcidDictionary(combineProteins(proteinList1)), aminoAcidDictionary(combineProteins(proteinList2))
    for i,j in dict1.items():
        dict1[i] = j/len(combineProteins(proteinList1))
        if i not in dict2:
            dict2[i] = 0
    for i,j in dict2.items():
        dict2[i] = j/len(combineProteins(proteinList2))
        if i not in dict1:
            dict1[i] = 0
        if abs(dict1[i] - dict2[i]) > cutoff:
            if i != 'Start' and i != 'Stop':
                d.append([i, dict1[i], dict2[i]])
    return d


'''
displayTextResults(commonalities, differences)
#5 [Check6-2]
Parameters: 2D list of strs ; 2D list of values
Returns: None
'''
import math
def displayTextResults(commonalities, differences):
    lst = sorted(commonalities)
    print("The following proteins occurred in both DNA Sequences:")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == "Start" or lst[i][j] == "Stop":
                continue
            print(lst[i][j], end=' ')
            #lst.append(commonalities[i][j] + ' ')
        print()
    #lst.sort()
    print("The following amino acids occurred at very different rates in the two DNA sequences:")
    for i in sorted(differences):
        #print(i[0],": ",math.ceil(i[1]*100)," in Seq1",math.ceil(i[2]*100)," in Seq2")
        print(i[0],": ",round(i[1]*100, 2),"% in Seq1,",round(i[2]*100, 2),"% in Seq2")
        #for j in range(len(differences[i])):
        print()
    #print(differences)
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
    lst = combineProteins(proteinList1)
    lst1 = combineProteins(proteinList2)
    lst2 = []
    for i in range(len(lst)):
        if lst[i] not in lst2:
            lst2.append(lst[i])
    for i in range(len(lst1)):
        if lst1[i] not in lst2:
            lst2.append(lst1[i])
    out = sorted(lst2)
    #print(out)
    return out


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):
    lst = combineProteins(proteinList)
    dict = aminoAcidDictionary(lst)
    out = []
    for i in labels:
        if i in dict:
            freq = dict[i]/len(lst)
            out.append(freq)
        else:
            out.append(0)
    #print(out)
    return out


'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''
def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    w = 0.35
    plt.bar(xLabels, freqList1, width = -w, align="edge", label = label1, edgecolor = edgeList)
    plt.bar(xLabels, freqList2, width = w, align="edge", label = label2, edgecolor = edgeList)
    plt.xticks(rotation = "vertical")
    plt.legend()
    plt.show()
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
    '''test.testReadFile()
    test.testDnaToRna()
    test.testMakeCodonDictionary()
    test.testGenerateProtein()
    test.testSynthesizeProteins()'''

    ## Uncomment these for Week 2 ##
    
    '''print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    runWeek2()'''
    '''test.testCommonProteins()
    test.testCombineProteins()
    test.testAminoAcidDictionary()
    test.testFindAminoAcidDifferences()'''
    ## Uncomment these for Week 3 ##
    
    print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    runFullProgram()
