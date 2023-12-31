
import pandas as pd
import random
import argparse

def rand_rep(string_length, max_rep):
    """
    The function generates random nucleotide strings by sampling from a list of nucleotides ['A', 'C', 'T', 'G'].
    The length of each string is determined by the 'string_length' parameter, and the maximum repetition
    of each nucleotide in a string is determined by the 'max_rep' parameter.
    The function generates 100,000 strings and ensures that each generated string is unique by checking against
    the existing list of strings.
    The result is printed, displaying the maximum number of unique nucleotide strings that can be generated
    based on the provided parameters.
    The function returns a list containing all the generated unique strings.

    Args:
        string_length (int): The desired length of the generated nucleotide strings.
        max_rep (int): The maximum number of times a nucleotide can be repeated in a string.

    Returns:
        list: A list containing unique random nucleotide strings.

    """
    
    n = 0  
    strings_list = list()  # List to store generated strings.
    l = ["A", "C", "T", "G"]

    random.seed(35)  # Setting the random seed for reproducibility.
    
    while n < 100000:  
        bases_string = "".join([str(x) for x in random.sample(l, k=string_length, counts=[max_rep]*4)])  # Generating a random string by sampling from the nucleotide list.
        
        if bases_string not in strings_list:  # Checking if the generated string is already in the list.
            strings_list.append(bases_string)  # Adding the generated string to the list.
        else:
            pass  # If the string is already in the list, do nothing and continue to the next iteration.
        
        n += 1  
    
    
    print('Note: The maximum number of nucleotide strings that can be generated with the length of {} and maximum nuc/len of {} is: {}'.format(string_length, max_rep, len(strings_list)))
    
    return strings_list  




def generate_ascii_nuc_table(string_length, max_rep):
    """
    Generates an updated ASCII table with nucleotide codes and saves it as a CSV file.

    Args:
        string_length (int): The desired length of the generated nucleotide strings.
        max_rep (int): The maximum number of times a nucleotide can be repeated in a string.
        table_name (str, optional): The name of the output CSV file. Defaults to 'Nuc_ascii'.

    The function generates random nucleotide strings using the 'rand_rep' function and creates an updated ASCII table.
    It uses a pre-existing ASCII table stored in a CSV file named 'ASCII.csv'.
    The 'ASCII.csv' file should have columns: 'Decimal', 'Binary', 'Octal', 'Hexadecimal', 'Symbol', 'Description'.
    The function reads the 'ASCII.csv' file and adds two new columns: '0bBinary' and 'Nuc_code'.
    The '0bBinary' column contains the binary representation of each ASCII value with the '0b' prefix.
    The 'Nuc_code' column contains unique nucleotide strings generated by the 'rand_rep' function.
    The function ensures that the 'Nuc_code' column contains 128 unique strings, as the ASCII table has 128 characters.
    The updated table is rearranged and contains columns: 'Decimal', 'Binary', 'Octal', 'Hexadecimal',
    '0bBinary', 'Nuc_code', 'Symbol', 'Description'.
    The updated table is then saved as a CSV file with the provided 'table_name'.
    A confirmation message is printed, indicating the name of the saved CSV file.
    """

    # Setting the random seed for reproducibility.
    random.seed(5)

    # Reading the pre-existing ASCII table from 'ASCII.csv'.
    ascii = pd.read_csv("ASCII.csv", sep=",")

    # Prepending '0b' to the binary values.
    binary_with_pre = '0b' + ascii["Binary"].astype(str)

    # Generating random nucleotide strings using the 'rand_rep' function.
    strings = rand_rep(string_length, max_rep)

    nuc_strings = list()
    # Ensuring the 'nuc_strings' list contains 128 unique strings.
    while len(nuc_strings) < 128:
        random_element = random.choice(strings)
        if random_element not in nuc_strings:
            nuc_strings.append(random_element)

    ascii['0bBinary'] = binary_with_pre
    ascii['Nuc_code'] = nuc_strings


    ascii = ascii[['Decimal', 'Binary', 'Octal', 'Hexadecimal', '0bBinary', 'Nuc_code', 'Symbol', 'Description']]

    new_table_name = 'Nuc_ascii_SL{}_MR{}.csv'.format(string_length, max_rep)

    ascii.to_csv(new_table_name, sep=',', index=False)

    print('The updated ASCII table with nucleotide codes has been created and saved as: {}'.format(new_table_name))


def decoder(file_name, output_filename="Decoded_text", string_length=4, max_rep=2):
    """
    Decodes a file encoded using nucleotide ASCII encoding.

    Args:
        file_name (str): The name of the file to decode.
        output_filename (str, optional): The name of the decoded output file. Defaults to "Decoded_text".
        string_length (int, optional): The length of nucleotide strings used for encoding. Defaults to 4.
        max_rep (int, optional): The maximum repetition of nucleotide strings used for encoding. Defaults to 2.
    """

    with open(file_name, 'r') as f:
        read = f.readline()

    # Generate the table name
    table_name = 'Nuc_ascii_SL{}_MR{}.csv'.format(string_length, max_rep)
    path = "./{}".format(table_name)

    try:
        # Check if the table exists in the current directory
        table = pd.read_csv(table_name, sep=',')
        print("Table {} is found in the current directory and it is going to be used for decoding.".format(table_name))
    except FileNotFoundError:
        # Table not found, prompt user to generate it
        print("Table {} is not in the current directory. Please generate the table first.".format(table_name))
        n = input("Do you want to generate ASCII table with the entered parameters (Y/N)?")
        if n.lower() == 'y':
            generate_ascii_nuc_table(string_length, max_rep)
            table = pd.read_csv(table_name, sep=',')
            pass
        else:
            exit()

    start_index = 0
    end_index = string_length
    n = 0

    # Create the output file
    output_file = "{}_SL{}_MR{}.txt".format(output_filename, string_length, max_rep)
    open(output_file, 'w').close()

    try:
        # Decode the input file
        while n < len(read)/string_length:

            if n != len(read)/string_length - 1:
                # Decode a nucleotide string and write the symbol to the output file
                symbol = chr(table.loc[table['Nuc_code'] == read[start_index:end_index], 'Decimal'].values[0])
                start_index = end_index
                end_index = start_index + string_length
                with open(output_file, 'a') as f:
                    f.write(symbol)

            else:
                # Decode the last nucleotide string and write the symbol to the output file
                symbol = chr(table.loc[table['Nuc_code'] == read[start_index:], 'Decimal'].values[0])
                with open(output_file, 'a') as f:
                    f.write(symbol)

            n += 1
    except:
        # Handle errors in decoding process
        print("\033[1;31mError\033[0m: The entered parameters are not correct. Please try again with the following parameters:")
        try:
            # Try to extract the incorrect parameters from the output file name
            s = file_name[file_name.find('_SL')+3:file_name.find('_SL')+4]
            m = file_name[file_name.find('_MR')+3:file_name.find('_MR')+4]
            print("The string length that was used to encode {} is: {}".format(file_name, s))
            print("The maximum repetition that was used to encode {} is: {}".format(file_name, m))
            exit()
        except:
            exit()

    print("The file has been successfully decoded and saved as {}".format(output_file))




parser = argparse.ArgumentParser(description="Decodes a file that contains ASCII characters encoded using nucleotide encoding.")

parser.add_argument('-a', '--file_name', required=True, type=str, metavar='', help='The file name that contains DNA encoded text.')
parser.add_argument('-o', '--output_filename', required=False, type=str, default='Decoded_file', metavar='', help='The name of the output file of the decoded text (without the extension).')
parser.add_argument('-s', '--string_length', required=False, type=int,default=4, metavar='', help='The string length parameter that was used to encode the text you want to decode. Default value is 4')
parser.add_argument('-r', '--max_rep', required=False, type=int, default=2, metavar='', help='The maximum repetition parameter that was used for encoding the text you want to decode. Default value is 2.')

args = parser.parse_args()

if __name__ == '__main__':
    decoder(args.file_name, args.output_filename, args.string_length, args.max_rep)