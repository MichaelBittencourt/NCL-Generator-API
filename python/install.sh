#!/bin/bash
#
# install.sh
# Copyright (C) 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.
#

if test -n "$1" 
then
    cp -r ncl $($1 -m site --user-site)
else
    echo "
    execute:
        $0 <YOUR_PYTHON3_COMMAND>
    Eg:
        $0 python3"
fi


