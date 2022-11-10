import splitfolders

input_folder = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/input/'
output_folder = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output1/'

splitfolders.fixed(input_folder, output=output_folder,
                   seed=1337, fixed=(3200, 900, 1959), group_prefix=None, move=False)
