# to run this file: `sh math.sh`

expr 5 + 2
expr 5 - 2
expr 5 \* 2
expr 5 / 2

# bc stands for bench calculator, use it for more complex math
echo "22 / 7" | bc -l
echo "4.2 * 9.15" | bc -l
echo "(6.5 / 0.5) + (6 * 2.2)" | bc -l