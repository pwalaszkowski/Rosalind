#!/usr/bin/python


# Transcribing DNA into RNA
# http://rosalind.info/problems/rna/

def convertDnaToRna(dna_string):
    # New RNA string
    rna_string = ""

    # Iterate over DNA and replace T with U
    for char in dna_string:
        if char == "T":
            rna_string += "U"
        else:
            rna_string += char

    return rna_string


print convertDnaToRna("CCTCCCCTCGAAGTCTGATTGTTTAAGCCAAATGCCTCAGCCAAATTTAGTGTAGGCGAAGGTTTTGAGGGATGTCTCCGAAGGCTGTACCTTTTCTATTTCTGACTTGGGGGCATCAGCTCTGGATGGTCTAGTACGAGAGTGAGTAACCTAACTTGTTTCAACAGAGTGATGTGAGTATCGACAGAGCTCCGTTTACTGTCATCACTAGCACCAATGTCATAACGAGTGGAACGATTGGGGAGGCGGCTTGGCACCTTCATTTGGCCGGTTCTTGGGACCGATTCGTAATGAGTCTCAGAACGAATCATCGACTCACTATCTCGCCCGCTTTCGCTCTCGGGCAACCAGCCCCGGCGTTATCCCACATCCATATACTGAACTAAAAGGAGTGCGCAACACTCGAGCCGACAATGTAAGTCAGACTAATTCGTGCTCCGACTCTGCAAAGTCGTAAGGAAAAGTTATGGAACCTGCCGTTATAAAGTCGCCCCGCTAAAATCTTGTATTTCCGCTTCCATTGCGCTAGACTTTTTAACCGGTCGATCATTTAGCCGCCCATGCGGTTGCAAGGCTAAATTGTCTGGCAGTACTTTACTTGTCTGACCGGCAGTGATCATTTCACTCTGTGTAGACGAGTACACCGGAGCTCGTGGTTCGAATTTATACTGTCATTGAATGTGGCCTATCCTTGATTACCTGTCGTGTGCTCGGCGCTGAGTCCGTTTCGCTCTTGCTTTGACTGATTAGAATGAATTGAGTAAATTCCCTACTTGATCATCTCAGGATGCTTGAGAATTGGGGAAGTGACTGTACTAGCGCTAACCACATGTAATCCCCCTCGCCTTACCTTACTGGTGGTCGGGTCATAACGCTCTGAACGAACGCTGTTTATGGGTTGAGTCACACCTGGCATAGGCGTAGTGGGGCGACGCCATGCTCGGTATCTGGGCGCCTTCAATGTAGAACAACGTACA")