def trim_data(brand, type, usage, grade, size, pct_elongation):
    print(brand, type, usage, grade, size, pct_elongation)
    return [
        brand[brand.index(":") :].strip(),
        type[type.index(":") :].strip(),
        usage[usage.index(":") :].strip(),
        grade[grade.index(":") :].strip(),
        size[size.index(":") :].strip(),
        pct_elongation[pct_elongation.index(":") :].strip(),
    ]
