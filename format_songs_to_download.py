# Takes in a text file of songs. Each artist/song is on it's own line.
# Goal: Format my list of

old_filename = 'C:\\Users\\steve\\Desktop\\songs_to_download.txt'
new_filename = 'C:\\Users\\steve\\Desktop\\formatted_songs_to_download.txt'


with open(old_filename, 'r') as input_file, open(new_filename, 'w') as output_file:

    for element in input_file:
        parts = element.split(' - ')
        print(parts)
        formatted_contents = parts[0].title() + ' - ' + parts[-1].title()
        print('Formatted contents: ' + formatted_contents)
        print(formatted_contents, file=output_file)

