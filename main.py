import os
current_dir = os.getcwd()
print(current_dir)
#os.makedirs('parent_dir/child_dir/grandchild_dir')
for dirpath, dirnames, filenames in os.walk('parent_dir'):
    print(f'디렉터리 경로: {dirpath}')
    print(f'디렉터리 이름: {dirnames}')
    print(f'파일이름: {filenames}')

#
# # os.mkdir('new_directory')
# # os.makedirs('parent_dir/child_dir/grandchild_dir')
#
# #change directory
# os.chdir('new_directory')
# current_dir2 = os.getcwd()
# print(current_dir2)
#
# with open('example.txt','w') as file_object:
#     file_object.write('Hello world!')
#
# print('done')
#
# os.rename('new_directory', 'old_directory')