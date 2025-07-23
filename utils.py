import time

last_triggered = {}

def can_trigger(gesture, cooldown=2.0):
    now = time.time()
    if gesture not in last_triggered or (now - last_triggered[gesture]) > cooldown:
        last_triggered[gesture] = now
        return True
    return False