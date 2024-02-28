def get_cats_info(path) -> list:
    list_with_cats_data = []
    try:
        with open(path, "r", encoding="utf-8") as cats_file:
            for line in cats_file.readlines():
                data_about_cat = line.strip().split(",")
                list_with_cats_data.append({
                    "id" : data_about_cat[0],
                    "name" : data_about_cat[1],
                    "age" : data_about_cat[2]                      
                                            })
    except FileNotFoundError:
        print("Input correct path!!!")

    return list_with_cats_data