from collections import deque

def roundrobin(*iterables):
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # remove exhausted iterators
            iterators.popleft()