from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

if __name__ == '__main__':
    genbank_file_path = 'input_files/unknown_virus.gb'

    genbank_file = open(genbank_file_path, 'r')
    genbank_count = 1

    for genebank in SeqIO.parse(genbank_file, 'genbank'):
        print(f'------------- Genbank record #{genbank_count} -------------')
        neuclotide_sequence = genebank.seq
        neuclotide_sequence_complementary = genebank.seq.reverse_complement()

        orfs = [1, 2, 3]
        proteins_by_orf = {1: [], 2: [], 3: []}
        proteins_complementary_by_orf = {1: [], 2: [], 3: []}

        for orf in orfs:
            neuclotide_sequence_with_ORF_applied = neuclotide_sequence[orf - 1:]
            aminoacids = neuclotide_sequence_with_ORF_applied.translate()
            aminoacids_separated_by_stop_codons = aminoacids.split('*')
            for protein in aminoacids_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    proteins_by_orf[orf].append(protein)

            neuclotide_sequence_complementary_with_ORF_applied = neuclotide_sequence_complementary[orf - 1:]
            aminoacids_complementary = neuclotide_sequence_complementary_with_ORF_applied.translate()
            aminoacids_complementary_separated_by_stop_codons = aminoacids_complementary.split('*')
            for protein in aminoacids_complementary_separated_by_stop_codons:
                start_position = protein.find('M')
                if start_position != -1:
                    protein = protein[start_position:]
                    proteins_complementary_by_orf[orf].append(protein)

        output_path = f'output_files/Ejercicio1_{genbank_count}.fasta'

        all_proteins = []
        for orf, proteins_in_orf in proteins_by_orf.items():
            for protein in proteins_in_orf:
                all_proteins.append((protein, orf))
        for orf, proteins_in_orf in proteins_complementary_by_orf.items():
            for protein in proteins_in_orf:
                all_proteins.append((protein, (-1) * orf))

        sorted_proteins = sorted(
            all_proteins,
            key=lambda protein_tuple: len(protein_tuple[0]),
            reverse=True
        )

        protein_records = []

        for i, (protein, orf) in enumerate(sorted_proteins):
            protein_records.append(SeqRecord(protein,
                                             description=f'Protein #{i+1} translated from {genebank.id} with ORF = {orf}'))

        SeqIO.write(protein_records, output_path, 'fasta')

        genbank_count += 1
