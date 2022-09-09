import datetime
from calendar import monthrange
from random import randrange
from itertools import chain
from functools import reduce

def maximum_plays(dataset: list) -> int:
    """
    Calculates the maximum number of concurrent plays in a given dataset
    
    Parameter:  dataset, list[dict]
                where each dictionary is of the form: {start: datetime.datetime, end: datetime.datetime}
                (more details in the README)
    
    Returns:    maximum number of concurrent plays, int    
    """
    
    # If an empty dataset is passed to the method
    if len(dataset) == 0:
        return 0
    
    # Step 1) list[dict] -> list[tuple[tuple]], e.g
    #         [{start: 16-02-2022 22:55:00, end: 17-02-2022 01:50:00}, ...] -> 
    #         [((16-02-2022 22:55:00, 1), (17-02-2022 01:50:00, -1)), ...]
    #
    #         Where tuple[1] = 1 if it's a start time and -1 if it's an end time
    #
    # Step 2) Unpack and chain
    #         [(16-02-2022 22:55:00, 1), (17-02-2022 01:50:00, -1), ...]
    
    unpacked_iter = chain(*(((play["start"], 1), (play["end"], -1)) for play in dataset))
    
    # Sorting the tuples in the list by the datetime
    sorted_plays = sorted(unpacked_iter)

    # At this point we have a sorted list of tuples consisting of a datetime and an integer
    # By sorting them we have constructed a timeline so to speak
    # Iterating over them we can maintain a count to determine the concurrent plays
    # We then add 1 every time we encounter a start time and -1 off the count every time a play is ended
    # The function below does this 
    
    def f(state, play):
        state.append(state[-1] + play[1])
        return state

    # The reduce operation here produces a list of the running total
    # Max of that gives us the maximum concurrent runs in the dataset
    max_intersect = max(reduce(f, sorted_plays, [0]))

    return max_intersect