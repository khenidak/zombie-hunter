# Zombie Hunter

Simulate zombie process and kill them.

## Steps
```
#compile the maker

cd maker
gcc -Wall main.c -o zombie-maker

# run it
./zombie-maker # creates 1000 zombies (for 2 max of 120 sec)

# run the hunter
cd hunter
./hunter.py

# optionaly filter using username or process (x contains('Z_HUNTER_PROCESS_NAME'))
Z_HUNTER_PROCESS_NAME='bad-process' Z_HUNTER_USERNAME='kal' ./hunter.py 
```
