#!/bin/bash
rm -rf dataset/
wget https://codechallengestracc.blob.core.windows.net/code-challenge/dublin-dataset.zip
unzip dublin-dataset.zip -d dataset
rm dublin-dataset.zip
