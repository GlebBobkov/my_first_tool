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
