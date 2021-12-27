#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    hidden = dir(hidden_4)
    for search_ in hidden:
        if search_[0] != '_':
            print(search_)
