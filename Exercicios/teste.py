def teste(matriz):
    result_map = {}
    for item in matriz:
        for year in range(item[0], item[1]):
            year_str = str(year)
            if year_str in result_map:
                result_map[year_str] += 1
            else:
                result_map[year_str] = 1
    return result_map