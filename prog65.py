cursos = ["python","Powerbi"]
novo_curso = input("Digite um curso para adicionar: ")
cursos.append(novo_curso)
print("\nLista de cursos:")
for curso in cursos:
    print("-",curso)
remover = input("\nDigite o nome do curso que deseja remover: ")
if remover in cursos:
    cursos.remove(remover)
    print("\nCurso removido com sucesso")
else:
    print("\nCurso não encontrado!")
print("\nLista atualizada de cursos:")
for curso in cursos:
    print("-", curso)