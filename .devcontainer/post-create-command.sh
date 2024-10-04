#!/bin/bash

echo "#### post-create-command.sh: $(date) - start"

set -e

env

ME=$(basename "$0")

echo "#### post-create-command.sh: $(date) - me is $ME - pwd is $(pwd)"

sudo apt-get update

sudo apt-get install -y git-lfs

pip install --user -r requirements.ansible.txt

echo "#### post-create-command.sh: $(date) - end"
