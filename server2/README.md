## rules

def group - cards in ascending order that are next to each other on one stack

def hole - empty space between two stack of cards

rules:

1. every player gets one card color
2. in each move player can:

    a. place card from hand on a new or existing stack

    b. move one or group of cards on stack next to it

3. there cant be a "hole" between stacks
4. card or groups can be placed only on a lower valued card or group
5. group sum value of its cards
6. if after picking up part of a group, card or group under left part have lower value its illegal (same result as in rule 4.)
7. first person that will have eplty hand and J Q K A at tops of their stacks wins
8. values of cards are same as their number, with $J=11,Q=12,K=13,A=14$

## notation

### cards

card is `AB` where `A=2..=14` is its value and `B=0..=3` is its color

*we add 0 before values 2..9 for better looking stacks*

examples
- 3 kier is `030`
- A trefl is `142`

### state of game

exaple state in 2 player game

```
030 021 091
040     120
081
```

### move

move is `A-B` where `A` is card / lowest card in group that we move  and `B` is card on which we place card `A`

examples

1. card move `081-120` is change like this

```
030 021 091
040     120
081
```
```
030 021 091
040     120
        081
```

2. group move `081-120` is change like this

```
030 021 091
040     120
081
121
```
```
030 021 091
040     120
        081
        121
```