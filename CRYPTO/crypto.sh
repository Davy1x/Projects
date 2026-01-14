#!/bin/bash

intro_msg="< WELCOME__TO__CRYPTO >"
clear
echo "$intro_msg"

read -p $'1. Launch Program\n2. Read Doc\n> ' stdin

if [[ "$stdin" == '1' ]]; then
    python3 main.py
elif [[ "$stdin" == '2' ]]; then
    cat read_me
fi