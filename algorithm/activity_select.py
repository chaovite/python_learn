"""implement a greedy algorithm to select activities"""

def act_sel(start, finish):
    acts = zip(start, finish)
    # sort the activities with ascending finish time
    acts = sorted(acts, key=lambda act: act[1])
    select  = []
    print(acts[0])
    last_finish = acts[0][1]
    select.append(acts.pop(0))

    for act in acts:
        st = act[0]
        fi = act[1]
        if st >= last_finish:
            print(act)
            last_finish = fi
    return act_sel

start1  = [10, 12, 20]
finish1 = [20, 25, 30]

start2  = [1, 3, 0, 5, 8, 5]
finish2 = [2, 4, 6, 7 ,9, 9]
sel1    = act_sel(start1, finish1)
sel2    = act_sel(start2, finish2)
