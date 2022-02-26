
# NFT generator

It is what it is...


## How to use

Download the required libraries first

```
pip install -r requirements.txt
```
After this, you're good to go!

Run main.py thourgh python to start generating NFTs

```
python main.py
```

```
python3 main.py
```

Also works by just running through your editor of choice (e.g. [Atom](https://atom.io/))
## requirements.txt

numpy==1.22.2

Pillow==9.0.1

tqdm==4.62.3
## Custom commands

| -command        | --command           | Info  | Default   |
| ------------- |:-------------:| -----:| -----:|
| -h        | --help           | Shows you all the available commands  |    |
| -a      | --amount | Amount of images to generate | 10   |
| -g      | --gif      |   Creates a .gif file of all the newly generated images |  False |
| -ga | --gif_all      |    Creates a .gif file of the available images in the 'Output' folder |  False |

### Example

```
python main.py -a 8
```
-> Generates 8 new images


```
python main.py -a 25 -g
```
-> Generates 25 new images + Creates a .gif file of them


```
python main.py -a 3 -g -ga
```
-> Generates 3 new images + Creates a .gif file of them + Creates .gif file of all images in 'Output' folder