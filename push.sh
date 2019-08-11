#!/bin/bash

echo '=== committing ==='
git add --all
git commit -a -m fix

echo '=== github.com ==='
git push upstream master
