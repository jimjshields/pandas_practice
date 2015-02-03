import pandas as pd
import re
import os

data_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'names'))

year_pattern = re.compile('.*(\d{4})\.txt')
files = [file_name for file_name in os.listdir(data_dir) if re.match(year_pattern, file_name)]
years = [int(re.match(year_pattern, file_name).groups()[0]) for file_name in files]

data_frames = []

for year in years:
	file_name = os.path.join(data_dir, 'yob%d.txt' % (year))
	df = pd.read_csv(file_name, names=['Name', 'Sex', 'Births'])
	df['Year'] = year
	data_frames.append(df)

data_frame = pd.concat(data_frames, ignore_index=True)

# 1 Create a new column in the dataset entitled 'F' with value 1 as an int if the name is female, or 0 if the name if male

# 2 Create a 'M' column the the values inverted, please do this a different way

# 3 Create a column '%' that indicated the percentage each name represents for its year.

# 4 Add a column containing the number of letters in each name

# 5 Add a column that gives (average for the year - number of letters in name) for each name

# 6 Sort by number of births per name

grouped_by_name = data_frame.groupby(['Name'])

# 7 On the original frame, add a column with the first letter of each name

# 8 Which letter has appeared the most? The least?

