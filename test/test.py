from CachedFunc import CacheManager
from CachedFunc.CacheRepos import MemRepo

cm = CacheManager()


@cm.register
def add(a, b, c=3, *args, **kwargs):
    print('func called')
    return a+b+c+sum(args)+sum(kwargs.values())


if __name__ == '__main__':
    mr = MemRepo()
    mr.save('a', 123)
    mr['b'] = 321
    print(mr.get('a'))
    print('b' in mr)
    print(mr['b'])

    print(cm.add_repo(mr))

    print(add(1, 2, 4))
    print(add(1, b=2, c=4))
    print(add(1, 2, 3))
    print(add(1, 2))
    print(add(1, 2, 3, 4))
    print(add(1, 2, 3, _cached_func_force_refresh=True))
