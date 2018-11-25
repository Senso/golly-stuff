import time
from glife import rect
import golly as g
import random
random.seed()

GRID_SIZE = (16, 16)
GENS = 200

prev_world = None

def is_static():
    global prev_world

    bbox = rect(g.getrect())
    if bbox.empty:
        return False

    cur_world = g.hash(g.getrect())
    if prev_world and prev_world == cur_world:
        return True
    else:
        prev_world = cur_world

def better_randfill():
    g.new('')
    g.select([-10, -10, GRID_SIZE[0], GRID_SIZE[1]])
    g.randfill(random.randrange(50))
    g.select([])
    g.autoupdate(True)
   
    cnt = 0 
    for x in range(0,GENS):
        cnt += 1
        if not g.empty():
            g.run(1)
            if is_static():
                break
            time.sleep(0.05)
        else:
            break
        if cnt % 10 == 0:
            g.fit()

better_randfill()
