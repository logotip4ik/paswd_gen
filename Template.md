#Simple password generator
This generator is cross-platform.

##Installation
1. ```git clone https://github.com/logotip4ik/paswd_gen.git```
2. ```pip3 install pyperclip```

##Usage
####Command line
```
python3 pswdgen.py
```
This outputs random generated password length of 15 characters, digits and punctuation symbols.
####Output
```
*UV#4~xb%]3oC!8
```
* You can you specify the length of password, with digit after the main program.
```
python3 pswdgen.py 36
```
* Also you can select quiet mode. This will copy password to clipboard and wont print any output.
```
python3 pswdgen.py -q
```