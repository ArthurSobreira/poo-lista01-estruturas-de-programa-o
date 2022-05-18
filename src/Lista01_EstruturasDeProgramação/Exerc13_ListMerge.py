def list_merge(list_01, list_02):
    merged_list = []
    c = 0
    while True:
        if (c < len(list_01)) and (c < len(list_02)):
            if list_01[c] < list_02[c]:
                merged_list.append(list_01[c])
            else:
                merged_list.append(list_02[c])
            c += 1
        else:
            return merged_list
