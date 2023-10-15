def remplir_dictionnaire():
    data = []
    for i in range(2):
      print(f"Étudiant {i + 1}")
      item = {}
      for j in range(2):
        subject = input("Veuillez saisir une matiere s["+str(i)+ "] : \n ")
        note = int(input('Enter the note of this subject for this student : '))
        item[subject] = note
      data.append(item)
    return data


def test(lst, marks):
    result = [d[marks] for d in lst if marks in d]
    return result



f = remplir_dictionnaire()
print(f)
subj="math"
print(test(f, subj))