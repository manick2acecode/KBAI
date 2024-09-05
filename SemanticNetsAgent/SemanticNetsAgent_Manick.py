from collections import deque


class SemanticNetsAgent_Manick:
    def __init__(self):
        pass

    def solve(self, initial_missionaries, initial_cannibals):
        class State:
            def __init__(self, left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat_position):
                self.left_missionaries = left_missionaries
                self.left_cannibals = left_cannibals
                self.right_missionaries = right_missionaries
                self.right_cannibals = right_cannibals
                self.boat_position = boat_position
                self.parent = None

            def __eq__(self, other):
                return (self.left_missionaries == other.left_missionaries and
                        self.left_cannibals == other.left_cannibals and
                        self.right_missionaries == other.right_missionaries and
                        self.right_cannibals == other.right_cannibals and
                        self.boat_position == other.boat_position)

            def __hash__(self):
                return hash((self.left_missionaries, self.left_cannibals, self.right_missionaries,
                             self.right_cannibals, self.boat_position))

            def is_goal_state(self):
                return (self.left_missionaries == 0 and self.left_cannibals == 0 and
                        self.right_missionaries == initial_missionaries and
                        self.right_cannibals == initial_cannibals and self.boat_position == "right")

            def is_valid_state(self):
                if (self.left_missionaries != 0 and self.left_cannibals > self.left_missionaries) or \
                        (self.right_missionaries != 0 and self.right_cannibals > self.right_missionaries):
                    return False
                if self.left_missionaries < 0 or self.left_cannibals < 0 or \
                        self.right_missionaries < 0 or self.right_cannibals < 0:
                    return False
                return True

        def generate_successors(curr_state):
            successors = []
            possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

            if curr_state.boat_position == "left":
                for move in possible_moves:
                    new_state = State(curr_state.left_missionaries - move[0], curr_state.left_cannibals - move[1],
                                      curr_state.right_missionaries + move[0], curr_state.right_cannibals + move[1],
                                      "right")
                    if new_state.is_valid_state():
                        new_state.parent = curr_state
                        successors.append(new_state)
            else:  # boat moves from right to left
                for move in possible_moves:
                    new_state = State(curr_state.left_missionaries + move[0], curr_state.left_cannibals + move[1],
                                      curr_state.right_missionaries - move[0], curr_state.right_cannibals - move[1],
                                      "left")
                    if new_state.is_valid_state():
                        new_state.parent = curr_state
                        successors.append(new_state)

            return successors

        def bfs():
            initial_state = State(initial_missionaries, initial_cannibals, 0, 0, "left")
            if initial_state.is_goal_state():
                return initial_state

            queue = deque([initial_state])
            explored = set()

            while queue:
                current_state = queue.popleft()
                if current_state.is_goal_state():
                    return current_state

                explored.add(current_state)

                for successor in generate_successors(current_state):
                    if successor not in explored and successor not in queue:
                        queue.append(successor)

            return None

        def reconstruct_path(state):
            path = []
            while state.parent:
                move = (abs(state.left_missionaries - state.parent.left_missionaries),
                        abs(state.left_cannibals - state.parent.left_cannibals))
                path.append(move)
                state = state.parent
            return path[::-1]

        solution = bfs()
        return reconstruct_path(solution) if solution else []
