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


def fasta_filtering(seqs, gc_bounds = (0, 100), length_bounds = [0, 2**32], quality_threshold = 0):
    outline_new_dict_fasta = {}
    inline_new_dit_fasta = {}
    for key, value in seqs.items():
        sequence_for_filtering = value[0]
        quality_of_sequence_for_filterring = value[1]
        if GC_cont_check(sequence_for_filtering, gc_bounds) == True and lenght_chech(sequence_for_filtering, length_bounds) == True and quality_chech(quality_of_sequence_for_filterring, quality_threshold) == True:
            inline_new_dit_fasta[key]= value
    outline_new_dict_fasta = {**inline_new_dit_fasta}
    return (outline_new_dict_fasta)

fasta_filtering(seqs)
