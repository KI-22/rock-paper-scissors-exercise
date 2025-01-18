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

1) arrive on homepage (index) + asked to choose
2) select a move (rock-paper-scissors)
    ^^ TBC if text input OR selectable image
3) confirm selection
4) arrive on results page + see:
    a - both moves played
    b - result/winner
    c - option to play again
5) select 'new game'
6) return to refreshed homepage


## TESTING - brain dump for now ##
- no input/confirmed without selecting move
- input incorrect move (e.g. another move, like gun)
- try to go straight to results page (e.g. localhost:5001/result)
- ...