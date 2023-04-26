# def log(*values, decor="-", **kwargs):
def log(*values, **kwargs):
    # """ def log_test(**kwargs):
    # print(kwargs)
    # log_test(name="John", age=30) """

    """Utility function for logging"""

    # if "padding" not in kwargs:
    #     kwargs["padding"] = "2"
    kwargs.setdefault("padding", 2)
    # if "end" not in kwargs:
    #     kwargs["end"] = "\n"
    kwargs.setdefault("end", "\n")
    # if "decor" not in kwargs:
    #     kwargs["decor"] = "-"
    kwargs.setdefault("decor", "-")

    for val in values:
        val = str(val)
        len_val = len(val)
        prefix1 = kwargs["decor"]*kwargs["padding"] + kwargs["decor"]*len_val + kwargs["decor"]*kwargs["padding"]
        # prefix2 = "--" + "-"*len_val + "--"
        
        print(prefix1)
        print(kwargs["decor"] * (kwargs["padding"] - 1) + " " + str(val) + " " + kwargs["decor"] * (kwargs["padding"] - 1))
        print(prefix1, end=kwargs["end"])

    # return log

# log("hello")
# log(decor="#" , val="hello")
# log(1,2,3, decor="§", padding=6, end="\n\n")
#tests

if __name__ == "__main__":

    log(0, 1, end="\n\n")
    log(0, decor="#", padding=3)



