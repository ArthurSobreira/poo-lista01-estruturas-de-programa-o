def list_merge(list_01, list_02):
    org_list_01 = sorted(list_01)
    org_list_02 = sorted(list_02)
    merged_list = []
    c = 0
    while True:
        if (c < len(org_list_01)) and (c < len(org_list_02)):
            if org_list_01[c] < org_list_02[c]:
                merged_list.append(org_list_01[c])
            else:
                merged_list.append(org_list_02[c])
            c += 1
        else:
            return merged_list
