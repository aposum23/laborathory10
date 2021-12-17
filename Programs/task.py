#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    u = set('abcdefghijklmnopqrstuvwxyz')
    a = {'a', 'e', 'f', 'i'}
    b = {'a', 'b', 'k', 'n'}
    c = {'e', 'f', 'n', 'o', 'w', 'x'}
    d = {'a', 'd', 'e', 'o', 'p', 't', 'u'}
    x = c.union(a.intersection(b))
    y = (u.difference(a).intersection(u.difference(b))).difference(c.union(d))
    print(f'x = {x}')
    print(f'y = {y}')
