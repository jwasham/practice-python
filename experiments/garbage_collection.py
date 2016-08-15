"""
Messing around with garbage collection with circular references
and the gc and sys modules. Sys provides getrefcount()
"""

import gc
import sys


def main():
    a = 4
    b = 5

    c_list = []
    c_list.append(123)
    c_list.append(456)
    # reference cycle
    c_list.append(c_list)
    c_list[2].append(789)

    # foo = ['hi']
    # c_list = foo

    print(c_list)

    print("Stats: {}".format(gc.get_stats()))
    print("Count: {}".format(gc.get_count()))
    print("GC enabled: {}".format(gc.isenabled()))
    print("Threshold: {}".format(gc.get_threshold()))
    print("c_list is tracked: {}".format(gc.is_tracked(c_list)))

    """
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to getrefcount().
    """
    print("Reference count for c_list: {}".format(sys.getrefcount(c_list)))
    del c_list[2]
    print("Reference count for c_list: {}".format(sys.getrefcount(c_list)))

    print("Collecting: {}".format(gc.collect()))

    print("Done.")


if __name__ == "__main__":
    main()
