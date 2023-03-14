import subprocess, json, re
from unittest import result
from prettytable import PrettyTable
from typing import Union



def nuclei(args: object) -> Union[object, object]:

    """Run a command and pass its output through nuclei"""

    command = ['nuclei']

    if args.url:
        command +=  ['-u', args.url]
    elif args.url_file:
        url_list = ''

        #read lines from the list and add it in url_list.
        with open(args.url_file, 'r') as file:
            for line in file:
                url_list += '-u ' + line.strip() + " "

        command += url_list.split()

    if args.tables or args.json:
        command +=  ['--json', '-o', 'runtime_output.json']
    elif args.output:
        command +=  ['-o', 'runtime_output.txt']
    
    try:
        #Added Timeout so the plugin does not take lot of time in running
        subprocess.run(command, stdout=subprocess.PIPE, timeout= 150)
    except subprocess.TimeoutExpired:
        pass


    return(result_parsing(args))


def result_parsing(args: object) -> Union[object, object]:

    """ To parse result as per the user"""

    output_table = None
    result = None
    if args.json:
        result = output_json()
    elif args.output:
        result = output_normal()

    if args.tables:
        output_table = output_tables()

    return(result, output_table)

def output_json() -> json:

    """To convert the reult in json format"""

    with open('runtime_output.json', 'r') as file:
        data = file.read()

    # replace all occurrences of '}\n{' with '},\n{'
    json_data = json.loads('[' + re.sub(r'}\n{', '},\n{', data).strip() + ']')

    return(json_data)


def output_normal()-> str:

    """To give result as it is"""

    with open('runtime_output.txt', 'r') as file:
        data = file.read()

    return(data)


def output_tables() -> object:

    """To convert the output into tables form"""

    json_data = output_json()
    
    if not json_data:
        return None

    # definig structure for the tables
    nuclei_table = PrettyTable(["Template-Id", "Host" ,"Type", "severity"])

    # to add data in file
    for table in range(len(json_data)):
        nuclei_table.add_row([json_data[table]['template-id'], json_data[table]['host'], json_data[table]['type'], json_data[table]["info"]['severity']])

    return nuclei_table
