operations = {
        'length': length_info,
        'percentage': count_percentage_aa,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'DNA_code': get_protein_gene
    }


def find_pattern(sequences: list, pattern: str) -> dict:
    """
    Find all non-overlaping instances of a given pattern in sequences
    arguments:
    - sequences (list): sequences to find the pattern in
    - pattern (str): pattern in question
    return
    - finds(dict): dictionary with sequences as keys and lists of indexes of patterns and the number of patterns as values
    """
    finds = {}
    for j in range(0, len(sequences)):
        find = []
        for i in range(0, len(sequences[j])):
            if compare_pattern(sequences[j][i:i + len(pattern)], pattern):
                find.append(i)
                i += len(pattern)
        finds[sequences[j]] = [len(find)] + find
    return finds


def get_protein_gene(protein):
    """
    Transforming of an amino acid sequence/protein to DNA sequence
    :param protein: amino acid sequence of protein
    :return: sequence of protein in the DNA sequence form
    """
    return ''.join([retrnaslation_dict[aa] for i in protein])


def rename_three_letter_name(seqs: list, sep='') -> list:
    """
    Transform into a three-letter amino acids entry.
    arguments:
        - seqs (list): list of sequences for transforming to three-letter entire
        - sep (str): separator between aminoacids, default = ''
    return:
        - list: transformed sequences with separators
    """
    res = []
    for seq in seqs:
        threel_form = ''
        for aa in seq:
            threel_form = threel_form + threel[aa] + sep
        if sep:
            threel_form = threel_form[:-1]
        res.append(threel_form)
    return res


def protein_tool(*proteins, options=None):
    proteins = list(proteins)

    operations = {
        'compare': compare,
        'length': length_info,
        'percentage': count_percentage_aa,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'DNA_code': get_protein_gene
    }

    if options == 'compare':
        result = operations[options](proteins[:-2], proteins[-2], proteins[-1])
        return (result)
    elif options == '3Letter_name':
        result = operations[options](proteins[:-1], proteins[-1])
        return result
    elif options == 'length' or options == 'percentage' or options == 'DNA_code':
        result = []
        for protein in proteins:
            res = operations[options](protein)
            result.append(res)
        return (result)
    else:
        raise ValueError('Incorrect options input, please try again')
