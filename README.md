# P3
Project 3 of [REDACTED], written by Zoya Samsonov on April 30, 2019.


By default, this project tries to solve the 1-0 Knapsack problem with the following parameters (W=50):

| Weights | Values | Best Possible |
|:-------:|:------:|:-------------:|
| 1       | 18     | 1             |
| 1       | 29     | 1             |
| 2       | 7      | 1             |
| 2       | 2      | 1             |
| 3       | 6      | 0             |
| 4       | 15     | 1             |
| 4       | 25     | 1             |
| 4       | 21     | 1             |
| 4       | 14     | 1             |
| 5       | 19     | 1             |
| 5       | 3      | 0             |
| 7       | 16     | 1             |
| 7       | 28     | 1             |
| 8       | 9      | 0             |
| 8       | 1      | 0             |
| 8       | 10     | 0             |
| 9       | 17     | 0             |
| 9       | 27     | 1             |
| 10      | 11     | 0             |
| 10      | 12     | 0             |

The best possible solution has a total weight of 50 and a total value of 221 per the above chart.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

[Python 3](https://www.python.org/downloads/release/python-373/)

### Installing

Simply clone the project to your desired directory

```
git clone https://github.com/space-pagan/EVOP3.git
```

## Running the GA

Running driver.py will run the GA with default parameters. All parameters are
optional and are set to default values if not provided.
```
#single run using rank, p_sample, single_point, uniform
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
* ~~'arithmetic'~~ - arithmetic crossover is impossible with a binary encoded GA

#### mmethod
The mutation method to use. Defaults to uniform.
* ~~'gaussian'~~ - gaussian mutation is impossible with a binary encoded GA
* 'uniform' - sets x to a random binary digit

## Authors

* **Zoya Samsonov** - *Initial work* - [space-pagan](https://github.com/space-pagan)

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details
