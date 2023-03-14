# Maintainer
FROM python:3.10-bullseye

LABEL maintainer="Ashwin Singh <ashwinsinghsingh666672@gmail.com>"
LABEL description="This tool acts as a wrapper for Nuclei and generates a formatted JSON output that can be loaded and tables."
# Install required packages
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip git zip unzip

# Install Nuclei
# RUN go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei
RUN wget https://dl.google.com/go/go1.20.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.20.linux-amd64.tar.gz

ENV GOROOT=/usr/local/go 
ENV GOPATH=$HOME/go 
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH

RUN go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

WORKDIR /usr/src/app
# Copy the entrypoint script
COPY . .

# Install Project Dependencies
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt


# Set the entrypoint script as the default command
ENTRYPOINT ["python3","main.py"]
