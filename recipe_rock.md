Rock-Paper-Scissors recipe (ish)

## USER STORY ##
As a Maker
So I can play Rock Paper Scissors
I would like to enter my move on the home page
And click to confirm my move (rock, paper or scissors)

As a Maker
So I can play Rock Paper Scissors
I would like the opponent's move to be decided randomly by the program

As a Maker
So I can play Rock Paper Scissors
I would like to see the result of the game on the next page

As a Maker
So I can play Rock Paper Scissors again
I would like to click on a link on the result page
So it takes me back to the home page


## PLAYER JOURNEY ##

1) arrive on homepage (index) w/ a 'let's play' button, redirect to 'your move' page
2) asked to select a move (rock-paper-scissors)
    ^^ text input to start, maybe selectable images later
3) confirm selection, redirect to results page
4) arrive on results page + see:
    a - both moves played
    b - result/winner
    c - option to play again
5) select 'new game', redirect to homepage
6) return to refreshed homepage

# Possible additionals #
- what if multiple draws?
- extended version? (e.g. spock, lizard)

## TESTING - brain dump for now ##
- no input/confirmed without selecting move
- input incorrect move (e.g. another move, like xyz)
- try to go straight to results page (e.g. localhost:5001/result)
- DRAW!
    - ...mock?
- ...


```python

###################
### VALID TESTS ###
###################

# """ 
# Load main page
#     Expect result: able to see title of page
# """


""" 
Select a move, and submit
    ^^ just checking redirected to Results page once a move played
    Expected result: redirected to results page showing player's move
"""

"""
Computer plays a move
    - homepage, user plays, results page shows PC move
    Expected reuslt: see move stated on results page
"""


"""
Confirm PC play is random
    ^^ ...idk how...TBC!!
    Expected result: ???S
"""


"""
Winner announced!
    ^ need to test all variations (move + who plays its)
    Expected result: correct winner for each scenario
"""

"""
"It's a draw!"
    Expected result:
        - announce a draw
        - TBC a) redirect to new game, b) continue but play again...
"""


### STRETCH ###

"""
TESTS for a TALLY :D
"""



#####################
### INVALID TESTS ###
#####################


"""
No move submitted by player
    Expected result: 
        - error message/page
        - redirect to homepage? (TBC)
"""


"""
Incorrect move input + submitted
    ^^ TBC if text input
    Expected result:
        - error message/page
        - redirect to homepage? (TBC)
"""


"""
Load results page 
    ^^ e.g. goto localhost:5001/Play/Results 
    Expected Result:
        - redirect to homepage
        - error message ?? (TBC)
"""



```