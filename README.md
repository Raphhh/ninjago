# Ninjago GA gamer

This driver plays to [LEGO Ninjago Prime Empire](https://www.lego.com/fr-be/kids/games/ninjago/prime-empire-f98e88849512c6f12bb01678c9ce6c65) with a genetic algorithm AI written in Python3.


## Install and run

 1. This project works with Linux systems.
 2. Clone the project: `$ git clone git@github.com:Raphhh/ninjago.git && cd ninjago`
 3. Build docker image: `# docker-compose build`
 4. (Maybe you need to allow your host to display Chrome: `$ xhost local:root`)
 5. Run docker: `# docker-compose up`

## How it works

### Chrome "headfull" in Docker

#### Why Chrome?

Just because we need to manipulate a browser with `selenium` and retrieve the console logs.
But, unfortunately, the [WebDriver protocol recommendation](https://www.w3.org/TR/webdriver1/) does not specify any method for this.
So, [geckodriver](https://github.com/mozilla/geckodriver), the Firefox's driver, does not implement it ([issue #330](https://github.com/mozilla/geckodriver/issues/330)).

#### Installing Chrome

In `Dockerfile`, we install Chrome:

```dockerfile
RUN wget --no-verbose -O /tmp/chrome.deb http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_95.0.4638.54-1_amd64.deb
RUN apt install -y /tmp/chrome.deb
RUN rm /tmp/chrome.deb
RUN google-chrome --version
```

And we specify a user ("lloyd" is the green ninja):

```dockerfile
RUN useradd lloyd
RUN mkdir -p /home/lloyd && chown lloyd:lloyd /home/lloyd
```

In `docker-compose.yml`, we specify the following params:

```yaml
user: lloyd
privileged: true
shm_size: 2gb
```

#### Why Chrome needs to run "headfull"?

First, because the purpose of this app is to show the game (and not really calculate a very very long solution).
Second, the app interacts with the game by using `pyautogui` and not `selenium`.

For this, we just need to specify in `docker-compose.yml` the following params:

```yaml
environment:
  - DISPLAY=${DISPLAY}
network_mode: host
```

##### Sources

 - [cloudsavvyit.com](https://www.cloudsavvyit.com/10520/how-to-run-gui-applications-in-a-docker-container/)
 - [medium.com](https://medium.com/dot-debug/running-chrome-in-a-docker-container-a55e7f4da4a8)
 - [stackoverflow.com](https://stackoverflow.com/questions/28392949/running-chromium-inside-docker-gtk-cannot-open-display-0/34586732)


### Selenium in Docker

#### Why Selenium?

[Selenium](https://www.selenium.dev/) is a [WebDriver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) client.
It will allow us to manipulate Chrome easily from the code.

#### Installing chromedriver

In `Dockerfile`, we need to install [chromedriver](https://chromedriver.chromium.org) :

```dockerfile
RUN apt install unzip
COPY bin/install_chromedriver.sh /usr/bin/
RUN /usr/bin/install_chromedriver.sh
RUN rm /usr/bin/install_chromedriver.sh
RUN chromedriver --version
```

The only problem with the installation of `chromedriver` is the [matching of its version](https://chromedriver.chromium.org/downloads/version-selection) with the `google-chrome` one's. It is why we use `bin/install_chromedriver.sh`.

In `requirements.txt`, we specify [selenium](https://selenium-python.readthedocs.io/) for python:

```text
selenium~=4.0.0
```

#### Retrieving console logs with chromedriver

Remote logging is still considered a non-standard feature and not all the browsers support it. 

The `loggingPrefs` is one of the capabilities of `chromedriver`,
but does not appear in the [doc](https://chromedriver.chromium.org/capabilities).

In python, we need to specify we want to retrieve all the logs coming from the browser,
when we instantiate the driver.
The key `browser` is the type of logs and means here the console logs from the browser.
This is specific for each driver.

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
driver = webdriver.Chrome(desired_capabilities=capabilities)
```

Then, you can call the method `get_log`:

```python
console_log_entries = driver.get_log('browser')
```

##### Sources

 - [Selenium specific capabilities](https://www.selenium.dev/documentation/webdriver/capabilities/driver_specific_capabilities/)
 - [Selenium python API for desired capabilities](https://selenium-python.readthedocs.io/api.html#desired-capabilities)
 - [Selenium logging](https://github.com/SeleniumHQ/selenium/wiki/Logging)

### Input control with pyautogui

#### Why input control?

Selenium only interacts with selected html elements of the current page. 
That means there is some security restrictions, as well in Javascript.
To simulate totally normal user inputs and control mouse and keyboard, 
we use `pyautogui` that will interact directly with the system.


#### Installing pyautogui

In  `Dockerfile`, we install the required system dependencies:

```dockerfile
RUN apt-get install -y scrot
RUN apt-get install -y python3-tk
RUN apt-get install -y python3-dev
```

In `requirements.txt`, we specify [pyautogui](https://pyautogui.readthedocs.io) for python:

```text
PyAutoGUI~=0.9.53
```

And to work with Chrome, [python-xlib](https://pypi.org/project/python-xlib/) is required:

```text
python-xlib~=0.31
```


