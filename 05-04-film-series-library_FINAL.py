print(f"Film Library \n")

class Film: # definition of a base class called Film
    def __init__(self, title, release_year,genre, play_count):
        self.title = title 
        self.release_year = release_year
        self.genre = genre
        self.play_count = int(play_count)
    def __str__(self):
            return f'{self.title} ({self.release_year})'#v2 
            #return f'{self.title} {self.release_year} {self.genre} play_count = {self.play_count}'#v1
    def play(self):
        self.play_count += 1

SandF_list = [] # I create a list to store films and series

# Testing Class Film:
harry = Film(title = "Harry", release_year="2004", genre= "Fantasy", play_count="30")
pulpfiction = Film(title = "Pulp Fiction", release_year="1994", genre= "Action", play_count="143")
matrix = Film(title = "Matrix", release_year="1999", genre= "Science Fiction", play_count="205")
matrix2 = Film(title = "Matrix2", release_year="2003", genre= "Science Fiction", play_count="3421")
matrix3 = Film(title = "Matrix3", release_year="2004", genre= "Science Fiction", play_count="5421")
#print(harry)
SandF_list.append(harry)
SandF_list.append(pulpfiction)
SandF_list.append(matrix)
SandF_list.append(matrix2)
SandF_list.append(matrix3)
# Testing play function: 
#harry.play()
#print(SandF_list)

class Serie(Film): # definition of a subclass Serie of a base class Film
    def __init__(self, episode_nr,season_nr, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.episode_nr = int(episode_nr)
        self.season_nr = int(season_nr)
    def __str__(self):
        return f'{self.title} S{self.season_nr:02d}E{self.episode_nr:02d}' #v2    
        #return f'{self.title} {self.release_year} {self.genre} ep: {self.episode_nr:02d} se:  {self.season_nr:02d} count: {self.play_count}'#v1  


# Testing Class Serie ():
lost = Serie(title = "Lost", release_year="2004", genre= "Science-Fiction", episode_nr = "7", season_nr ="2", play_count="13230")
lost2 = Serie(title = "Lost 2", release_year="2004", genre= "Science-Fiction", episode_nr = "8", season_nr ="2", play_count="130")
lost3 = Serie(title = "Lost 3", release_year="2004", genre= "Science-Fiction", episode_nr = "9", season_nr ="2", play_count="12")
simpsons = Serie(title = "The Simpsons", release_year="1990", genre= "Cartoon", episode_nr = "5", season_nr ="4", play_count="42230")
#print(lost)
SandF_list.append(lost)
SandF_list.append(lost2)
SandF_list.append(lost3)
SandF_list.append(simpsons)


#9 Napisz funkcj?? generate_views, kt??ra losowo wybiera element z biblioteki, a nast??pnie dodaje mu losow?? (z zakresu od 1 do 100) ilo???? odtworze??.
#10 Napisz funkcj??, kt??ra uruchomi generate_views 10 razy.

from random import randrange

def display_titles(list):
    for title in list:
        print(f'{title} {title.play_count}')

def generate_views(list):
    i = randrange(len(list))
    views = randrange(100)+1
#    print(f"        I add {views} views to the {i}th item")
    list[i].play_count += views

def generate_views_multi(list,times):
    for i in range(times):
        generate_views(list)

generate_views_multi(SandF_list,10)        

# Napisz funkcj?? top_titles(), kt??ra zwr??ci wybran?? ilo???? najpopularniejszych tytu????w z biblioteki. Dla ch??tnych: dodaj do funkcji parametr content_type, kt??rym wybierzesz czy maj?? zosta?? pokazane filmy, czy seriale.

#print(f'\nTask 11 top_titles(): \n')
def top_titles(list,content_type, howmany):
    by_views = sorted(list, key = lambda film: film.play_count, reverse =True)
    by_views = [item for item in by_views if item.__class__ == content_type]
    for i in range(len(by_views)):
        if i< howmany:
            print(f"{by_views[i].play_count} {by_views[i].title} ")

from datetime import date
today = date.today()

print(f'The most popular films and series as of {today} are: ')
print(f'Top three films:')
top_titles(SandF_list, Film, 3)
print(f'\nTop three films:')
top_titles(SandF_list, Serie, 3)
print("")
#by_speed = sorted(cars, key=lambda car: car.top_speed)


 