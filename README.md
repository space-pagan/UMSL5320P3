# UMSL5320P2
Project 2 of Genetic Algs at UMSL, written by Zoya Samsonov on April 18, 2019.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

[Python 3](https://www.python.org/downloads/release/python-373/)

numpy
```
pip install numpy
```

### Installing

Simply clone the project to your desired directory

```
git clone https://github.com/space-pagan/UMSL5320P2.git
```

## Running the GA

Running driver.py will run the GA with default parameters. All parameters are
optional and are set to default values if not provided.
```
#single run using RWS, p_sample, single_point, gaussian
driver.py
```

### Parameters

driver.py takes a maximum of 5 parameters:
```
driver.py multi_run dmethod smethod cmethod mmethod
```

#### multi_run
The number of runs to perform and collect data on.
* can be any numerical value, but is converted to an integer.
* multi_run < 1 results in only a single run of the GA.

#### dmethod
The distribution method to use. Defaults to RWS.
* 'RWS' - Roulette Wheel Selection. Use with smethod = 'p_sample'
* 'rank' - Rank selection as controlled by rank_min. Use with smethod = 'p_sample'
* 'truncate' - Discard the worst n individuals as controlled by loss. No proportional value is calculated, only use with smethod = 'tournament'
* '*' - any string not listed above will not perform distribution, and therefore not calculate a p value. Use only with smethod = 'tournament'

#### smethod
The sampling method to use. Defaults to p_sample.
* 'tournament' - tournament sampling with two random individuals.
* 'p_sample' - proportional sampling using calculated p values. Only works with distribution methods RWS and rank.

#### cmethod
The crossover method to use. Defaults to single_point.
* 'single_point' - Crossover point randomly selected
* 'two_point' - Two crossover points randomly selected.
* 'arithmatic' - ax1 + (1-a)y1 where a is controlled by global variable 'weight'.

#### mmethod
The mutation method to use. Defaults to gaussian.
* 'gaussian' - x = x + gaussian(0, std)
* 'uniform' - sets x to a unifrom random value from x_min to x_max.

## Authors

* **Zoya Samsonov** - *Initial work* - [space-pagan](https://github.com/space-pagan)

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details