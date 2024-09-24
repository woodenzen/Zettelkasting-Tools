import time
import os

def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        # return the result of the decorated function execution
        return result
    # return reference to the wrapper function
    return wrapper

if __name__ == '__main__':
    @timer
    def count_and_average_links(directory):
        md_file_count = 0
        total_link_count = 0

        for item in os.listdir(directory):
            if item.endswith('.md'):
                md_file_count += 1
                file_path = os.path.join(directory, item)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        link_count = content.count(" [[")
                        total_link_count += link_count
                        # print(f"{item}: {link_count} occurrences of ' [['")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

        if md_file_count > 0:
            average_links = round(total_link_count / md_file_count, 1)
            print(f"Average ' [[' per .md file: {average_links}")
        else:
            print("No .md files found.")

    # Example usage
    directory_path = '/Users/will/Dropbox/zettelkasten'
    count_and_average_links(directory_path)


@timer
def train_model():
    print("Starting the model training function...")
    # simulate a function execution by pausing the program for 5 seconds
    print("Model training completed!")

train_model()    