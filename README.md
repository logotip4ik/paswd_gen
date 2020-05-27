# Simple Python password generator

This generator is cross-platform

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyperclip.

* ```pip install pyperclip```
* ```git clone https://github.com/logotip4ik/paswd_gen.git```

## Usage

```bash
python3 pswdgen.py
```
This outputs random generated password length of 15 characters, digits and punctuation symbols.

* You can specify length of password, simply adding digit after name of program, like that:
```bash
python3 pswdgen.py 30
```
* Also you can select quiet mode, with `-q` or `--quiet`. This will copy password to clipboard and wont print anything.
```bash
python3 pswdgen.py -q
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
