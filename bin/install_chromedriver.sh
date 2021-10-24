#!/bin/bash

# see https://chromedriver.chromium.org/downloads/version-selection

chrome_version=$(google-chrome --version | grep -o '[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*')
echo "chrome patch version: $chrome_version"

chromedriver_version=$(wget -O- -q "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version" | grep -o '[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*')
echo "equivalent chromedriver version: $chromedriver_version"

wget --no-verbose -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$chromedriver_version/chromedriver_linux64.zip"
unzip /tmp/chromedriver.zip -d /usr/bin/
rm /tmp/chromedriver.zip
