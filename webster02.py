#!/usr/bin/python3

def main():
    hostipdict = {'host1': '10.0.2.3', 'host2':'10.0.2.3','host3':'10.0.4.3' }
    print(hostipdict)
    print(hostipdict['host1'])
    hostipdict['host4'] = '10.11.2.5'
    print(hostipdict)
    print(hostipdict.get('yaaa'))
    print(hostipdict.keys())
    print(hostipdict.values())
    print(list(hostipdict.keys()))
    print(list(hostipdict.values()))


if __name__ == '__main__':
    main()
