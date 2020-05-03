chapter_number=5
echo $chapter_number

# change a variable using let
let chapter_number=$chapter_number+1
echo $chapter_number

the_empire_state="New York"
echo $the_empire_state

# count number of lines in math.sh and store that to math_line variable
math_line=$(cat math.sh | wc -l)
echo $math_line

# call the variable within an echo command
echo "I went to school in $the_empire_state."
