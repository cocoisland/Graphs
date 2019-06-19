


def countVote(input):
    '''
    input: [‘veronica’, ‘mary’, ‘alex’, ‘james’, ‘mary’, ‘michael’, ‘alex’, ‘michael’];
    '''
    
    dict={}
    max_vote = 0
    leading_candidate = ""
    for candidate in input:
        if dict[candidate] is None:
            dict[candidate] = 1
        else:
            dict[candidate] = += 1
            if dict[candidate] > max_vote :
                leading_candidate = candidate
                max_vote = dict[candidate]
            elif dict[candidate] == max_vote and dict[candidate] > leading_candidate :
                leading_candidate = dict[candidate]

    print(f'Winner is {leading_candidate}')


