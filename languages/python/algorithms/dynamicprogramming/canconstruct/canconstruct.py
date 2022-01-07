#!/usr/bin/env python3


def canconstruct(phrase, array=[]):
    print(phrase, array)
    for str in array:
        if str in phrase:
            phrase_split = phrase.split(str)
            phrase1 = phrase_split[0]
            phrase2 = phrase_split[1:][0] #concatanation and getting the string
            can1 = True
            can2 = True
            if len(phrase1) > 0:
                can1 = canconstruct(phrase1, array)
            if len(phrase2) > 0:
                can2 = canconstruct(phrase2, array)
            if can1 and can2:
                return True
    return False


print(canconstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(canconstruct('skateboard', ['bo','rd','ate','t','ska','sk', 'boar']))


# no need to compare middle part of the string. And empty string is always matchable

def canconstructMethod2(phrase, array=[]):
    if len(phrase) == 0:
        return True
    else:
        for str in array:
            if phrase.startswith(str):
                phrase_reset = phrase.split(str)[1]
                if canconstructMethod2(phrase_reset, array):
                    return True
        return False



print('\n canconstructMethod2')
print(canconstructMethod2('abcdef', ['ab','abc','cd','def','abcd']))
print(canconstructMethod2('skateboard', ['bo','rd','ate','t','ska','sk', 'boar']))
print(canconstructMethod2('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
['e','ee','eee','eeee','eeeee']))


def canconstructMemoize(phrase, array=[], mem=None):
    if mem is None:
        mem = {}
    if len(phrase) == 0:
        return True
    elif phrase in mem:
        return mem[phrase]
    else:
        for str in array:
            if phrase.startswith(str):
                phrase_reset = phrase.split(str)[1]
                if canconstructMemoize(phrase_reset, array, mem):
                    mem[phrase] = True
                    return True
        mem[phrase] = False
        return False



print('\n canconstructMemoize')
print(canconstructMemoize('abcdef', ['ab','abc','cd','def','abcd']))
print(canconstructMemoize('skateboard', ['bo','rd','ate','t','ska','sk', 'boar']))