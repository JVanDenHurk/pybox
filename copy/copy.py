import shutil
import os

# Path to the original file
original_file = 'script27.mp3'
# Path to the directory where the files will be copied
destination_directory = 'output'

# List of numbers from the image (manually copied here for the script)
numbers = [36, 40, 42, 47, 55, 60, 62, 68, 71, 80, 85, 146, 148, 166, 292, 296, 339, 368, 385, 389, 410, 417, 444, 447, 449, 452, 465, 469, 474, 478, 480, 483, 494, 504, 512, 517, 520, 522, 533, 558, 596, 599, 603, 623, 628, 631, 646, 668, 670, 674, 676, 680, 683, 705, 709, 714, 719, 721, 733, 779, 784, 796, 800, 805, 810, 813, 815, 821, 826, 828, 851, 853, 859, 861, 863, 871, 892, 895, 897, 898, 900, 903, 904, 907, 914, 916, 918, 920, 924, 926, 930, 933, 948, 957, 960, 962, 963, 967, 968, 971, 972, 973, 976, 979, 983, 986, 991, 994, 996, 1022, 1029, 1032, 1034, 1036, 1038, 1046, 1058, 1066, 1071, 1074, 1076, 1082, 1084, 1093, 1095, 1097, 1099, 1101, 1109, 1115, 1117, 1119, 1124, 1143, 1146, 1150, 1153, 1159, 1165, 1169, 1175, 1177, 1179, 1183, 1186, 1188, 1190, 1192, 1194, 1198, 1202, 1208]

# Ensure the destination directory exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through the numbers and copy the original file, renaming it accordingly
for number in numbers:
    destination_file = os.path.join(destination_directory, f'script{number}.mp3')
    shutil.copyfile(original_file, destination_file)

print("Files copied and renamed successfully.")
