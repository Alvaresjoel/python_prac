import csv
import math
def insert_into_csv(sqrt_list):
    try:
        with open('square_roots.csv', 'w', newline='') as sq_rt:
            writer = csv.writer(sq_rt)
            writer.writerow(['Number', 'Square Root'])
            for item in sqrt_list:
                # print(item)
                writer.writerow([item])
    except FileNotFoundError as f:
        raise f
        
def read_csv():
    try:
        with open('numbers.csv','r') as numbers_file:
            number_csv = csv.reader(numbers_file)
            # print(number_csv)
            line_count = 0
            new_csv = []
            for item in number_csv:
                # print(item)
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
                    new_csv.append(item[0])
    except FileNotFoundError as f :
        raise f
    else : 
        return new_csv
    
def check_sqrt(value_list):
    
        final_list = []
        for item in value_list:
            try:
                item = int(item)
                if item < 0 :
                    raise Exception("Skipping invalid or negative entry:{item}")
                if not isinstance(item,int):
                    raise TypeError("Skipping invalid or non-numeric entry:{item}")
                sq_root =  math.sqrt(item)
                print(f'Square root of {item} is :{sq_root}')  
                final_list.append([item, sq_root])
            except ValueError as val:
                raise val
            except TypeError as t:
                raise t
            except Exception as e:
                raise e
        return final_list    
try :
    csv_value = read_csv()
    sq_rt = check_sqrt(csv_value)
    insert_into_csv(sq_rt)
except TypeError as t :
    print(TypeError)
except ValueError as val:
    print(ValueError)
except Exception as e:
    print(Exception)