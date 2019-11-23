import os 
 
 
def search_bytes_r(file_path, marker, buffer_size=1024): 
    """ 
    Search specific bytes(marker) from the end of a file, 
    and then, return start offset of the bytes. 
 
    Arguments: 
        file_path {file} 
        marker {bytes} -- specific bytes to find. e.g. b'\\xff\\xd9' 
     
    Keyword Arguments: 
        buffer_size {int} -- (default: {1024}) 
 
    Returns: 
        int -- if found, return start offset of the bytes. else, return -1. 
    """ 
     
    with open(file_path, "rb") as f: 
        f.seek(0, os.SEEK_END)  # 파일의 끝에서부터 탐색 
        remaining_size = file_size = f.tell() 
        offset = 0 
 
        while(remaining_size > 0): 
            offset = min(file_size, offset + buffer_size) 
            f.seek(-offset, os.SEEK_END) 
            # 버퍼에 데이터 저장 및 탐색 
            buffer = f.read(min(remaining_size, buffer_size)) 
            remaining_size -= buffer_size 
            idx = buffer.find(marker) 
            # marker를 못찾았다면, 
            # 버퍼 크기에 따라 marker가 잘리는 경우도 있으므로 확인해야 함 
            if(idx == -1): 
                offset = offset + len(marker) - 1 
                if(offset < file_size): 
                    f.seek(-offset, os.SEEK_END) 
                    buffer = f.read(len(marker)*2 - 2) 
                    idx = buffer.find(marker) 
 
            # marker를 찾았다면 위치 offset 반환 
            if(idx != -1): 
                return file_size - offset + idx 
 
        return -1 
 
 
def insert_bytes_into_file(file_path, idx, data):
    """
    Create a new file with data inserted
    
    Arguments:
        file_path {file}
        idx {int} -- index into which data will be insert
        data {bytes} -- data you want to insert
    """
    file_name = os.path.basename(file_path)
    new_file_path = "./new_" + file_name

    with open(file_path, "rb") as old_file, open(new_file_path, "wb") as new_file:
        new_file.write(old_file.read(idx))
        new_file.write(data)
        new_file.write(old_file.read())


def remove_bytes_a_to_b(file_path, start, end):
    """
    Create a new file with data removed start_index to end_index
    
    Arguments:
        file_path {[type]} -- [description]
        start {[type]} -- [description]
        end {[type]} -- [description]
    """
    file_name = os.path.basename(file_path)
    new_file_path = "./recover_" + file_name

    with open(file_path, "rb") as old_file, open(new_file_path, "wb") as new_file:
        new_file.write(old_file.read(start))
        old_file.seek(end+1, os.SEEK_SET)
        new_file.write(old_file.read())


if __name__ == "__main__": 
    pass