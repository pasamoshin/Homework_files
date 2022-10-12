import os


def list_files(files_path):
    files_sorted = []
    for root, dirs, files in os.walk(files_path):
        for filename in files:
            files_sorted.append(os.path.join(root, filename))
    return files_sorted


def sorted_files_len(files_sorted):
    files_len = {}
    for file in files_sorted:
        with open(file, encoding='utf-8') as file:
            len_files = len(file.readlines())
        files_len[file.name] = len_files
    return sorted(files_len.items(), key=lambda x: x[1])


def open_file(path):
    with open(path, encoding='utf-8') as file:
        content = file.readlines()
    return ''.join(content)


def write_result_file(files_sorted):
    with open('result.txt', 'w', encoding='utf8') as res:
        for file in files_sorted:
            res.write(os.path.split(file[0])[1] + '\n')
            res.write(str(file[1]) + '\n')
            res.write(open_file(str(file[0])) + '\n')


if __name__ == '__main__':
    files_path = r".\files"
    files = list_files(files_path)
    files_sorted = sorted_files_len(files)
    write_result_file(files_sorted)
