import random


class Node:

    def __init__(self, left, operator, right):
        self.operator = operator
        self.right = right
        self.left = left

    def __repr__(self, is_root=False):
        if is_root:
            return f'{self.left} {self.operator} {self.right}'
        else:
            return f'({self.left} {self.operator} {self.right})'


def random_simple_expr(operators, variables, repeat_variables=False, not_percentage=50, not_op='not'):

    X = random.choice(variables) 
    Y = random.choice(variables)

    if not repeat_variables:
        while X == Y:
            X = random.choice(variables) 
            Y = random.choice(variables)

    if random.random()*100 < not_percentage:
        X = f'{not_op} {X}'

    if random.random()*100 < not_percentage:
        Y = f'{not_op} {Y}'
    
    return Node(X, random.choice(operators), Y)



def generate_expr(operators, variables, expr, iterations, branching_percentage=50, repeat_variables=False, not_percentage=50, not_op='not'):

    if iterations > 0 and random.random()*100 < branching_percentage:

        base_expr = random_simple_expr(operators, variables, repeat_variables, not_percentage, not_op)
        negated = (random.random()*100 < not_percentage)*f'{not_op} '
        expr.left = negated +str(generate_expr(
            operators,
            variables,
            base_expr,
            iterations-1,
            branching_percentage,
            repeat_variables,
            not_percentage,
            not_op,
        ))

    if iterations > 0 and random.random()*100 < branching_percentage:

        base_expr = random_simple_expr(operators, variables, repeat_variables, not_percentage, not_op)
        negated = (random.random()*100 < not_percentage)*f'{not_op} '
        expr.right = negated +str(generate_expr(
            operators,
            variables,
            base_expr,
            iterations-1,
            branching_percentage,
            repeat_variables,
            not_percentage,
            not_op,
        ))

    return expr


from print_tree import print_tree

if __name__ == '__main__':

    variables_number = 10
    
    repeat_variables = False
    not_percentage = 30
    branching_percentage = 70
    branching_iterations = 2
    number_of_expr = 30

    operators = [r'\land', r'\lor', r'\implies', r'\iff']
    not_op = r'\neg'
    
    variables = list('ABCDEFGHIJKMNOPQRSTUVWXYZ')[:variables_number]

    with open('expressions.md', 'w') as f:
        f.write('')

    for _ in range(number_of_expr):
        base_expr = random_simple_expr(operators, variables, repeat_variables, not_percentage, not_op)
        expr = generate_expr(
            operators,
            variables,
            base_expr,
            branching_iterations,
            branching_percentage,
            repeat_variables,
            not_percentage,
            not_op,
        )

        with open('expressions.md', 'a') as f:
            f.write(f'- ${expr}$\n')
