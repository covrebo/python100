import api

def main():
    keyword = input("What is the title you would like to search for: ")
    result = api.get_movie_by_title(keyword)

    print(f"There are {len(result)} movies found.")
    for r in result:
        print(f'{r.title} has imdb score {r.imdb_score}')


if __name__ == '__main__':
    main()
