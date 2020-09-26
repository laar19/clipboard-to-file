# Convert selected file list into one single file in order to
# show it on window
def list_to_string(list_):
    string = str()
    for i in range(len(list_)):
        string += str(i+1) + " - " + list_[i] + "\n\n"
    return string

def create_text_file(list_, file_name):
    #file_name = "clipboard.txt"
    file_name += ".txt"
    text_file = open(file_name, "w")

    for i in list_:
        text_file.write(str(i)+"\n")

    text_file.close()

def list_append(list_, var):
    if var not in list_:
        list_.append(var)
        return 0
    return 1