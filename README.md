# NucWrap

Nucwrap is a wrapper tool around the nuclei scanner which converts the output to a loadable format of JSON and table format.



# Using the Nucwrap

## Installation Through PIP
To install dependencies, use the following command:

```bash
pip3 install -r requirements.txt
```
To use the Nucwrap, you can run it with the following command:
```bash
python3 main.py -u example.com --json --tables
python3 main.py -u example.com -o 
```

For an overview of all commands use the following command:

```bash
python3 main.py -h
```

The output shown below are the latest supported commands.

```bash
usage: python3 main.py [-h] [--url URL] [--url_file URL_FILE] [--output OUTPUT] [--json] [--tables]

Wrapper For Nuclei

optional arguments:
  -h, --help           show this help message and exit
  --url URL, -u URL    url to scan
  --url_file URL_FILE, --uf URL_FILE
                       list of urls
  --output OUTPUT, -o OUTPUT
                       Output in text form
  --json               Output in json form
  --tables             Output in table form


Example: 
```

## Installation with Docker
This tool can also be used with [Docker](https://www.docker.com/). To set up the Docker environment, follow these steps (trying using with sudo, if you get any error):

```bash
docker build -t nucwrap .
```

## Using the Docker Container

A typical run through Docker would look as follows:

```bash
docker run --rm nucwrap -u scanme.nmap.org -o --tables
```

**NOTE:** Nucwrap should be used responsibly and with permission from the target owner.
