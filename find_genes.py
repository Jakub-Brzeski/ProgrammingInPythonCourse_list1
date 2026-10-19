import list1

#Task 6
def find_genes_in_sequence(dna):
    """Scans a DNA sequence to identify all potential genes.

    A valid gene starts with ATG, ends with a stop codon (TAG, TAA, TGA),
    has a length that is a multiple of 3, and contains no internal stop codons.

    Args:
        dna: String representing a DNA sequence.

    Returns:
        List of strings containing all identified gene sequences.
    """
    stop_codons = ["TAG", "TAA", "TGA"]
    genes = []
    i = 0

    while i < len(dna):
        if dna[i:i + 3] == "ATG":
            j = i + 3
            while j < len(dna):
                codon = dna[j:j + 3]
                if codon in stop_codons:
                    gene = dna[i:j + 3]
                    genes.append(gene)
                    break
                j += 3
        i += 1

    return genes

def main():
    user_input = input("Enter a DNA sequence: ").strip().upper()

    try:
        comp_dna = list1.dna_complement(user_input)
    except (TypeError, ValueError) as e:
        print("Error processing DNA sequence:", e)
        return

    original_genes = find_genes_in_sequence(user_input)
    complement_genes = find_genes_in_sequence(comp_dna)

    print("\n--- Results ---")
    print("Original sequence:", user_input)
    if original_genes:
        print("Genes in original sequence:", original_genes)
    else:
        print("No genes found in original sequence.")

    print("\nComplementary sequence:", comp_dna)
    if complement_genes:
        print("Genes in complementary sequence:", complement_genes)
    else:
        print("No genes found in complementary sequence.")

if __name__ == '__main__':
    main()