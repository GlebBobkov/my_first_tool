coperations = {
        'length': length_info,
        'percentage': count_percentage_aa,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'DNA_code': get_protein_gene
    }


retrnaslation_dict = {
        'F': 'TTC', 'f': 'ttc',
        'L': 'TTA', 'l': 'tta',
        'S': 'TCG', 's': 'tcg',
        'Y': 'TAC', 'y': 'tac',
        'C': 'TGC', 'c': 'tgc',
        'W': 'TGG', 'w': 'tgg',
        'P': 'CCC', 'p': 'ccc',
        'H': 'CAT', 'h': 'cat',
        'Q': 'GAA', 'q': 'gaa',
        'R': 'CGA', 'r': 'cga',
        'I': 'ATT', 'i': 'att',
        'M': 'ATG', 'm': 'atg',
        'T': 'ACC', 't': 'acc',
        'N': 'AAT', 'n': 'aat',
        'K': 'AAA', 'k': 'aaa',
        'V': 'GTT', 'v': 'gtt',
        'A': 'GCA', 'a': 'gca',
        'D': 'GAT', 'd': 'gca',
        'E': 'GAG', 'e': 'gag',
        'G': 'GGG', 'g': 'ggg'
    }


threel = {'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': "ASP", 'V': 'VAL',
              'H': 'HIS', 'G': "GLY", 'Q': "GLN", 'E': 'GLU', 'I': 'ILE',
              'L': 'LEU', 'K': 'LYS', 'M': 'MET', 'P': 'PRO', 'S': 'SER',
              'Y': 'TYR', 'T': 'THR', 'W': 'TRP', 'F': 'PHE', 'C': 'CYS',
              'a': 'ala', 'r': 'arg', 'n': 'asn', 'd': "asp", 'v': 'val',
              'h': 'his', 'g': "gly", 'q': "gln", 'e': 'glu', 'i': 'ile',
              'l': 'leu', 'k': 'lys', 'm': 'met', 'p': 'pro', 's': 'ser',
              'y': 'tyr', 't': 'thr', 'w': 'trp', 'f': 'phe', 'c': 'cys'
}


def length_info (protein: str) -> int:
    """
    Сounting the length of an amino acid sequence/protein in the number of amino acids
    :param protein:  sequence of protein
    :return: number of amino acids in an amino acid sequence/protein
    """
    return len(protein)


def count_percentage_aa(seq: str) -> dict:
    """
    Count percentage of each amino acid in sequence
    arguments:
        - seq (str): sequence for counting
    return:
        - dict: dictionary with counted percentage
    """
    l = count_length(seq)
    result = {}
    for aa in seq:
        if aa not in result:
            result[aa] = 1
        else:
            result[aa] += 1
    result.update((key, round(value / l * 100, 2)) for key, value in result.items())
    res = {key: value for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True)}
    return res


def compare_pattern(sequence: str, pattern: str) -> bool:
    """
    Compare a given pattern to a fragment of sequence of the same length
    arguments:
    - sequence (str): sequence fragment to compare with the pattern
    - pattern (str): pattern for comparison
    return:
    - (bool): whether pattern and fragment match
    """
    for i in range(0, len(sequence)):
        if not sequence[i] == pattern[i]:
            return False
    return True


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
