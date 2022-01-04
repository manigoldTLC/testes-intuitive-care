import utils

file = "file_download.pdf"

table_30 = utils.extract_table(file,
                               "114",
                               area=(295.625, 137.138, 376.689, 320.088))

table_31 = utils.extract_table(file,
                               "115",
                               area=(143.167, 131.932, 746.308, 468.085))

table_31_1 = utils.extract_table(file,
                                 "116",
                                 area=(97.801, 137.138, 747.795, 500.064))

table_31_2 = utils.extract_table(file,
                                 "117",
                                 area=(98.545, 136.395, 741.102, 500.808))

table_31_3 = utils.extract_table(file,
                                 "118",
                                 area=(97.058, 137.138, 748.539, 501.551))

table_31_4 = utils.extract_table(file,
                                 "119",
                                 area=(97.801, 137.138, 741.845, 501.551))

table_31_5 = utils.extract_table(file,
                                 "120",
                                 area=(97.058, 136.395, 316.449, 500.808))

table_32 = utils.extract_table(file,
                               "120",
                               area=(457.008, 132.676, 512.786, 265.055))

utils.convert_to_csv(table_30, "quadro_30")
utils.convert_to_csv(table_31_1, "quadro_31")
utils.convert_to_csv(table_31_2, "quadro_31(1)")
utils.convert_to_csv(table_31_3, "quadro_31(2)")
utils.convert_to_csv(table_31_4, "quadro_31(3)")
utils.convert_to_csv(table_31_5, "quadro_31(4)")
utils.convert_to_csv(table_32, "quadro_32")
