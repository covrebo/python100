import search_api


def main():
    keyword = input("What is the keyword you would like to search for: ")
    result = search_api.get_episode_by_title(keyword)

    print('#################')
    print('###  RESULTS  ###')
    print('#################')
    print(f"There are {len(result)} episodes found.")
    for r in result:
        print(f'{r.category} {r.id}, titled {r.title}.')


if __name__ == '__main__':
    main()
