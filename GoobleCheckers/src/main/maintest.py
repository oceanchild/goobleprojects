'''
Created on 2011-10-02

@author: Gooble
'''

if __name__ == '__main__':
    for i in range (0, 8):
            for j in range (0, 8):
                if i < 3 and (i + j) % 2 == 0:
                    print (i, j),