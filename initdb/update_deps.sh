#!/bin/bash
python3 -m venv .dep_venv

VENV_BIN=$PWD/.dep_venv/bin

$VENV_BIN/pip install --upgrade pip pip-tools
$VENV_BIN/pip-compile requirements.in

rm -rf .dep_venv
