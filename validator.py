# validator.py

def validate_row(row):
    try:
        email, fname, lname = row[0], row[1], row[2]
        res_addr, res_city, res_state, res_post = row[3], row[4], row[5], row[6]
        post_addr, post_city, post_state, post_post = row[10], row[11], row[12], row[13]

        return all([email, fname, lname, res_addr, res_city, res_state, res_post, post_addr, post_city, post_state, post_post])
    except IndexError:
        return False
