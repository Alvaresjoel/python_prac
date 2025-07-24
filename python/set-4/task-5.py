import csv
import math
def insert_into_csv(sq_rt_list):
    with open('square_roots.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number', 'Square Root'])
        
        for item in sq_rt_list:
            print(item)
            writer.writerow([item])
def read_csv():
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
                # print(sq_root)  
                final_list.append([item, sq_root])
            except ValueError:
                print(f"ValueError: {item} is not a number")
            except TypeError as e:
                print(f"TypeError: {e}")
            except Exception as e:
                print(f"Exception: {e}") 
        return final_list    

csv_value = read_csv()
sq_rt = check_sqrt(csv_value)
insert_into_csv(sq_rt)