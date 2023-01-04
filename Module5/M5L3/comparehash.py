import argparse
import os 
from PIL import Image
import imagehash
parser = argparse.ArgumentParser(
                    prog = 'ImageHasher',
                    description = 'Checks images for equal hashes',
                    epilog = 'Text at the bottom of help')
parser.add_argument('folder')

# parser.add_argument('-f', '--folder')
parser.add_argument('output')

# parser.add_argument('-o', '--output')
args = parser.parse_args()

isdir = os.path.isdir(args.folder)

if isdir == True:
    hash_list = []
    dir_list = os.listdir(args.folder)
    print(dir_list, hash_list)

    for i in dir_list:
        hash = imagehash.average_hash(Image.open(f'{args.folder}\{i}'))
        hash_list.append(str(hash))
    
        list_2 = hash_list
        for x in hash_list:
            hash_list.remove(x)

            if x not in hash_list:
                hash_list.append(x)

                print(f'Matching hashes: {x}')
            if x in hash_list:
                print(f'Matching hashes: ', x)
                
    with open(args.output, 'w') as f:
        for x in hash_list:
            f.write(x)
            f.close()
else:
    print('Not a folder, try again')