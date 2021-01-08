# Tennis kata
===========

Tennis has a rather quirky scoring system, and to newcomers it can be a little difficult to keep track of. The Tennis Society has contracted you to build a scoreboard to display the current score during tennis games. The umpire will have a handset with two buttons labelled "player 1 scores" and "player 2 scores", which he or she will press when the respective players score a point. When this happens, a big scoreboard display should update to show the current score. (When you first switch on the scoreboard, both players are assumed to have no points). When one of the players has won, the scoreboard should display which one.

Your task is to write a "TennisGame" class containing the logic which outputs the correct score as a string for display on the scoreboard. You can assume that the umpire pressing the button “player 1 scores” will result in a method wonPoint("player1") being called on your class, and similarly wonPoint("player2") for the other button.

Afterwards, you will get a call "getScore()" from the scoreboard asking what it should display. This method should return a string with the current score. (Note: do modify the method names to match the idiom for your programming language)

You can read more about Tennis scores is summarized below:

1.  A game is won by the first player to have won at least four points in total and at least two points more than the opponent. The score is then "Win for player1" or "Win for player2"

2.  The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "Love", "Fifteen", "Thirty", and "Forty" respectively.

3.  If at least three points have been scored by each player, and the scores are equal, the score is “Deuce.

4.  If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is “Advantage player1” or “Advantage player2.

The Tennis Society has agreed that Sets and Matches are out of scope, so you only need to report the score for the current game. However, they have requested another feature with lower priority. 

They want to be able to change the name of the players from "player1" to "Björn Borg" and "player2" to "John McEnroe". This feature has been categorized “Nice to have, or, more accurately, "in your dreams"!