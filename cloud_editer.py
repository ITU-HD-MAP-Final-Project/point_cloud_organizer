import os

# CloudCompare
# -O 2021-09-18-10-19-24_Velodyne-HDL-32-Data.las
# -SS OCTREE 16
# -SOR 6 1
# -NOISE KNN 6 REL 1.0 RIP
# -OCTREE_NORMALS auto -MODEL QUADRIC
# -OCTREE_NORMALS auto -MODEL LS
# -FEATURE PLANARITY 0.1
# -FEATURE LINEARITY 0.1
# -SAVE_CLOUDS ALL_AT_ONCE FILE test.bin

directory = "/home/ataparlar/data/hdmap_paper_data/test_clouds/"
terminal_exec_str = "CloudCompare -O "
file_counter = 0
file_list = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    print("file collect")
    file_list.append(filepath)
    print("files collected")

for filepath in file_list:
    print("file '" + filepath + "' is calculating")

    new_file_name = "{:06d}".format(file_counter) + ".bin"
    file_counter += 1

    terminal_exec_str += filepath
    print("execution")
    terminal_exec_str += " -SS OCTREE 16 -SOR 6 1 -NOISE KNN 6 REL 1.0 RIP -OCTREE_NORMALS auto -MODEL QUADRIC -OCTREE_NORMALS auto -MODEL LS -FEATURE PLANARITY 0.1 -FEATURE LINEARITY 0.1 -SAVE_CLOUDS ALL_AT_ONCE FILE "
    terminal_exec_str += new_file_name
    os.system(terminal_exec_str)
    print("executed")

    terminal_exec_str = "CloudCompare -O "

print("done -------------------")








