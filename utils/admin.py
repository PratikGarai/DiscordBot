def get_admins() :
    admins = []
    admins.append(int(open("admin_id.txt", "r").read()))

    return admins


def isAdmin(id : int) :
    return id in get_admins()
    
# def adminVerifyAndReact(ctx : 