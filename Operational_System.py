import math
#  Convert and Clean Data: 
# o Convert all file counts into integers. 
# o Convert systems_operational to a Boolean. 
# o Verify the data types of all variables using type(). 
# 2. Compute Summary Statistics: 
# o Calculate the total number of files processed. 
# o Estimate the total processing time for all files combined. 
# o Compute the average file size. 
# 3. Data Integrity Check: 
# o Check if "API" exists as a key in data_sources. 
# o Add a new data source "Cloud" with format "parquet". 
# o Print all sources and their formats. 
# 4. Reflection: 
# o In a comment, explain which of the data structures used here are mutable and 
# which are immutable, and why that matters in a data engineering workflow.
#  
# Expected Output Example: 
# Converted file counts: [120, 95, 135] 
# Systems operational: True 
# Total files processed: 350 
# Total processing time: 857.5 seconds 
# Average file size: 11.38 MB 
# Data sources: {'API': 'json', 'CSV': 'csv', 'IoT': 'xml', 'Cloud': 'parquet'} 
# 'API' found in data sources: True

#  Provided: 
# file_counts = ["120", "95", "135"]         # From API, CSV, IoT respectively 
# avg_time_per_file = 2.45                   # In seconds 
# systems_operational = "True"               
# # String value from a JSON 
# response 
# data_sources = {"API": "json", "CSV": "csv", "IoT": "xml"} 
# file_sizes = [12.4, 8.9, 15.6, 9.8, 10.2]  # In MB


# o Convert all file counts into integers. 
file_counts = ["120","95","135"]
file_counts[0] = int(file_counts[0])
file_counts[1] = int(file_counts[1])
file_counts[2] = int(file_counts[2])
# To convert a string in a List we use the index number of the value in the list

#converted_fc = list(map(lambda x: int(x), file_counts))
print(file_counts)

# o Convert systems_operational to a Boolean. 
systems_operational = "True"
converted_so = bool(systems_operational)
print('Systems operational:', converted_so)

# o Verify the data types of all variables using type().
all_vars = (file_counts, converted_so)
vars_d_type = tuple(map(lambda y: type(y), all_vars))
print('Verified data types:', vars_d_type)

# o Calculate the total number of files processed.
file_sum = sum(file_counts)
print('Total files processed:', file_sum)

# o Estimate the total processing time for all files combined.
avg_time_per_file = 2.45
total_pt = avg_time_per_file * file_sum
print(f'Total processing time: {total_pt:.1f}')

# Compute the average file size.
# Average file size: 11.38 MB
file_sizes = [12.4, 8.9, 15.6, 9.8, 10.2]
avg_size = round(sum(file_sizes) / len(file_sizes), 2)
print('Average file size:', avg_size)

# Check if "API" exists as a key in data_sources.
loop_result = bool()
target_key = 'API'
target_result = lambda: f"{target_key} found in data sources: {loop_result}"
data_source = {
    'API': 'json',
    'CSV': 'csv',
    'IoT': 'xml'
}
for key in data_source.keys():
    if key == target_key:
        loop_result = True
print(target_result())

# o Add a new data source "Cloud" with format "parquet".
data_source["Cloud"] = "parquet"
print('New data source:', data_source)

#Print all sources and their formats.
print('Data source and Formats:')
for key in data_source.keys():
    print(f'{key} | {data_source[key]}')






# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE