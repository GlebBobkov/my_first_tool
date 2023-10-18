from os import makedirs
import os.path

def GC_cont_check(sequence_for_filtering: str , gc_bounds: list) -> bool:
    """
    Check the GC content of the sequence for filtering
    :param sequence_for_filtering: analyzed sequence
    :param gc_bounds: list with limitation for GC content
    :return: bool argument for filtering in fasta_filtering function
    """
    GC_counter = 0
    for i in sequence_for_filtering:
        if i == "C" or i == "G" or i == "c" or i == "g":
            GC_counter += 1
    GC_calculc = GC_counter/len(sequence_for_filtering)*100
    if len(gc_bounds)==1:
        if GC_calculc <= gc_bounds[0]:
            return True
    if len(gc_bounds) == 2:
        if GC_calculc <= gc_bounds[1] and GC_calculc >= gc_bounds[0]:
            return True

def lenght_chech (sequence_for_filtering: str, length_bounds: list) -> bool:
    """
    Check the lenght of the sequence for filtering
    :param sequence_for_filtering: analyzed sequence
    :param length_bounds: list with limitations for lenght
    :return: bool argument for filtering in fasta_filtering function
    """
    if len(length_bounds)==1:
        if len(sequence_for_filtering) <= length_bounds[0]:
            return True
    if len(length_bounds) == 2:
        if len(sequence_for_filtering) <= length_bounds[1] and len(sequence_for_filtering) >= length_bounds[0]:
            return True

def quality_chech (quality_of_sequence_for_filterring: str, quality_threshold: int) -> bool:
    """
    Check the quality of the sequence for filtering
    :param quality_of_sequence_for_filterring: 2nd key for the sequense with quality of each nucleotide reading 
    :param quality_threshold: limitation for the quality of nucleotides reading
    :return: bool argument for filtering in fasta_filtering function
    """
    quality_threshold = str(quality_threshold)
    quality_counter = 0
    for i in quality_of_sequence_for_filterring:
        quality_counter += ord(i)
    quality = quality_counter/len(quality_of_sequence_for_filterring)
    if quality >= ord(quality_threshold):
        return True


def seqs_creation(input_path_input: str) -> dict:
    """
    Reading of the input file and creating the dictinary of the seqs
    with structure
     {name' : ('sequence', 'comment' 'quality')
     }
    :param input_path_input:
    :return: dictinary of esquenses 
    """

    path_input = str(input_path_input)
    inline_new_dit_fasta = {}
    outline_new_dict_fasta = {}
    py_file = open (path_input)
    lines = py_file.readlines()
    i = 0
    seq = {}
    seqs = {}
    while i != (len(lines)):
        key = lines[i]
        key = key[:-1]
        value_1 = lines[i+1]
        value_1 = value_1 [:-1]
        value_3 = lines[i+2]
        value_3 = value_3[:-1]
        value_2 = lines[i+3]
        if value_2[-1] == '\n':
            value_2 = value_2[:-1]
        value = [value_1, value_3 ,value_2]
        seq[key] = value
        seqs = {**seq}
        i +=  4
    return seqs

 
def fasta_filtering(seqs, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0):
    if type(gc_bounds) != tuple:
        gc_bounds = (0, gc_bounds)
    if type(length_bounds) != tuple:
        length_bounds = (0, length_bounds)
    outline_new_dict_fasta = {}
    inline_new_dit_fasta = {}
    for key, value in seqs.items():
        sequence_for_filtering = value[0]
        quality_of_sequence_for_filterring = value[1]
        if GC_cont_check(sequence_for_filtering, gc_bounds) == True and lenght_chech(sequence_for_filtering, length_bounds) == True and quality_chech(quality_of_sequence_for_filterring, quality_threshold) == True:
            inline_new_dit_fasta[key]= value
    outline_new_dict_fasta = {**inline_new_dit_fasta}
    return (outline_new_dict_fasta)


