def f(*args, **kwargs):
    print("Positional:", args)
    # print("Named:", kwargs)



# f(100, 50, 25)
# f(100, 50, 25, 5)
# f(100)

values = [100, 25, 50]
f(*values)

# f(galleons=100, sickles=50, knuts=25)


# def print(*objects, sep=" ", end="\n" ...):
#     for object in objects:
#         ...
