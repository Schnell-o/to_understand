try_it = 3

def main():
    try:
        to_understand()
        try:
            to_understand()
            try:
                try:
                    try:
                        to_understand()
                    except:
                        raise Hand()
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        print("He's a magic man.")

def to_understand():
    if try_it == 0:
        raise Hand('Try to understand...')
    try_it -= 1

if __name__ == "__main__":
    main()

class Hand(Exception):
    pass