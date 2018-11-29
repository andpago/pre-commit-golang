#!/bin/env bash

godoc2md $1 > $GOPATH/src/$1/README.md
