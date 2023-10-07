operations = {
        'transcribe': transcribe,
        'reverse': reverse,
        'complement': complement,
        'reverse_complement': reverse_complement
    }

transcription_dict = {
    'A': 'U', 'a': 'u',
    'T': 'A', 't': 'a',
    'G': 'C', 'g': 'c',
    'C': 'g', 'c': 'g'
}


complement_dict = {
    'A': 'T', 'a': 't',
    'T': 'A', 't': 'a',
    'G': 'C', 'g': 'c',
    'C': 'g', 'c': 'g'
}


def transcribe(sequns: str) -> str:
    """
    That function transcribe DNA to RNA
    :param sequns: DNA sequence
    :return: RNA sequence
    """
    return ''.join([transcription_dict[i] for i in sequns])


def reverse (sequns: str) -> str:
    """
    That function reverses DNA sequence
    :param sequns:DNA sequense 
    :return: reversed DNA sequence
    """
    return sequns[::-1]

def complement (sequns: str) -> str:
    """
    That function create a complementarity chain fot the DNA sequence
    :param sequns: DNA sequense
    :return: complementarity chain to the DNA sequence
    """
    return ''.join([complement_dict[i] for i in sequns])


def dna_rna_tools (*args):
    *sequnses, def_name = args
    for sequns in sequnses:
        if RNA_checking(sequns) == True:
            continue
        else:
            raise ValueError('Incorrect options input, please try again')
    result = []
    for sequns in sequnses:
        res = operations[def_name](sequns)
        result.append(res)
    return (result) 
