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
