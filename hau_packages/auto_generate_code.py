
def generate_code(code_dict, key_code, prefix):
    count_in_list = 1
    list_code = []
    list_int_code = []
    for code in code_dict:
        list_code.append(code[key_code])
    for code in list_code:
        int_code = int(code.split(f"{prefix}")[-1])
        list_int_code.append(int_code)
    while count_in_list in list_int_code:
        count_in_list += 1
    
    code_generated = prefix + f'{count_in_list:08}'
    return code_generated





