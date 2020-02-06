# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # Start: (5, 5)
    #
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # Start 's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    #
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())

    visit = []
    path = []
    stack = util.Stack()
    state = problem.getStartState()

    start = (problem.getStartState(), path)
    stack.push(start)

    while True:

        if stack.isEmpty():
            return "Fail!!!"


        # pop - flag visited - add successors
        state, path = stack.pop()

        if problem.isGoalState(state):
            return path

        if state not in visit:
            visit.append(state)

            for successor in problem.getSuccessors(state):
                path_ = path + [successor[1]]  # str to list & append to list
                # print "path_",path_
                # print path
                stack.push((successor[0], path_))


    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    visit = []
    path = []
    queue = util.Queue()
    state = problem.getStartState()

    start = (problem.getStartState(), path)
    queue.push(start)

    while True:

        if queue.isEmpty():
            return "Fail!!!"

        # pop - flag visited - add successors
        state, path = queue.pop()

        if problem.isGoalState(state):
            return path

        if state not in visit:
            visit.append(state)

            for successor in problem.getSuccessors(state):
                #if successor[0] not in visit:
                path_ = path + [successor[1]]  # str to list & append to list
                queue.push((successor[0], path_))


    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visit = []
    path = []
    priority = 0
    priorityQueue = util.PriorityQueue()
    state = problem.getStartState()

    # priorityQueue: push(item,priority)
    #                pop(item)
    start = (problem.getStartState(), path)
    priorityQueue.push(start, priority)


    while True:

        if priorityQueue.isEmpty():
            return "Fail!!!"

        if problem.isGoalState(state):
            return path

        # pop - flag visited - add successors
        state, path = priorityQueue.pop()
        visit.append(state)

        for successor in problem.getSuccessors(state):
            if successor[0] not in visit:
                path_ = path + [successor[1]]
                priority_ = problem.getCostOfActions(path_)
                priorityQueue.push((successor[0], path_), priority_)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visit = []
    path = []
    priority = 0
    priorityQueue = util.PriorityQueue()
    state = problem.getStartState()

    # priorityQueue: push(item,priority)
    #                pop(item)
    start = (problem.getStartState(), path)
    priorityQueue.push(start, priority)

    while True:

        if priorityQueue.isEmpty():
            return "Fail!!!"

        if problem.isGoalState(state):
            return path

        # pop - flag visited - add successors
        state, path = priorityQueue.pop()
        visit.append(state)

        for successor in problem.getSuccessors(state):
            if successor[0] not in visit:
                path_ = path + [successor[1]]
                priority_ = problem.getCostOfActions(path_) + heuristic(successor[0],problem)
                priorityQueue.push((successor[0], path_), priority_)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
