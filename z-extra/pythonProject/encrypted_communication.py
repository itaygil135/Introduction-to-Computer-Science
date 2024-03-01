
def weave_strings(str1, str2, str3):
    result = ''
    devision = len(str3)
    for i in range(devision):
        result += str1[i] + str2[i] + str3[i]
    result += str1[devision:] + str2[devision:] + str3[devision:]
    return result


def encode(msg):
    # TODO implement
    return


def decode(enc_msg):
    # TODO implement
    return weave_strings(str1, str2, str3)


if __name__ == '__main__':
    msg = 'Hi Bob, I am here'
    enc_msg = encode(msg)
    dec_msg = decode(enc_msg)
    if msg == dec_msg:
        print("Success")
    else:
        print("Failure: Decrypted message is not equal to the original message.")