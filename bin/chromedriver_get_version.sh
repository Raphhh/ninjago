#!/bin/bash

# see https://chromedriver.chromium.org/downloads/version-selection

chrome_version=$(cat <&0 | grep -o '[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*')
wget -O- -q "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version" | grep -o '[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*\.[[:digit:]]*'
