#keyword arguments
# clean_name(last_name="   smith   ", first_name="   jane   ")

# # calculate the number of values
# def count_values(*args):
#     print(len(args))
#     print(sum(args))
#     print(f"Number of positional arguments: {len(args)}")


# count_values(1, 2, 3)

#create user profile
def create_user(**kwargs):
    print(type(kwargs))

create_user()