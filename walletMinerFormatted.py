(
    input("[\033[1;33mINFO\033[0m] - Press to start mining!\n")
    + str(
        [
            str(
                print(
                    "\n".join(
                        [
                            (
                                ("[\033[1;31mINVALID\033[0m]\033[1;31m ")
                                + __import__("random").choice(["1", "bc1", "3"])
                                + __import__("secrets").token_hex()
                                + "\033[0m"
                                + " - 0 BTC"
                            )
                        ]
                    )
                    + str(__import__("time").sleep(0.01))[:-4]
                )
            )[:-4]
            for _ in range(__import__("random").randrange(100, 1000))
        ].clear()
    )
    + str(
        print(
            ("[\033[1;32mVALID\033[0m]\033[1;32m ")
            + __import__("random").choice(["1", "3", "bc1"])
            + __import__("secrets").token_hex()
            + "\033[0m"
            + " - "
            + str(__import__("random").uniform(0.001, 2.0))
            + " BTC"
        )
    )[:-4]
)
