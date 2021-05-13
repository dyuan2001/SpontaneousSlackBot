# returns dict representing the group
def create_group(text):
    args = text.split()
    timeout = 30    # default timeout is 30 min
    members = []
    assert args[0] == "/create"
    groupname = args[1]
    if args[2].isnumeric():
        timeout = int(args[2])
    else:
        members.append(args[2])
    for arg in args[3:]:
        members.append(arg)
    return {"groupname": groupname,
            "timeout": timeout,
            "members": members}


            



if __name__ == "__main__":
    text = "/create testgroup 5 daniel david olga philip raymond"
    print(create_group(text))
    text = "/create testgroup daniel david olga philip raymond"
    print(create_group(text))
        


