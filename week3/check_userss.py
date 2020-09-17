def check_users(current_users, new_users):
    pass
    current_users_lower = []
    for user in current_users:
        current_users_lower.append(user.lower())
        
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("Unfortunately, that username, has already been taken" )
        else:
            print("That username is still availible")
            
if __name__ == "__main__":
    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)
