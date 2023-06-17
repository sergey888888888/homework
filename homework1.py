def pal_detect(msg):
    msg_d = msg[::-1]
    if msg_d == msg:
        return True
    else:
        return False