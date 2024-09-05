class SemanticNetsAgent:
    def __init__(self):
        self.initial_state = None

    def solve(self, initial_sheep, initial_wolves):
        self.initial_state = State.init_sem_state(initial_sheep, initial_wolves)
        to_search = [self.initial_state]
        seen_states = {self.initial_state.state_vars}
        solutions = []

        loop_count = 0
        max_loop = 10000

        while to_search and loop_count < max_loop:
            loop_count += 1

            current_state = to_search.pop()
            next_states = current_state.get_next_states(initial_sheep, initial_wolves)

            for next_state in next_states[::-1]:
                if next_state.state_vars not in seen_states:
                    if next_state.check_for_failure(initial_sheep, initial_wolves):
                        continue
                    if next_state.check_for_solution():
                        solutions.append(next_state)
                        continue

                    to_search.append(next_state)
                    seen_states.add(next_state.state_vars)

        return self.extract_solution(solutions)

    def extract_solution(self, solutions):
        if not solutions:
            return []

        optimal_solution = min(solutions, key=lambda s: s.tot_moves)
        result = []

        while optimal_solution:
            result.append(optimal_solution.move)
            optimal_solution = optimal_solution.parent

        result.reverse()
        return result[1:]


class State:
    def __init__(self, state_vars, tot_moves=0, move=(0, 0), parent=None):
        self.move = move
        self.tot_moves = tot_moves
        self.parent = parent
        self.state_vars = state_vars

    @classmethod
    def init_sem_state(cls, initial_sheep, initial_wolves):
        return cls((initial_sheep, initial_wolves, 1))

    def get_next_states(self, initial_sheep, initial_wolves):
        moves = self.ret_potential_moves()
        next_states = []
        sheep_right, wolves_right, boat_right = self.state_vars

        for move in moves:
            change_sheep, change_wolves = move
            if boat_right == 1:
                new_state_vars = (sheep_right - change_sheep, wolves_right - change_wolves, 0)
            else:
                new_state_vars = (sheep_right + change_sheep, wolves_right + change_wolves, 1)

            next_state = State(new_state_vars, self.tot_moves + 1, move, self)
            if next_state.is_move_legal(initial_sheep, initial_wolves):
                next_states.append(next_state)

        return next_states

    def is_move_legal(self, initial_sheep, initial_wolves):
        sheep, wolves, boat = self.state_vars
        if not (0 <= sheep <= initial_sheep):
            return False
        if not (0 <= wolves <= initial_wolves):
            return False
        return True

    def check_for_solution(self):
        return self.state_vars == (0, 0, 0)

    def check_for_failure(self, initial_sheep, initial_wolves):
        sheep, wolves, boat = self.state_vars

        if 0 < sheep < wolves:
            return True

        sheep_on_left = initial_sheep - sheep
        wolves_on_left = initial_wolves - wolves

        if 0 < sheep_on_left < wolves_on_left:
            return True
        return False

    def ret_potential_moves(self):
        """Return all possible moves in the problem as tuples."""
        return [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
