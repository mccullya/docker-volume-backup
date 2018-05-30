#!/usr/bin/env python
import os
import sys

def main():
    command = sys.argv[1]
    print 'Running: ' + sys.argv[0] + ' ' + sys.argv[1]
    if command == 'backup':
        backup()
    elif command == 'restore':
        restore()
    else:
        print 'Unrecognized argument: ' + command


def backup():
    print 'Staring volume backup'
    print 'tar -C /input -cvf - ./ | gzip > /output/backup.tar.gz'
    os.system('tar -C /input -cvf - ./ | gzip > /output/backup.tar.gz')
    print 'Volume backup complete'


def restore():
    print 'Restoring Docker volume'
    print 'Running: tar -xvf ' + sys.argv[2] + ' -C /output'
    os.system('tar -xvf ' + sys.argv[2] + ' -C /output')
    print 'Volume restore complete'


if __name__ == '__main__':
    main()


