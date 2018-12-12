# -*- coding: utf-8 -*-


def test_max_depth(al=[]):
    al.append(1)
    try:
        test_max_depth()
    except:
        print(len(al))


if __name__ == '__main__':
    test_max_depth()
