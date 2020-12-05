# <h1> Tic-Tac-Toe User Documentation Manual </h1>
<h5> Project built using Python </h5>
<h5> Project By: Katrina Curro </h5>

--------
# <h2> Project goal: implement different agents who can play a tic-tac-toe game </h2>
<h5> The project uses 4 different agents: Random Agent, Basic Strategy Agent, Minimax Agent, 
and Minimax Agent with Alpha Beta Pruning </h5>
<h5> The agents can be played on 3 different board sizes: small 3x3, medium 4x4, large 5x5. </h5>

--------
<h5> The Random Agent will choose a tic-tac-toe location by random on the grid. This agent 
  does not use any game winning algorithm to help them along. </h5>
<h5> The Basic Strategy Agent will play the corners of the tic-tac-toe grid first then 
  choose random positions. </h5>
<h5> The Minimax Agent will use minimax game trees to help agent choose the optimal move. </h5>
<h5> The Minimax Agent with Alpha Beta Pruning will use the minimax with alpha beta pruning 
  algorithm to help agent choose the optimal move. </h5>

--------
<h5> The opponent to each of these agents will be played using the Random Agent method. </h5>
<h5> Each file is structured as a combination of agent method used and board type allowing the user
to decide what game they want to run. </h5>
<h6> For example, the RandomAgentSmallBoard.py is a combination of the Random Agent method
and the small board of size 3x3. </h6>

--------
<h5> As a constant the agent will always make the first move. </h5>
<h5> To win on the small board the agent must have 3 of its symbols in a row. </h5>
<h5> To win on the medium board the agent must have 4 of its symbols in a row. </h5>
<h5> To win on the large board the agent must have 5 of its symbols in a row. </h5>
<h5> The project also allows users to calculate the total run time of the program and
the number of nodes the program (agent and opponent) extends. </h5>

--------
# <h1> To run this project, install it locally using: </h1>

```
$ git clone TicTacToe_Final
```

<h5> Depending on what agent and board combination you want to use, run
  one of the files using the command: </h5>
  
```
$ python RandomAgentSmallBoard.py

$ python RandomAgentMediumBoard.py

$ python RandomAgentLargeBoard.py

$ python BasicAgentSmallBoard.py

$ python BasicAgentMediumBoard.py

$ python BasicAgentLargeBoard.py

$ python MinimaxAgentSmallBoard.py

$ python MinimaxAgentMediumBoard.py

$ python MinimaxAgentLargeBoard.py

$ python AlphaBetaSmallBoard.py

$ python AlphaBetaMediumBoard.py

$ python AlphaBetaLargeBoard.py
```

