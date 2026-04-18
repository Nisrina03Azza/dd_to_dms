# Get degree in absolute format
def get_degree(a):
    return int(abs(a))

# Get minute in absolute format
def get_minutes(a):
    abs_degree = abs(a)
    degree = int(abs_degree) 
    minutes = (abs_degree-degree)*60
    return int(minutes)

# Get second in absolute format
def get_second(a):  
    abs_degree = abs(a)
    degree = int(abs_degree)
    remainder_minutes = (abs_degree-degree)*60
    minutes = int(remainder_minutes)
    second = float((remainder_minutes-minutes)*60)
    # 2 digit decimal
    return f"{abs(second):.2f}"

# Get pole for the longitude, E for east meridian, W for west meridian
def get_longpole(a):
    longpole = 'E' if a >= 0 else 'W'
    return f"{longpole}"

# Get pole for the latitude, N for north equator, S for south equator
def get_latpole(a):
    latpole = 'N' if a >= 0 else 'S'
    return f"{latpole}"

