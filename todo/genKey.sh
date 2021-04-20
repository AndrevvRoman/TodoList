#!/bin/bash
key=$(< /dev/urandom tr -dc '0-9!@$#?*+_a-zA-Z' | head -c52)
sed -i "s~.*SECRET_KEY\ =\ .*~SECRET_KEY\ =\ '${key}'~" settings.py
