 operations = {
        'length': length_info,
        'percentage': count_percentage_aa,
        'pattern': find_pattern,
        '3Letter_name': rename_three_letter_name,
        'DNA_code': get_protein_gene
    }

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
