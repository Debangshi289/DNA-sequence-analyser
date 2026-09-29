# Validate DNA sequence
dna = input("Enter DNA Sequence : ")
dna = dna.upper()

valid = True

for nucleotide in dna:
    if nucleotide not in "ATGC":
        valid = False
        print("Invalid character found:", nucleotide)
        break

if valid:
    print("=================================")
    print("     DNA ANALYSIS REPORT")
    print("=================================")
    print("DNA sequence :", dna)
    print()

    # Count nucleotides
    a_count = 0
    t_count = 0
    g_count = 0
    c_count = 0

    for nucleotide in dna:
        if nucleotide == "A":
            a_count = a_count + 1
        elif nucleotide == "T":
            t_count = t_count + 1
        elif nucleotide == "G":
            g_count = g_count + 1
        elif nucleotide == "C":
            c_count = c_count + 1

    print("A Count : ", a_count)
    print("T Count : ", t_count)
    print("G Count : ", g_count)
    print("C Count : ", c_count)

    # Calculate sequence Length
    length = len(dna)
    print("Length : ", length)

    # Calculate GC Content
    gc_content = ((g_count + c_count) / length) * 100
    print("GC content :",round(gc_content,2), "%")

    # Calculate AT Content
    at_content = ((a_count + t_count) / length) * 100
    print("AT content :",round(at_content,2), "%")

    # Generate Complement
    complement = ""

    for nucleotide in dna:
        if nucleotide == "A":
            complement = complement + "T"
        elif nucleotide == "T":
            complement = complement + "A"
        elif nucleotide == "G":
            complement = complement + "C"
        elif nucleotide == "C":
            complement = complement + "G"

    print("Complement :", complement)

    # Generate Reverse Complement
    reverse_complement = complement[::-1]
    print("Reverse complement :", reverse_complement)

    # DNA to RNA transcription
    rna = ""

    for nucleotide in dna:
        if nucleotide == "T":
            rna = rna + "U"
        else:
            rna = rna + nucleotide

    print("RNA Sequence :", rna)
    print("=================================")
else:
    print("Invalid sequence")
    