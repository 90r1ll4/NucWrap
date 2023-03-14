from argparse import ArgumentParser
import json
import subprocess
from nuclei_wrapper.wrapper import nuclei


def nuclei_check() -> str:

    """To check if nuclei configured or not"""
    
    command = 'nuclei'

    try:
        # run the command
        subprocess.call([command, '-silent','--version'])
    except subprocess.CalledProcessError as e:
        if e.returncode == 127:
            print(f"Command '{command}' not found.")
            return None
    except FileNotFoundError as e:
        print("Nuclei not found")
        return None

    subprocess.call(['clear'])
    
    return True


def parser_argument() -> object:
   
    """Wrapper for the Nuclei cli."""

    # Parse arguments
    parser: ArgumentParser = ArgumentParser(description='Wrapper For Nuclei', epilog='python3 main.py -u scanme.nmap.org --json --tables')
    nuclei_wrapper = parser.add_argument_group('Wrapper Utility')
    nuclei_wrapper.add_argument('--url','-u', metavar = '', help = 'url to scan')
    nuclei_wrapper.add_argument('--url_file','-uf', metavar = '', help = 'list of urls')
    nuclei_wrapper.add_argument('--output','-o', metavar = '', help = 'Output in text form')
    nuclei_wrapper.add_argument('--json', action = 'store_true', help = 'Output in json form')
    nuclei_wrapper.add_argument('--tables', action = 'store_true', help = 'Output in table form')
    return parser.parse_args()


def main():
    
    args = parser_argument()

    #Checking if nuclei is installed or not
    if nuclei_check():
        result, tables = nuclei(args)
        if result:
            print(json.dumps(result, indent=4))
        if tables:
            print("\n",tables)


if __name__ == '__main__':
    main()
