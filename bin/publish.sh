#!/bin/sh


set -e

export BIN_DIR=`dirname $0`
export PROJECT_ROOT="${BIN_DIR}/.."
. ${BIN_DIR}/common.sh
setup no


twine upload dist/freenit-* --verbose
