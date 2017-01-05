#!/bin/bash

set -e

if [[ $# -eq 0 ]] ; then
  echo 'Please supply the solution number to run (e.g. ./run-ts.sh 1)'
  exit 1
fi

tsc --outDir typescript/bin typescript/$1.ts
node typescript/bin/$1.js
