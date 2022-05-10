print(
    "Your randomly generated password was: "
    + str(
        "".join(
            sorted(
                list(
                    filter(
                        lambda char: char not in "\"'&`|\\^",
                        __import__("string").printable.split()[0],
                    )
                ),
                key=lambda x: __import__("random").random(),
            )
        )[0 : int(input("What is the desired length of the password? "))]
    )
)
