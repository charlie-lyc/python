# 구현 가능한 OOP 만들기 : 노트북 - 노트를 정리하는 프로그램
# 사용자는 note에 뭔가를 적을 수 있다.
# 노트에는 content가 있고 , 그 내용을 제거할 수 있다.
# 노트는 notebook에 삽입된다.
# 노트북은 노트가 삽입될 때 page를 생성하며, 최고 300페이지까지 저장 가능하다.
# 300페이지가 넘으면 더 이상 노트를 삽입하지 못한다.

# class 구상
#             < notebook >         < note >
#               add_note         write_content
# [method]     remove_note        romve_all
#           get_number_of_pages
#
#                 title             content
# [variable]   page_number
#                 notes


class Note(object):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content

    def write_content(self, content):
        self.content = content

    def remove(self):
        self.content = 'Content was deleted.'

    def get_number_of_lines(self):
        return self.content.count('\n') + 1

    def get_number_of_characters(self):
        return len(self.content)


class NoteBook(object):

    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def __str__(self):
        return 'This is a ' + title + ' notebook.'

    def add_note(self, note, page=0):
        if type(note) != Note:
            raise ValueError('Invalid note')
        if len(self.notes.keys()) < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                for page in range(1, 300):
                    if page in self.notes.keys():
                        print('Page already exists.')
                        break
                    self.notes[page] = note
                    self.page_number += 1
        else:
            print('Notebook is full of notes.')

    def remove_note(self, page):
        if page in self.notes.keys():
            del self.notes[page]
            # self.notes.pop(page)
        else:
            print('There is no page.')

    def get_number_of_all_pages(self):
        return len(self.notes.keys())

    def get_number_of_all_lines(self):
        count = 0
        for page in self.notes.keys():
            num_lines = self.notes[page].get_number_of_lines()
            count += num_lines
        return count

    def get_number_of_all_characters(self):
        count = 0
        for page in self.notes.keys():
            num_characters = self.notes[page].get_number_of_characters()
            count += num_characters
        return count
