#!/usr/bin/env python3
# https://adventofcode.com/2022/day/19

print('---------------------- VERY SLOW SOLUTION ----------------------')
print('Completing computation for both parts took ~1.5h on gen 6 i7 CPU')
print('----------------------------------------------------------------')

import re, math

blueprints = []
with open('i.txt', 'r') as f:
    for line in f.readlines():
        nums = re.findall(r'\d+', line)
        blueprints.append(((int(nums[1]), 0, 0, 0),\
                (int(nums[2]), 0, 0, 0),\
                (int(nums[3]), int(nums[4]), 0, 0),\
                (int(nums[5]), 0, int(nums[6]), 0)))

MINUTES = 24 

ORE = 0
CLAY = 1
OBSI = 2
GEO = 3

max_geos = 0 
CACHE = {}


def get_available(robots, costs):
    av = []
    #print(costs)
    if robots[2] > 0: 
        av.append(GEO)
    if robots[1] > 0 and robots[2] < costs[2]:
        av.append(OBSI) 
    if robots[1] < costs[1]:
        av.append(CLAY)
    if robots[0] < costs[0]:
        av.append(ORE)
    return av


def can_buy(resources, cost):
    after = list(map(lambda x,y: x-y, resources, cost))
    return all(x>=0 for x in after), after


def should_stop(minute, resources, robots):
    global max_geos
    n = MINUTES - minute
    max_prediction = resources[-1] * (n+1) + (n * (n + 1) // 2)
    if max_prediction < max_geos:
        #print('just stop')
        return True
    return False


def trash_surplus(resources, max_costs):
    rsc = [0,0,0,0]
    for idx in range(2):
        rsc[idx] = min(resources[idx], max_costs[idx])
    rsc[3] = resources[3]
    return tuple(resources)


def work(minute, robots, resources, sequent, costs, max_costs):
    global max_geos

    if robots==max_costs:
        print('robots==max_costs')
        n = MINUTES - minute
        return resources[-1] * (n+1) + (n * (n + 1) // 2)

    if (minute, robots, resources) in CACHE:
        return CACHE[(minute, robots, resources)]

    # TODO maybe a good idea but requires further analysis    
    # predict end result taking that we are able to produce 
    # one obsidian gatherer per round till the end of time
    #if should_stop(minute, resources, robots):
    #    return '-1'
    
    if minute == MINUTES:
        CACHE[(minute, robots, resources)] = resources[-1]
        max_geos = max(resources[-1], max_geos)
        return resources[-1]


    # handle transaction 
    # TODO is it possible to buy multiple robots in one round?
    ordered_robots = [0, 0, 0, 0]
    bought, after_paying = can_buy(resources, costs[sequent])
    if bought:
        ordered_robots[sequent] += 1
        resources = after_paying

    # dig, update resources
    resources = tuple(map(lambda x,y: x+y, resources, robots)) 
    resources = trash_surplus(resources, max_costs)

    # pick up newly purchased robots
    robots = tuple(map(lambda x,y: x+y, robots, ordered_robots))
    
    if bought:
        for sequent in get_available(robots, max_costs):
            ret = work(minute+1, robots, resources, sequent, costs, max_costs)
            CACHE[(minute, robots, resources)] = ret
    else:
        ret = work(minute+1, robots, resources, sequent, costs, max_costs)
        CACHE[(minute, robots, resources)] = ret

    return max_geos


def get_max_costs(blueprint):
    max_costs = []
    for idx in range(len(blueprint)):
        max_costs.append(max(m[idx] for m in bp))
    return tuple(max_costs)


def analyze_blueprint(blueprint):
    global max_geos
    
    max_geos = 0
    robots = (1, 0, 0, 0)
    resources = (0, 0, 0, 0)

    max_costs = get_max_costs(blueprint)
    for sequent in get_available(robots, max_costs):
        work(0, robots, resources, sequent, blueprint, max_costs) 
    return max_geos

qualities = []
for i, bp in enumerate(blueprints,1):
    CACHE = {}

    bp_max = analyze_blueprint(bp)
    print(f'Finished analyzing {i}/{len(blueprints)}')
    qualities.append(i*bp_max)
print('p1:', sum(qualities))


### p2 ###
MINUTES = 32
blueprints = blueprints[:3]
best_geos = []
for i, bp in enumerate(blueprints,1):
    CACHE = {}

    bp_max = analyze_blueprint(bp)
    print(f'Finished analyzing {i}/{len(blueprints)}')
    best_geos.append(bp_max)
print('p2:', math.prod(best_geos))
