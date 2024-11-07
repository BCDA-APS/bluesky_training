#!/bin/bash

echo $(date): Doodle demonstration starting

# optional argument is number of seconds to sleep, default is 5
counter=${1:-5}

until [ $counter -eq 0 ]; do
    echo $(date): countdown ${counter}
    sleep 1
    ((counter--))
done
echo $(date): Doodle demonstration complete
