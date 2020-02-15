import search

class RouteSearchProblem(search.SearchProblem):
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.
    """

    def __init__(self, map, costFn = lambda x: 1, goal, start):
        """
        Stores the start and goal.
        gameState: A GameState object 
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.startState = start
        self.goal = goal
        self.map = map
        self.costFn = costFn

        # For display purposes
        #self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def getStartState(self):

    def goalTest(self, state):

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """
        
    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """

    def getCost(self, state, action):
        """
        Given a state and an action, returns associated cost, which is
        the incremental cost of expanding to that successor.
        """

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions. If those actions
        include an illegal move, return 999999.
        """
def MaxHeuristic:
    return 1

prob = RouteSearchProblem(map, start=, goal=)
search.astar(prob, MaxHeuristic)