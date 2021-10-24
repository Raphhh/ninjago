FROM python:3

# system
RUN apt-get update
RUN apt install unzip

# install chrome
RUN wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_95.0.4638.54-1_amd64.deb
RUN apt install -y /tmp/chrome.deb
RUN rm /tmp/chrome.deb
RUN google-chrome --version

# install selenium driver
COPY bin/install_chromedriver.sh /usr/bin/
RUN /usr/bin/install_chromedriver.sh
RUN rm /usr/bin/install_chromedriver.sh
RUN chromedriver --version

# add user to execute chrome
RUN useradd lloyd
RUN mkdir -p /home/lloyd && chown lloyd:lloyd /home/lloyd

# control inputs
RUN apt-get install -y scrot
RUN apt-get install -y python3-tk
RUN apt-get install -y python3-dev

# set python venv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY . .
CMD ["python", "main.py"]