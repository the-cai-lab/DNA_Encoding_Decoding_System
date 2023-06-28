This repository contains two Python scripts that are executable using the command line.

The first script (Encoder.py) is the Text-to-Nucleotide Encoder.

The second script (Decoder.py) is the Nucleotide-to-Text Decoder.

Note: This encoding/decoding system works only on English text with the first 128 ASCII values.

# Text-to-Nucleotide Encoder
The given code is used to generate nucleotide strings from English characters. Here is a summary of how it works:

1. The code defines a function named text_to_bin(Eng_file) that takes an English text file as input and converts the English characters to binary strings. It reads the lines from the file, converts each character to its binary representation, and concatenates the binary strings.

2. The code defines another function named rand_rep(string_length, max_rep) that generates random nucleotide strings. It takes two parameters: string_length, which determines the length of each generated string, and max_rep, which specifies the maximum repetition of each nucleotide in a string. The function generates 100,000 strings by sampling from a list of nucleotides ['A', 'C', 'T', 'G']. It ensures that each generated string is unique and returns a list containing all the generated unique strings.

3. The code defines a function named generate_ascii_nuc_table(string_length, max_rep) that generates an updated ASCII table with nucleotide codes. It takes the same parameters as the rand_rep function. The function reads a pre-existing ASCII table from a CSV file named "ASCII.csv". It generates random nucleotide strings using the rand_rep function and adds the nucleotide strings to the ASCII table. The updated table is then saved as a CSV file.

4. The code defines a function named encode(input_filename, output_filename, string_length, max_rep) that converts binary strings in an input file to nucleotide codes and writes the result to an output file. It takes four parameters: input_filename, which is the name of the input file containing binary strings; output_filename, which is the name of the output file to write the nucleotide codes (default is 'Encoded_text'); string_length, which is the desired length of each nucleotide code (default is 4); and max_rep, which is the maximum number of times a nucleotide can be repeated in a string (default is 2).

5. The encode function first checks if the updated ASCII table with the input parameters already exists. If not, it calls the generate_ascii_nuc_table function to generate the table.

6. The function then reads the ASCII table and the input file. It extracts the binary strings from the input file and converts each binary string to its corresponding nucleotide code using the ASCII table. The nucleotide codes are written to the output file.

7. The code uses the argparse module to parse command-line arguments. It takes arguments for the English file name, output file name, string length, and maximum repetitions. It then calls the encode function with the provided arguments.

### Installation
To run the script, you need to have Python installed on your system. The script is compatible with Python 3.6 and above.
Clone the repository to your local machine or download the script file directly.
Install the required dependencies by running the following command in your terminal:

```bash 

pip install pandas argparse

```

### Usage
The script provides a command-line interface for encoding text into nucleotide codes. It accepts the following command-line arguments:
```bash
python Encoder.py -a ENGLISH_FILE_NAME -b OUTPUT_FILE_NAME -l STRING_LENGTH -r MAXIMUM_REPETITIONS

```

* [ENGLISH_FILE_NAME] (required): The name of the file that contains the English text to be encoded. The file should be located in the current working directory.

* [OUTPUT_FILE_NAME] (optional): The name of the output file. If not provided, the default name "Encoded_text" will be used. The output file will be saved in the current working directory.

* [STRING_LENGTH] (optional): The length of the nucleotide strings that map to ASCII binary values. The default value is 4.

* [MAXIMUM_REPETITIONS] (optional): The maximum number of times a nucleotide can be repeated in a string. The default value is 2.

### Example
To encode an English text file named "input.txt" with a string length of 4 and a maximum repetition of 2, run the following command:

```bash

python Encoder.py -a input.txt -b Encoded_text -l 4 -r 2

```

The encoded nucleotide codes will be written to the output file "Encoded_text_SL4_MR2.txt" in the current working directory.

#### The assumptions regarding reproducibility in this code are:

1. The random seed is set for reproducibility: The code uses the random.seed() function to set the random seed. By setting a specific seed value (e.g., random.seed(35) in the rand_rep function), it ensures that the random number generator produces the same sequence of random numbers each time the code is executed with the same seed value. This allows for reproducibility of the generated nucleotide strings.

2. The ASCII table is consistent: The code assumes that the pre-existing ASCII table stored in the "ASCII.csv" file is consistent and does not change between different runs of the code. It relies on the information in the ASCII table to generate the nucleotide codes. If the ASCII table is modified or replaced, it may affect the reproducibility of the results.

3. The input file content remains the same: The code assumes that the content of the input file (English text or binary strings) remains the same between different runs of the code. If the input file is modified or replaced, it will produce different nucleotide codes as the encoding process depends on the content of the input file.

4. By considering these assumptions, the code aims to provide reproducibility in terms of generating the same nucleotide strings given the same input file and parameters, and using the same random seed for random number generation.


# Nucleotide-to-text Decoder
This Python script decodes a file that contains ASCII characters encoded using nucleotide encoding. The script takes the encoded file as input, decodes it, and saves the decoded text to an output file.

1. The decoder function looks for the updated ASCII table that was used for encoding the original text and that contains nucleotide codes. If not found, the decoder function prompts the user to generate a table with the same criteria used for encoding the original text.

2. The rand_rep function generates random nucleotide strings based on the provided string length and maximum repetition parameters. It uses the random.sample function to sample nucleotides from the list ['A', 'C', 'T', 'G'] and creates a random string of the desired length. It ensures that each generated string is unique by checking against the existing list of strings. The function continues generating strings until it reaches a total of 100,000 unique strings. The maximum number of unique nucleotide strings that can be generated based on the provided parameters is printed, and the list of generated strings is returned.

3. The generate_ascii_nuc_table function generates an updated ASCII table with nucleotide codes and saves it as a CSV file. It reads a pre-existing ASCII table from the 'ASCII.csv' file using the pd.read_csv function. It then adds two new columns to the table: '0bBinary' and 'Nuc_code'. The '0bBinary' column contains the binary representation of each ASCII value with the '0b' prefix, and the 'Nuc_code' column contains unique nucleotide strings generated by the rand_rep function. The function ensures that the 'Nuc_code' column contains 128 unique strings, as there are 128 characters in the ASCII table. The updated table is rearranged, and the resulting table is saved as a CSV file with a name based on the provided string length and maximum repetition parameters.

4. The decoder function decodes a file that has been encoded using nucleotide ASCII encoding. It takes the encoded file name, output file name, string length, and maximum repetition as parameters. The function reads the encoded file and retrieves its contents using the readline function. It checks if the necessary ASCII table file exists in the current directory. If the table file is found, it proceeds with decoding. Otherwise, it prompts the user to generate the ASCII table using the generate_ascii_nuc_table function and exits. The function decodes the nucleotide strings in the encoded file using the provided ASCII table and writes the decoded symbols to the output file.

5. The script includes an argument parser that allows running the nuc_decoder function from the command line. It parses the command-line arguments for the encoded file name, output file name, string length, and maximum repetition. These arguments are then passed to the nuc_decoder function.

### Installation
To run the script, you need to have Python installed on your system. 

The script is compatible with Python 3.6 and above.

Clone the repository to your local machine or download the script file directly.

Install the required dependencies by running the following command in your terminal:

```bash
pip install pandas argparse
```

### Usage
The script provides a command-line interface for decoding nucleotide-encoded files. It accepts the following command-line arguments:
```bash
python Decoder.py -a ENCODED_FILE_NAME -o OUTPUT_FILE_NAME -s STRING_LENGTH -r MAXIMUM_REPETITIONS

```
* [ENCODED_FILE_NAME] (required): The name of the file that contains the nucleotide-encoded text to be decoded. The file should be located in the current working directory.

* [OUTPUT_FILE_NAME] (optional): The name of the output file where the decoded text will be saved. If not provided, the default name "Decoded_file" will be used. The output file will be saved in the current working directory.

* [STRING_LENGTH] (optional): The string length parameter that was used for encoding the text. The default value is 4.

* [MAXIMUM_REPETITIONS] (optional): The maximum repetition parameter that was used for encoding the text. The default value is 2.

### Example
To decode an encoded file named "encoded.txt" with a string length of 4 and a maximum repetition of 2, run the following command:

```bash
python Decoder.py -a encoded.txt -o Decoded_file -s 4 -r 2

```
The decoded text will be saved in the output file "Decoded_file_SL4_MR2.txt" in the current working directory.

#### The assumptions for the reproducibility of this code are as follows:

1. Random Seed: The code uses the random module to generate random nucleotide strings and to set the random seed for reproducibility. It assumes that the same random seed value will be used consistently across different runs of the script. By setting the random seed to the same value, the random number generation process will be deterministic, ensuring that the same set of random nucleotide strings is generated each time the script is executed with the same parameters.

2. File and Table Stability: The code assumes that the input file containing the encoded text and the ASCII table ('ASCII.csv') remain unchanged between different runs of the script. Any modifications to the input file or the ASCII table can lead to different decoding results. To ensure reproducibility, it is important to keep the input file and the ASCII table intact without any modifications between different runs of the script.

3. Dependency Stability: The code relies on external dependencies, such as the pandas library, for reading and manipulating data. It assumes that the versions of these dependencies remain stable and do not change between different runs of the script. Changes in library versions or dependencies may lead to different behaviors or results, affecting the reproducibility of the code.

4. System Environment: The code assumes that the script is executed in the same system environment or on the same machine between different runs. Different environments or machines may have variations in system configurations, libraries, or random number generators, which can affect the reproducibility of the code.

5. Consistent Parameter Values: The code assumes that the same parameter values are used consistently between different runs of the script for encoding and decoding. If the parameter values are changed, such as the string length or maximum repetition, the decoding process may yield different results. It is important to maintain consistency in the parameter values to ensure reproducibility.

6. By adhering to these assumptions and ensuring stability and consistency in the random seed, input files, dependencies, system environment, and parameter values, the code can be reproducible, producing the same decoding results each time it is executed with the same inputs and settings.