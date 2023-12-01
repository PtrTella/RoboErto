
import numpy as np
import time 
import library as moves
from collections import Counter

#Global Variables and CONSTANTS
BRANCHING_FACTOR = 5
TIME_TOLERANCE = 20 #seconds
MAX_TREE_SIZE = 100


def moves_evaluation(node, analyzed_song, dur, song):
    INTERVAL = 2
    round_time = 0
    value = 0

    for move in node:

        round_time += move.duration
        if round_time > dur + TIME_TOLERANCE:
            return value/len(node)
        intensity = analyzed_song[int(round(round_time - move.duration/2))]

        # Valutazione in base alla mossa e all'intensità
        if move in moves.list_fast_moves:
            if intensity > song['max'] - song['mean']/INTERVAL:
                value += 1
            elif song['min'] + song['mean']/INTERVAL <= intensity <= song['max'] - song['mean']/INTERVAL:
                value += 0.5
            else:
                value += 0.2

        if move in moves.list_normal_moves:
            if song['min'] + song['mean']/INTERVAL <= intensity <= song['max'] - song['mean']/INTERVAL:
                value += 1
            else:
                value += 0.5
            
        if move in moves.list_slow_moves:
            if intensity < song['min'] + song['mean']/INTERVAL:
                value += 1
            elif song['min'] + song['mean']/INTERVAL <= intensity <= song['max'] - song['mean']/INTERVAL:
                value += 0.5
            elif intensity > song['max'] - song['mean']/INTERVAL:
                value += 0.2
        
        return value/len(node)
    

def repeat_move(node):
    # Count the overall number of repeated moves    
    item_counts = Counter(node)

    value = 1
    for item, count in item_counts.items():
        value = value/count
    
    return value
            


#Function that returns the total time-span of a solution by summating it's move durations.
def compute_time(node):
    return sum([move.duration for move in node])

# Caluclate heuristic
def heuristic(node, analyzed_song, dur, song):
    alpha, beta, gamma = 0.5, 0.25, 0.25
    
    time = compute_time(node)
    moves = moves_evaluation(node, analyzed_song, dur, song)
    duplicate = repeat_move(node)

    return (alpha*time/dur + beta*moves + gamma*duplicate), time
    

#Search algorithm:
#It expands nodes based on an Heuristic h
#h: linear combination between the normalized duration of a Solution and the normalized number of matching position included
def search(analyzed_song, dur):
    EPOCH = 1000
    epoch = 0
    song = { 'max': np.max(analyzed_song), 'min': np.min(analyzed_song), 'mean': np.mean(analyzed_song)}

    while epoch < EPOCH:
        iteration = 0
        np.random.shuffle(moves.intermediate)
        np.random.shuffle(moves.mandatory)
        best = [moves.initial, *moves.mandatory, moves.goal] #prima: mandatory_pos
        print("Starting moves:",*[x.name for x in best], sep=' >> ')
        h_best, t_best = heuristic(best, analyzed_song, dur, song)

        while iteration < MAX_TREE_SIZE:

            #Heuristic computation for each new expanded node
            best = max(expand(best), key= lambda x: heuristic(x, analyzed_song, dur, song))
            h_best, t_best = heuristic(best, analyzed_song, dur, song)
            #print(h_best, t_best)
            if t_best > dur + TIME_TOLERANCE:
                break
        
            if t_best > (dur)  and t_best < (dur + TIME_TOLERANCE) and h_best > 0.8:
                return best, t_best, h_best, iteration, epoch
            
            iteration += 1
        epoch += 1
        
    return [], 0, 0, 0, epoch 

        
#Return a list of poissible children for a given node one
def expand(node):
    list = []
    # Expand the node by adding BRANCHING_FACTOR children
    for _ in range(BRANCHING_FACTOR):
        child = expand_node(node)
        list.append(child.copy())
    # Return the best child according to the heuristic
    return list


#Function in charge of expanding selected nodes.
def expand_node(parent):
    new = parent.copy()
    while True:
        # Select random mandatory move and place after it a random non mandatory move
        post_move = np.random.choice(moves.mandatory)
        pre_move = new[new.index(post_move)-1]
        move = np.random.choice(moves.intermediate)
        #Check if the Selected non mandatory move is compatible with the one 
        if pre_move.postconditions == None or pre_move.postconditions == move.preconditions or move.preconditions == None:
            if post_move.preconditions == None or post_move.preconditions == move.postconditions or move.postconditions == None:
                new.insert(new.index(post_move), move)
        return new





def search_coreography(analyzed_song, dur):

    np.random.shuffle(moves.intermediate)
    np.random.shuffle(moves.mandatory)


    solution, time, score, it, ep = search(analyzed_song, dur)

    if solution == []:
        print("No solution found")
        print("Epochs: {:}".format(ep))
        return None
    
    else:
        print("\n\nSTATS:\n\nBest Move Sequence:")
        print(*[x.name for x in solution], sep=" ► ")
        print("\nTotal Time: {:}s".format(time))
        print("Score: {:.2f}".format(score))
        print("Iterations: {:}".format(it))
        print("Epochs: {:}".format(ep))
        return solution

