def fun(file_name, s):
    with open (file_name, 'a') as output_file:
        output_file.write("name, adress, age\n")
        for i in s:
            for j in i:
                output_file.write (j)
                if j != i[-1]:
                    output_file.write (", ")
            output_file.write("\n")      
s = [('Георгий', 'Невский проспект', '22'), ('Иван', 'пр. Ветеранов', '21')]
fun("example_text.txt", s)
