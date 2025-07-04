# Given a set of motifs, create a consensus motif using a profile array
# A profile array is an array that keeps track of how many times each base occurs in each position
# The most probable bases in each position can be combined to create the consensus strand

from numpy import transpose

# Creates a profile array from the motifs
def profile(motifs):
    tMotifs = []
    for column in transpose(motifs):
        tMotifs.append(list(column))
    k = len(tMotifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(k):
        for r in tMotifs:
            if r[i] == "A":
                A[i] += 1
            elif r[i] == "C":
                C[i] += 1
            elif r[i] == "G":
                G[i] += 1
            elif r[i] == "T":
                T[i] += 1
    return [A, C, G, T]


# Constructs the consensus strand from the profile array generated earlier
def consensus(profile_arr):
    cons = ""
    prof = transpose(profile_arr)
    for i in prof:
        m = list(i).index(max(i))
        match m:
            case 0:
                cons += "A"
            case 1:
                cons += "C"
            case 2:
                cons += "G"
            case 3:
                cons += "T"
    return cons


# Formats the output for the Rosalind grader
def formatOutput(cons: str, prof: list[list[int]]) -> str:
    s = cons
    nuc = "ACGT"
    for r in range(4):
        temp = []
        s += "\n"
        s += nuc[r] + ": "
        for i in prof[r]:
            temp.append(str(i))
        s += " ".join(temp)
    return s


# Parses the input, provided in FASTA format
def parseInput(file):
    d = list()
    temp = ""
    for line_s in file:
        line = line_s.strip()
        if line.isspace():
            continue
        elif line.startswith(">"):
            if len(temp) == 0:
                pass
            else:
                d.append(temp)
                temp = ""
        else:
            temp += line.strip()
    d.append(temp)
    return d
