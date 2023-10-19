from os import makedirs
import os.path


def convert_multiline_fasta_to_oneline(path_input: str, output_fasta = None):
    """
    Convert mulriline fasta to the onle line fasta  
    :param path_input: file for analysing and reding 
    :param output_fasta: converted file with one line fasta writing 
    :return: 
    """
    with open(path_input, mode='r') as f:
        list_of_readed_lines = []
        for line in f:
            line = line.strip('\n')
            list_of_readed_lines.append(line)
    list_for_printing = []
    for i in list_of_readed_lines:
        if i == list_of_readed_lines[0]:
            list_for_printing.append(i)
            one_line_sum = ''
        else:
            if i[0] == '>':
                list_for_printing.append(one_line_sum)
                list_for_printing.append(i)
                one_line_sum = ''
            else:
                one_line_sum = one_line_sum + str(i)
        if i == list_of_readed_lines[-1]:
            list_for_printing.append(one_line_sum)
    if output_fasta != None:
        os.makedirs('bio_files_processor_results', exist_ok=True)
        output_fasta = 'bio_files_processor_results/' + output_fasta + '.fastq'
    else:
        os.makedirs('bio_files_processor_results', exist_ok=True)
        output_fasta = 'bio_files_processor_results/' + path_input
    with open(output_fasta, mode='w') as f:
        for line in list_for_printing:
            f.write(line + '\n')
