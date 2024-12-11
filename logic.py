import random


class Node:

    def __init__(self, left, operator, right):
        self.operator = operator
        self.right = right
        self.left = left

    def __repr__(self):

        if len(str(self.left)) == 1:
            left_str = self.left
        else:
            left_str = f'({self.left})'
            
        if len(str(self.right)) == 1:
            right_str = self.right
        else:
            right_str = f'({self.right})'

        return f'{left_str} {self.operator} {right_str}'



def random_simple_expr(variables, repeat_variables=False, not_percentage=50):

    X = random.choice(variables) 
    Y = random.choice(variables)

    if not repeat_variables:
        while X == Y:
            X = random.choice(variables) 
            Y = random.choice(variables)    

    if random.random()*100 < not_percentage:
        X = f'not {X}'

    if random.random()*100 < not_percentage:
        Y = f'not {Y}'
    
    return Node(X, random.choice(operators), Y)



def generate_expr(variables, expr, iterations, branching_percentage=50, repeat_variables=False, not_percentage=50):

    if iterations > 0 and random.random()*100 < branching_percentage:

        expr.left = random_simple_expr(variables, repeat_variables, not_percentage)
        expr.left = generate_expr(
            variables,
            expr.left,
            iterations-1,
            branching_percentage,
            repeat_variables,
            not_percentage 
        )

    if iterations > 0 and random.random()*100 < branching_percentage:

        expr.right = random_simple_expr(variables, repeat_variables, not_percentage)
        expr.right = generate_expr(
                variables,
                expr.right,
                iterations-1,
                branching_percentage,
                repeat_variables,
                not_percentage
        )

    return expr



def print_tree(node, prefix="", is_left=True):
    if type(node) != str:
        if node.left or node.right:
            # Print the current node
            connector = "├─" if is_left else "└─"
            print(prefix + connector + str(node.operator))

            # Adjust prefix for children
            new_prefix = prefix + ("│ " if is_left else "  ")

            # Recurse for left and right children
            print_tree(node.left, new_prefix, is_left=True)
            print_tree(node.right, new_prefix, is_left=False)



if __name__ == '__main__':

    variables_number = 2
    repeat_variables = False
    not_percentage = 40
    branching_percentage = 80
    iterations = 2
    
    operators = ['and', 'or', 'implies', 'iff']
    variables = list('ABCDEFGHIJKMNOPQRSTUVWXYZ')[:variables_number]

    expr = generate_expr(
            variables,
            random_simple_expr(variables, repeat_variables, not_percentage),
            iterations,
            branching_percentage,
            repeat_variables,
            not_percentage,
            )

    print(expr)
    print_tree(expr)
