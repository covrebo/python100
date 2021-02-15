import search_api
import webbrowser


def main():
    # prompt the user for a search term.
    keyword = input("What is the keyword you would like to search for: ")

    # query the talkpython search API
    result = search_api.get_episode_by_title(keyword)

    print('#################')
    print('###  RESULTS  ###')
    print('#################')
    print(f"There are {len(result)} episodes found.")
    for r in result:
        if r.category == 'Episode':
            print(f'{r.category} {r.id}, titled {r.title}.')

    # prompt the user if they would like to view one of the episodes
    episode = input("What episode number do you want to view or [Q]uit: ")

    # check if the user wants to quite
    if episode.strip().lower() == 'q':
        print("Good bye")
    else:
        # validate the input is an int
        try:
            episode = int(episode)
            found = 0
            for r in result:
                if r.id == episode:
                    # open a webpage of the episode
                    webbrowser.open(f"https://talkpython.fm{r.url}", new=2)
                    found = 1
            # return an error message if the number entered was not in the results
            if found == 0:
                print(f'Sorry, episode {episode} was not in the list.')
        # print an error if the value entered wasn't an int
        except:
            print("Sorry you entered an invalid episode number.")


if __name__ == '__main__':
    main()
