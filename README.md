<h1>Haunted House</h1>
<h2>Scenario</h2>
<p>
  A long haunted house consisting of two columns of N rooms has had some, unfortunate, budget cuts. As the scare master, you must close off K rooms to stay in the new budget. 
  Each room has a scary score, and you must close off K rooms while maximizing the scary factor of a path through the entire haunted house.  
  That means you cannot close off two rooms on the same level, and diagonal movement is not permitted. A path can move to the next level, left, or right. 
</p>
<h2>Solution</h2>
<h3>Recursive</h3>
<p>
  The problem can be solved recursively by considering three possibilities at each level: closing the left room, closing the right room, or leaving both rooms open. 
  If the algorithm reaches the end of the haunted house it returns a sentinel value if the number of closed doors is not exactly K.
  At each recursive step, return the maximum result among the decisions that can be made plus the score of the rooms currently in the path. 
  If the path came from the right, it cannot recurse on the left, only both or right. If the path came from the left, only recurse on the left or both. 
  If the path came from both rooms, then recurse on all three decisions. 
</p>
<h3>Dynamic Programming</h3>
<p>
  The recursive solution can be optimized using memoization, storing previously calculated results to avoid redundant recursive calls.
  The memoization structure uses a 3d array which stores the current level, number of rooms closed, and which room was previously closed if any. 
</p>
<h2>Inputs</h2>
<p1>
  Both the dynamic and recursive solutions take the same inputs. States can be read from a file, or entered manually, chosen by the Boolean, "load_from_file."
  Which test case is loaded is defined as the string passed to "load_test_case."
</p1>
<p>
  Manually, the first input contains two integers, N and K, where 3&#8804;N&#8804;200 gives the number of rows, and 0&#8804;K&#8804;N gives the number of rooms that must be     closed off. 
  This is followed by N rows of two integers, giving the scare factor of the two rooms in that row. 
</p>
<p>
  Solutions are found in the "Expected_Outputs.txt" 
</p>
