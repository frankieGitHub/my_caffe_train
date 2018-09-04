import os

data_root = '/home/coolpad/AI/face_dataset/alive_detect/data'
output_file = './train_file.txt'


index = -1
root_temp = data_root
f_output = open(output_file, 'wr')

for root, dirs, files in os.walk(data_root):
   
    for ff in files:
       
        if root_temp != root:
            index += 1
        item = os.path.join(root,ff) + ' ' + str(index)
        print item
        f_output.writelines(item)
        f_output.writelines('\n')
        #print os.path.join(root, ff)
        #print index
        root_temp = root


