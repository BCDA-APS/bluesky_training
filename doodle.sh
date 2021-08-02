#!/bin/bash

echo $(date): Doodle demonstration starting
echo $(date): sleep 5 seconds
for i in 5 4 3 2 1; do
    echo $(date): countdown ${i}
    sleep 1
done
echo $(date): Doodle demonstration complete
