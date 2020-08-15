# Challenge

This challenge is divided into 5 iterations.

## Installation

* Install python 
* Install docker

## Usage

### iteration 1

```
python <script> <target>
python iteration_1.py 127.0.0.1

```

### iteration 2

```
Clarification: The interpreter implementation in CPython is not thread-safe. Equally I used the threading library
               


python <script> <threads_cant> <target>

python iteration_2.py 3 127.0.0.1
```

### iteration 3

```
python <script> <threads_cant> <flagFirewall> <target>

python iteration_3.py 3 f 127.0.0.1
python iteration_3.py 4 -f 127.0.0.1
```

### iteration 4

```
python <script> <threads_cant> <flagFirewall> <target>

python iteration_4.py 3 f 127.0.0.1
python iteration_4.py 4 -f 127.0.0.1
```

### iteration 5

```
First:
Setup: dockerfile (In this file you can configure the script to run)
    * Run in terminal: docker build -t docker-iteration-5 .
    * Run in terminal: run -e TARGET=<target> docker-iteration-5
Existing problems in this iteration: Cannot set the expose port in image docker
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)