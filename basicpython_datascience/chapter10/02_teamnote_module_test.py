from teamnote import Note
from teamnote import NoteBook

good_sentence1 = """세상 사는데 도움이 되는 명언들 힘이 되는 명언들 용기를 주는 명언들"""

note_1 = Note(good_sentence1)
print(note_1)
note_1.remove()
print(note_1)
note_1.write_content(good_sentence1)
print(note_1)
print()

print(note_1.get_number_of_lines())
print(note_1.get_number_of_characters())
print()


good_sentence2 = """삶이 있는 한 희망은 있다. - 키케로"""
note_2 = Note(good_sentence2)
print(note_2)
print()

good_sentence3 = """하루에 3시간을 걸으면 7넌 후에 지구를 한바퀴 돌 수 있다. - 사무엘존슨"""
note_3 = Note(good_sentence3)
print(note_3)
print()

good_sentence4 = """행복의 문이 하나 닫히면 다른 문이 열린다 그러나 우리는 우리를 향해 열린 문을 보지 못한다. - 헬렌켈러"""
note_4 = Note(good_sentence4)
print(note_4)
print()

wise_saying_notebook = NoteBook('WiseSaying')

wise_saying_notebook.add_note(note_1)
print(wise_saying_notebook.get_number_of_all_pages())
wise_saying_notebook.remove_note(1)
print(wise_saying_notebook.get_number_of_all_pages())
print()

wise_saying_notebook.add_note(note_1)
wise_saying_notebook.add_note(note_2)
wise_saying_notebook.add_note(note_3)
wise_saying_notebook.add_note(note_4)

print(wise_saying_notebook.title)
print(wise_saying_notebook.notes)
print(wise_saying_notebook.get_number_of_all_pages())
print(wise_saying_notebook.page_number)
print()

print(wise_saying_notebook.get_number_of_all_lines())
print(wise_saying_notebook.get_number_of_all_characters())
