for botchoice in sorted(
    ([["Rock", "s", "p"], ["Paper", "r", "s"], ["Scissors", "p", "r"]]) * 1000,
    key=lambda k: (x := __import__("random").random()) * (10 * x),
):
    print(
        "You lost! I chose " + botchoice[0]
        if (x := input("Rock, Paper or Scissors? ").lower()[0]) == botchoice[1]
        else (
            "You win! I chose " + botchoice[0]
            if x == botchoice[2]
            else (
                "Draw! I chose " + botchoice[0]
                if x == botchoice[0].lower()[0]
                else ("Incorrect choice! I chose " + botchoice[0] + ", you chose " + x)
            )
        )
    )
