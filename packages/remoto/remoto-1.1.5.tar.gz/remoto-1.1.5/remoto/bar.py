def foo(arg):
    return 1


if __name__ == '__channelexec__':
    for item in channel:
        channel.send(eval(item))
