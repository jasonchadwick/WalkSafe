import search

weight = 1

class RouteSearchProblem(search.SearchProblem):
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.
    """

    def __init__(self, map, costFn, goal, start):
        """
        Stores the start and goal.
        gameState: A GameState object 
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        State: can be anything as long as we are consistant (longitude, latitude)
        Map: how we store the map (dictionary w/ state keys and set values)
        """
        self.startState = start
        self.goal = goal
        self.map = map
        self.costFn = costFn

        # For display purposes
        #self._visited, self._visitedlist, self._expanded = {}, [], 0 # DO NOT CHANGE

    def getStartState(self):
        return self.startState

    def goalTest(self, state):
        isGoal = state == self.goal
        return isGoal

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """
        return self.map.get(state)
        
    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """

    def getCost(self, state, action):
        """
        Given a state and an action, returns associated cost, which is
        the incremental cost of expanding to that successor.
        """
        distance = util.getDist(state[0], action[0])
        safety = action[1]
        return distance + (safety * weight)

    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions. If those actions
        include an illegal move, return 999999.
        """
def MaxHeuristic(state, problem):
    return util.getDist(state, problem.goal)

prob = RouteSearchProblem(map, start=, goal=)
search.astar(prob, MaxHeuristic)