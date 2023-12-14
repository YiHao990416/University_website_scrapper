## Table of Contents
* [Project Description](#project-description)
* [Installation](#installation)
* [Usage](#usage)
* [Dependencies](#dependencies)
* [License](#license)

## Project Description
This project is used to extract Chinese text information from Taiwan university websites

## Installation

clone this github repository with the commandline below
``````
``````

## Usage
### Create files and directory required
To use this website scrapper program, please create the files and directory with the commandline below.

create folder named "output", "output_json" and "checkpoint" in the root of the folder

```
mkdir output
mkdir output_json
mkdir checkpoint
mkdir input
```

create empty .txt file named "error.txt" in the checkpoint folder.
directory: ./checkpoint/error.txt

the website information and link is stored in the form of jsonl file in input folder
directory: ./input/all_uni.json

the example format of the all_uni.jsonl files is shown below:

{"學校名稱": "國立中正大學", "網址": "http://www.ccu.edu.tw/", "abbrev": "ccu"}
{"學校名稱": "國立宜蘭大學", "網址": "https://www.niu.edu.tw/", "abbrev": "niu"}

### How to used the program
execute the program with the command below to extract all the chinese text from university website
The amount of text extracted is based on the hyperparameter which can be adjusted in the main.py

The default is set to
depth = 3
min_len = 50

```
run python main.py
```

To convert the extracted .txt files into jsonl format, execute the tools.py
```
run python tools.py
```

## Dependencies

The virtual environment is created with condaa. The dependencies is listed in requirements.txt.
To install the dependencies, use the command line below

```
pip install -r requirements.txt
```

## License
Please ensure that you follow the code of conduct and contribution guidelines when contributing to this project. License This project is licensed under the MIT License - see the LICENSE file for details







