#Create a student grade processor that: 
# • Uses a list of student scores (mix of valid and invalid data)
#  • Uses if-else to classify each score as "Pass" (≥60) or "Fail" (<60) 
# • Uses a for loop to process all scores
# • Skips any negative scores with continue 
# • Prints results for each valid score 
# • Counts total passing and failing students

STUDENTS_RECORD = [
    {"name": "Joshua", "score": 85},
    {"name": "John", "score": 45},
    {"name": "Esther", "score": 150},
    {"name": "Yemi", "score": -50},
    {"name": "Davy", "score": 100},
    {"name": "Nelly", "score": 30},
]

COUNT_PASS = 0
COUNT_FAIL= 0

def STAR_COUNT(y):
    record = STUDENTS_RECORD[y]
    if record['score'] > 90 and record['score'] <= 100:
        return '5 STARS'
    elif record['score'] > 50 and record['score'] <= 90:
        return '3 STARS'
    else:
        return '0 STARS'

print("\n\033[33m[ STUDENT GRADE PROCESSOR ]\033[0m\n")
space_gen = lambda z: " " * (20 - z)
print("\n\033[33mNAME               SCORE               STATUS               STAR\033[0m\n")
for index in range(len(STUDENTS_RECORD)):
    
    if STUDENTS_RECORD[index]['score'] < 0 or STUDENTS_RECORD[index]['score'] > 100: continue

    if STUDENTS_RECORD[index]['score'] > 60:
        COUNT_PASS += 1
        print(f"{STUDENTS_RECORD[index]['name']}{space_gen(len(STUDENTS_RECORD[index]['name']))}{STUDENTS_RECORD[index]['score']}{space_gen(len(str(STUDENTS_RECORD[index]['score'])))}PASS{space_gen(len('PASS'))}{STAR_COUNT(index)}")
    else:
        COUNT_FAIL += 1
        print(f"{STUDENTS_RECORD[index]['name']}{space_gen(len(STUDENTS_RECORD[index]['name']))}{STUDENTS_RECORD[index]['score']}{space_gen(len(str(STUDENTS_RECORD[index]['score'])))}FAIL{space_gen(len('FAIL'))}{STAR_COUNT(index)}")
print('\n\033[33m[  STUDENT GRADE SUMMARY  ]\033[0m', end='\n\n')
print(f'Total Passed Students: {COUNT_PASS}')
print(f'Total Failed Students: {COUNT_FAIL}')





# FOR MORE INFORMATION CONCERNING THIS PROJECT OR REPO - LOCATE THE README.mb FILE